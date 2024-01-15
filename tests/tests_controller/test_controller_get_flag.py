import pytest

from langstring import Controller
from langstring import GlobalFlag
from langstring import LangStringFlag
from langstring import MultiLangStringFlag
from langstring import SetLangStringFlag

# Combine all flag types into a single list for parametrization
all_flags = (
    list(LangStringFlag.__members__.values())
    + list(SetLangStringFlag.__members__.values())
    + list(MultiLangStringFlag.__members__.values())
    + list(GlobalFlag.__members__.values())
)


@pytest.mark.parametrize("flag", all_flags)
def test_get_flag_valid(flag) -> None:
    """Test retrieving the state of a valid flag."""
    Controller.set_flag(flag, True)  # Set flag to True for testing
    assert Controller.get_flag(flag) is True, "Flag state should be retrievable"


@pytest.mark.parametrize("flag, expected_state", [(flag, False) for flag in all_flags])
def test_get_flag_default_states(flag, expected_state: bool) -> None:
    """Test retrieving the default state of each flag."""
    # Handle exceptions where the default state is not False
    if flag in [LangStringFlag.PRINT_WITH_QUOTES, LangStringFlag.PRINT_WITH_LANG]:
        expected_state = True
    assert Controller.get_flag(flag) == expected_state


@pytest.mark.parametrize("flag, state_to_set", [(flag, True) for flag in all_flags])
def test_get_flag_after_setting_state(flag, state_to_set: bool) -> None:
    """Test retrieving the state of a flag after setting it to a specific state."""
    Controller.set_flag(flag, state_to_set)
    assert Controller.get_flag(flag) == state_to_set, f"State of {flag.name} should be {state_to_set} after setting"


def test_get_flag_nonexistent() -> None:
    """Test retrieving the state of a nonexistent flag."""
    with pytest.raises(
        TypeError,
        match="Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag",
    ):
        Controller.get_flag("NonexistentFlag")


@pytest.mark.parametrize("invalid_flag", [123, 4.5, None, [], {}])
def test_get_flag_invalid_type(invalid_flag) -> None:
    """Test retrieving the state of a flag with an invalid type."""
    with pytest.raises(
        TypeError,
        match="Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag",
    ):
        Controller.get_flag(invalid_flag)
