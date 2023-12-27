from unittest.mock import patch

import pytest
from loguru import logger

from langstring.langstring_control import LangStringControl
from langstring.langstring_control import LangStringFlag


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
        (LangStringFlag.ENSURE_VALID_LANG, True),
        (LangStringFlag.VERBOSE_MODE, False),
    ],
)
def test_set_flag_valid(flag: LangStringFlag, state: bool) -> None:
    """Test setting a flag with valid values."""
    LangStringControl.set_flag(flag, state)
    assert LangStringControl.get_flag(flag) == state, "Flag state should be updated correctly"


@pytest.mark.parametrize("flag, state", [("InvalidFlag", True), (123, False)])
def test_set_flag_invalid(flag, state) -> None:
    """Test setting a flag with invalid flag values."""
    with pytest.raises(TypeError, match="Invalid flag received. Valid flags are:"):
        LangStringControl.set_flag(flag, state)


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
        LangStringFlag.VERBOSE_MODE,
    ],
)
def test_get_flag_valid(flag: LangStringFlag) -> None:
    """Test retrieving the state of a valid flag."""
    LangStringControl.set_flag(flag, True)  # Set flag to True for testing
    assert LangStringControl.get_flag(flag) is True, "Flag state should be retrievable"


def test_get_flag_invalid() -> None:
    """Test retrieving the state of an invalid flag."""
    with pytest.raises(TypeError, match="Invalid flag received. Valid flags are:"):
        LangStringControl.get_flag("InvalidFlag")


def test_get_flags() -> None:
    """Test retrieving the states of all flags."""
    expected_flags = {
        LangStringFlag.ENSURE_TEXT: False,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
        LangStringFlag.VERBOSE_MODE: False,
    }
    assert LangStringControl.get_flags() == expected_flags, "All flags should be retrieved correctly"


def test_log_flags() -> None:
    """Test logging the state of all flags."""
    with patch.object(logger, "info") as mock_logger:
        LangStringControl.log_flags()
        for flag in LangStringFlag:
            mock_logger.assert_any_call(f"{flag.name} = {LangStringControl.get_flag(flag)}")


@pytest.mark.parametrize(
    "flag, initial_state, new_state",
    [
        (LangStringFlag.ENSURE_TEXT, False, True),
        (LangStringFlag.ENSURE_ANY_LANG, True, False),
        (LangStringFlag.ENSURE_VALID_LANG, False, True),
        (LangStringFlag.VERBOSE_MODE, True, False),
    ],
)
def test_toggle_flag_state(flag: LangStringFlag, initial_state: bool, new_state: bool) -> None:
    """Test toggling the state of a flag.

    :param flag: The LangStringFlag to be toggled.
    :param initial_state: The initial state to set for the flag.
    :param new_state: The new state to set for the flag.
    """
    LangStringControl.set_flag(flag, initial_state)
    assert LangStringControl.get_flag(flag) == initial_state, "Initial flag state should be set correctly"
    LangStringControl.set_flag(flag, new_state)
    assert LangStringControl.get_flag(flag) == new_state, "Flag state should be toggled correctly"


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
        LangStringFlag.VERBOSE_MODE,
    ],
)
def test_default_flag_state(flag: LangStringFlag) -> None:
    """Test the default state of flags.

    :param flag: The LangStringFlag to check the default state for.
    """
    assert LangStringControl.get_flag(flag) is False, "Default state of the flag should be False"


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, None),
        (LangStringFlag.ENSURE_ANY_LANG, "True"),
        (LangStringFlag.ENSURE_VALID_LANG, 1),
        (LangStringFlag.VERBOSE_MODE, 0),
    ],
)
def test_set_flag_invalid_state_type(flag: LangStringFlag, state) -> None:
    """Test setting a flag with invalid state types.

    :param flag: The LangStringFlag to be set.
    :param state: The invalid state type to set for the flag.
    """
    with pytest.raises(TypeError, match="State must be a boolean"):
        LangStringControl.set_flag(flag, state)


def test_get_flags_after_modification() -> None:
    """Test retrieving the states of all flags after modification."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    flags = LangStringControl.get_flags()
    assert flags[LangStringFlag.ENSURE_TEXT] is True, "Modified flag should reflect the new state"
    assert all(
        flags[flag] is False for flag in LangStringFlag if flag != LangStringFlag.ENSURE_TEXT
    ), "Unmodified flags should remain in their default state"


def test_reset_flags_to_default() -> None:
    """Test resetting all flags to their default values.

    This test ensures that the reset_flags method sets all flags to their default state, which is False.
    """
    # Set all flags to True for testing
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, True)

    # Reset all flags
    LangStringControl.reset_flags()

    # Assert that all flags are reset to False
    assert all(
        not LangStringControl.get_flag(flag) for flag in LangStringFlag
    ), "All flags should be reset to their default state (False)"


def test_reset_flags_idempotence() -> None:
    """Test the idempotence of the reset_flags method.

    This test ensures that calling reset_flags multiple times does not change the outcome, i.e., all flags
    should remain in their default state (False) after multiple resets.
    """
    # Reset flags twice
    LangStringControl.reset_flags()
    LangStringControl.reset_flags()

    # Assert that all flags are still False
    assert all(
        not LangStringControl.get_flag(flag) for flag in LangStringFlag
    ), "Multiple resets should not change the state of the flags (remain False)"


def test_reset_flags_effectiveness() -> None:
    """
    Test the effectiveness of the reset_flags method in resetting all flags to False.

    This test ensures that after modifying the flags, calling reset_flags resets them all to their default state (False).

    :raises AssertionError: If any flag does not reset to False after calling reset_flags.
    """
    # Set all flags to True for testing
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, True)

    LangStringControl.reset_flags()

    assert all(
        not LangStringControl.get_flag(flag) for flag in LangStringFlag
    ), "All flags should be reset to False after calling reset_flags"


def test_instantiation_of_langstringcontrol() -> None:
    """
    Test that instantiation of LangStringControl raises a TypeError.

    This test ensures that LangStringControl, being a static configuration manager, cannot be instantiated due to
    the NonInstantiable metaclass.

    :raises AssertionError: If LangStringControl can be instantiated without raising a TypeError.
    """
    with pytest.raises(TypeError, match="LangStringControl class cannot be instantiated."):
        LangStringControl()


@pytest.mark.parametrize(
    "initial_state, new_state",
    [
        (False, True),
        (True, False),
    ],
)
def test_flag_state_persistence(initial_state: bool, new_state: bool) -> None:
    """
    Test the persistence of flag states after modification.

    This test verifies that once a flag's state is modified, it persists until explicitly changed again.

    :param initial_state: The initial state to set for a flag.
    :param new_state: The new state to set for the same flag.
    :raises AssertionError: If the flag state does not persist as expected.
    """
    flag = LangStringFlag.ENSURE_TEXT
    LangStringControl.set_flag(flag, initial_state)
    assert LangStringControl.get_flag(flag) == initial_state, "Initial flag state should persist"

    LangStringControl.set_flag(flag, new_state)
    assert LangStringControl.get_flag(flag) == new_state, "Modified flag state should persist"
