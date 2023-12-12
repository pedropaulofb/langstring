from unittest.mock import patch

import pytest
from loguru import logger

from langstring.langstring_control import LangStringControl
from langstring.langstring_control import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags():
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
    yield


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
        (LangStringFlag.ENSURE_VALID_LANG, True),
        (LangStringFlag.VERBOSE_MODE, False),
    ],
)
def test_set_flag_valid(flag: LangStringFlag, state: bool):
    """Test setting a flag with valid values."""
    LangStringControl.set_flag(flag, state)
    assert LangStringControl.get_flag(flag) == state, "Flag state should be updated correctly"


@pytest.mark.parametrize("flag, state", [("InvalidFlag", True), (123, False)])
def test_set_flag_invalid(flag, state):
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
def test_get_flag_valid(flag: LangStringFlag):
    """Test retrieving the state of a valid flag."""
    LangStringControl.set_flag(flag, True)  # Set flag to True for testing
    assert LangStringControl.get_flag(flag) is True, "Flag state should be retrievable"


def test_get_flag_invalid():
    """Test retrieving the state of an invalid flag."""
    with pytest.raises(TypeError, match="Invalid flag received. Valid flags are:"):
        LangStringControl.get_flag("InvalidFlag")


def test_get_flags():
    """Test retrieving the states of all flags."""
    expected_flags = {
        LangStringFlag.ENSURE_TEXT: False,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
        LangStringFlag.VERBOSE_MODE: False,
    }
    assert LangStringControl.get_flags() == expected_flags, "All flags should be retrieved correctly"


def test_log_flags():
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
def test_toggle_flag_state(flag: LangStringFlag, initial_state: bool, new_state: bool):
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
def test_default_flag_state(flag: LangStringFlag):
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
def test_set_flag_invalid_state_type(flag: LangStringFlag, state):
    """Test setting a flag with invalid state types.

    :param flag: The LangStringFlag to be set.
    :param state: The invalid state type to set for the flag.
    """
    with pytest.raises(TypeError, match="State must be a boolean"):
        LangStringControl.set_flag(flag, state)


def test_get_flags_after_modification():
    """Test retrieving the states of all flags after modification."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    flags = LangStringControl.get_flags()
    assert flags[LangStringFlag.ENSURE_TEXT] is True, "Modified flag should reflect the new state"
    assert all(
        flags[flag] is False for flag in LangStringFlag if flag != LangStringFlag.ENSURE_TEXT
    ), "Unmodified flags should remain in their default state"
