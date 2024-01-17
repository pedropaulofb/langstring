import pytest

from langstring import Controller
from langstring import GlobalFlag
from langstring import LangStringFlag
from langstring import MultiLangStringFlag
from langstring import SetLangStringFlag

all_flags = (
    list(LangStringFlag.__members__.values())
    + list(SetLangStringFlag.__members__.values())
    + list(MultiLangStringFlag.__members__.values())
    + list(GlobalFlag.__members__.values())
)


def test_get_flag_equals_get_flags():
    all_flags_dict = Controller.get_flags()
    for flag in all_flags:
        assert Controller.get_flag(flag) == all_flags_dict[flag], "get_flag should match get_flags for each flag"


@pytest.mark.parametrize("flag_class", [LangStringFlag, SetLangStringFlag, MultiLangStringFlag])
def test_reset_individual_flag_type_equals_reset_flags_except_global(flag_class):
    # Set all flags to a non-default state
    for flag in all_flags:
        Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    # Reset flags of the specific type
    Controller.reset_flag(flag_class)

    # Get the state after resetting the specific flag type
    state_after_reset_specific = Controller.get_flags()

    # Reset all flags and then set GlobalFlag back to non-default state
    Controller.reset_flags()
    for global_flag in GlobalFlag:
        Controller.set_flag(global_flag, not Controller.DEFAULT_FLAGS[global_flag])

    # Get the state after resetting all flags and setting GlobalFlag
    state_after_reset_all_except_global = Controller.get_flags()

    # Check if the states match for the specific flag type and all flags except GlobalFlag
    for flag, state in state_after_reset_specific.items():
        if isinstance(flag, flag_class):
            assert state == Controller.DEFAULT_FLAGS[flag], f"Flag {flag} should be reset to its default state"
        elif isinstance(flag, GlobalFlag):
            assert state == (
                not Controller.DEFAULT_FLAGS[flag]
            ), f"GlobalFlag {flag} should remain in the non-default state"


@pytest.mark.parametrize("flag_class", [GlobalFlag])
def test_reset_flag_global_equals_reset_flags(flag_class):
    # Set all flags to a non-default state
    for flag in all_flags:
        Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    # Reset GlobalFlag
    Controller.reset_flag(flag_class)

    # Get the state after resetting GlobalFlag
    state_after_reset_global = Controller.get_flags()

    # Reset all flags
    Controller.reset_flags()

    # Get the state after resetting all flags
    state_after_reset_all = Controller.get_flags()

    # Check if the states match for resetting GlobalFlag and resetting all flags
    assert (
        state_after_reset_global == state_after_reset_all
    ), "reset_flag(GlobalFlag) should match the state after reset_flags()"
