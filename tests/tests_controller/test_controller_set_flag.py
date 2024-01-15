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


@pytest.mark.parametrize("flag, state", [(flag, True) for flag in all_flags])
def test_set_flag_valid(flag, state) -> None:
    """Test setting a flag with valid values."""
    Controller.set_flag(flag, state)
    assert Controller.get_flag(flag) == state, "Flag state should be updated correctly"


@pytest.mark.parametrize("flag, state", [("InvalidFlag", True), (123, False)])
def test_set_flag_invalid(flag, state) -> None:
    """Test setting a flag with invalid flag values."""
    with pytest.raises(
        TypeError,
        match="Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag",
    ):
        Controller.set_flag(flag, state)


@pytest.mark.parametrize("flag, state", [(flag, None) for flag in all_flags] + [(flag, 1) for flag in all_flags])
def test_set_flag_invalid_state_type(flag, state) -> None:
    """Test setting a flag with invalid state types."""
    with pytest.raises(TypeError, match="State must be a boolean"):
        Controller.set_flag(flag, state)


@pytest.mark.parametrize("flag, initial_state, new_state", [(flag, False, True) for flag in all_flags])
def test_toggle_flag_state(flag, initial_state: bool, new_state: bool) -> None:
    Controller.set_flag(flag, initial_state)
    assert Controller.get_flag(flag) == initial_state
    Controller.set_flag(flag, new_state)
    assert Controller.get_flag(flag) == new_state


@pytest.mark.parametrize("flag_sequence, state_sequence", [([flag for flag in all_flags], [True for _ in all_flags])])
def test_set_multiple_flags_sequentially(flag_sequence, state_sequence):
    for flag, state in zip(flag_sequence, state_sequence):
        Controller.set_flag(flag, state)
    for flag, state in zip(flag_sequence, state_sequence):
        assert Controller.get_flag(flag) == state


@pytest.mark.parametrize("flag, state", [(flag, True) for flag in all_flags])
def test_set_flag_same_value_multiple_times(flag, state: bool):
    for _ in range(3):
        Controller.set_flag(flag, state)
    assert Controller.get_flag(flag) == state
