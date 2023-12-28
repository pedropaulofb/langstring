import pytest

from langstring import LangStringControl
from langstring import LangStringFlag


def test_get_flags() -> None:
    """Test retrieving the states of all flags."""
    expected_flags = {
        LangStringFlag.ENSURE_TEXT: True,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
    }
    assert LangStringControl.get_flags() == expected_flags, "All flags should be retrieved correctly"


def test_get_flags_after_modification() -> None:
    """Test retrieving the states of all flags after modification."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    flags = LangStringControl.get_flags()
    assert flags[LangStringFlag.ENSURE_TEXT] is True, "Modified flag should reflect the new state"
    assert all(
        flags[flag] is False for flag in LangStringFlag if flag != LangStringFlag.ENSURE_TEXT
    ), "Unmodified flags should remain in their default state"


def test_get_flags_after_reset() -> None:
    """
    Test retrieving the states of all flags after resetting them to their default values.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    LangStringControl.reset_flags()
    expected_flags = {
        LangStringFlag.ENSURE_TEXT: True,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
    }
    assert LangStringControl.get_flags() == expected_flags, "Flags should return to default states after reset"


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, False),
        (LangStringFlag.ENSURE_ANY_LANG, True),
        (LangStringFlag.ENSURE_VALID_LANG, True),
    ],
)
def test_get_flags_individual_modifications(flag: LangStringFlag, state: bool) -> None:
    """
    Test retrieving the states of all flags after individually modifying each flag.

    :param flag: The flag to be modified.
    :param state: The new state to set for the flag.
    """
    LangStringControl.set_flag(flag, state)
    flags = LangStringControl.get_flags()
    assert flags[flag] == state, f"State of {flag.name} should be {state} after modification"
    LangStringControl.reset_flags()  # Reset flags to default after test


def test_get_flags_immutable_return() -> None:
    """
    Test that the dictionary returned by get_flags is a copy and does not modify the original flags.
    """
    original_flags = LangStringControl.get_flags()
    modified_flags = LangStringControl.get_flags()
    modified_flags[LangStringFlag.ENSURE_TEXT] = not original_flags[LangStringFlag.ENSURE_TEXT]
    assert (
        LangStringControl.get_flags() == original_flags
    ), "Modifying the returned dictionary should not affect original flags"
