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


@pytest.mark.parametrize("flag, expected_state", [(flag, False) for flag in all_flags])
def test_default_flag_state(flag, expected_state: bool):
    # Handle exceptions where the default state is not False
    if flag in [LangStringFlag.PRINT_WITH_QUOTES, LangStringFlag.PRINT_WITH_LANG]:
        expected_state = True
    assert Controller.get_flag(flag) == expected_state


def test_instantiation_of_langstringcontrol():
    with pytest.raises(TypeError, match="Controller class cannot be instantiated."):
        Controller()


@pytest.mark.parametrize("initial_state, new_state", [(False, True), (True, False)])
def test_flag_state_persistence(initial_state: bool, new_state: bool):
    for flag in all_flags:
        Controller.set_flag(flag, initial_state)
        assert Controller.get_flag(flag) == initial_state
        Controller.set_flag(flag, new_state)
        assert Controller.get_flag(flag) == new_state


def test_multiple_flag_modifications_integrity():
    for flag in all_flags:
        Controller.set_flag(flag, True)
    for flag in all_flags:
        assert Controller.get_flag(flag), f"{flag.name} flag should be True"
    Controller.reset_flags()


def test_flag_state_consistency_across_methods():
    for flag in all_flags:
        Controller.set_flag(flag, True)
    all_flags_state = Controller.get_flags()
    for flag in all_flags:
        assert (
            Controller.get_flag(flag) == all_flags_state[flag]
        ), f"Flag state for {flag.name} should be consistent across get_flag and get_flags methods"
    Controller.reset_flags()
