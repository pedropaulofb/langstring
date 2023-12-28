import pytest

from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
    ],
)
def test_default_flag_state(flag: LangStringFlag) -> None:
    """Test the default state of flags.

    :param flag: The LangStringFlag to check the default state for.
    """
    assert LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not LangStringControl.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not LangStringControl.get_flag(LangStringFlag.ENSURE_VALID_LANG)


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


def test_multiple_flag_modifications_integrity() -> None:
    """
    Test the integrity of flag states after multiple modifications.

    This test ensures that modifications to different flags do not interfere with each other's states.

    :raises AssertionError: If the state of any flag is not as expected after multiple modifications.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, False)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    assert LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT), "ENSURE_TEXT flag should be True"
    assert not LangStringControl.get_flag(LangStringFlag.ENSURE_ANY_LANG), "ENSURE_ANY_LANG flag should be False"
    assert LangStringControl.get_flag(LangStringFlag.ENSURE_VALID_LANG), "ENSURE_VALID_LANG flag should be True"

    LangStringControl.reset_flags()  # Reset flags to default after test


def test_flag_state_consistency_across_methods() -> None:
    """
    Test the consistency of flag states across different methods.

    This test checks if the flag states remain consistent when accessed through get_flag and get_flags methods.

    :raises AssertionError: If the flag states are inconsistent across different methods.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    all_flags = LangStringControl.get_flags()

    assert (
        LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT) == all_flags[LangStringFlag.ENSURE_TEXT]
    ), "Flag state should be consistent across get_flag and get_flags methods"

    LangStringControl.reset_flags()  # Reset flags to default after test
