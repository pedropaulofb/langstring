import pytest

from langstring import LangStringFlag


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
    ],
)
def test_get_flag_valid(flag: LangStringFlag) -> None:
    """Test retrieving the state of a valid flag."""
    Controller.set_flag(flag, True)  # Set flag to True for testing
    assert Controller.get_flag(flag) is True, "Flag state should be retrievable"


def test_get_flag_invalid() -> None:
    """Test retrieving the state of an invalid flag."""
    with pytest.raises(TypeError, match="received. Valid flags are members of"):
        Controller.get_flag("InvalidFlag")


import pytest
from langstring import Controller, LangStringFlag


@pytest.mark.parametrize(
    "flag, expected_state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
        (LangStringFlag.ENSURE_VALID_LANG, False),
    ],
)
def test_get_flag_default_states(flag: LangStringFlag, expected_state: bool) -> None:
    """
    Test retrieving the default state of each flag.

    :param flag: The flag to be tested.
    :param expected_state: The expected default state of the flag.
    """
    assert Controller.get_flag(flag) == expected_state, f"Default state of {flag.name} should be {expected_state}"


@pytest.mark.parametrize(
    "flag, state_to_set",
    [
        (LangStringFlag.ENSURE_TEXT, False),
        (LangStringFlag.ENSURE_ANY_LANG, True),
        (LangStringFlag.ENSURE_VALID_LANG, True),
    ],
)
def test_get_flag_after_setting_state(flag: LangStringFlag, state_to_set: bool) -> None:
    """
    Test retrieving the state of a flag after setting it to a specific value.

    :param flag: The flag to be tested.
    :param state_to_set: The state to set for the flag.
    """
    Controller.set_flag(flag, state_to_set)
    assert Controller.get_flag(flag) == state_to_set, f"State of {flag.name} should be {state_to_set} after setting"


def test_get_flag_nonexistent() -> None:
    """
    Test retrieving the state of a nonexistent flag.
    """
    with pytest.raises(TypeError, match="Invalid flag .* received. Valid flags are members of LangStringFlag."):
        Controller.get_flag("NonexistentFlag")


@pytest.mark.parametrize("invalid_flag", [123, 4.5, None, [], {}])
def test_get_flag_invalid_type(invalid_flag) -> None:
    """
    Test retrieving the state of a flag with an invalid type.

    :param invalid_flag: An invalid flag type to be tested.
    """
    with pytest.raises(TypeError, match="Invalid flag .* received. Valid flags are members of LangStringFlag."):
        Controller.get_flag(invalid_flag)
