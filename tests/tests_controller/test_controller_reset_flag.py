import pytest

from langstring import Controller
from langstring import GlobalFlag
from langstring import LangStringFlag
from langstring import MultiLangStringFlag
from langstring import SetLangStringFlag

flag_classes = [GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]

all_flags = (
    list(LangStringFlag.__members__.values())
    + list(SetLangStringFlag.__members__.values())
    + list(MultiLangStringFlag.__members__.values())
    + list(GlobalFlag.__members__.values())
)


@pytest.mark.parametrize("flag_class", flag_classes)
def test_reset_specific_flag_type_to_default(flag_class):
    # Set all flags to a non-default state for testing
    for flag in all_flags:
        Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    # Reset flags of the specific type
    Controller.reset_flag(flag_class)

    # Assert that flags of the specific type are reset to their default state
    for flag in flag_class:
        assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag]

    # If GlobalFlag is reset, all flags should be reset to default
    if flag_class == GlobalFlag:
        for flag in all_flags:
            assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag]
    else:
        # Assert that flags of other types are not affected (remain in the non-default state)
        for other_class in flag_classes:
            if other_class != flag_class:
                for flag in other_class:
                    assert Controller.get_flag(flag) == (not Controller.DEFAULT_FLAGS[flag])


@pytest.mark.parametrize("flag_class", flag_classes)
def test_reset_flag_type_idempotence(flag_class):
    """
    Test the idempotence of the reset_flag method for a specific flag type.
    """
    # Reset flags of the specific type twice
    Controller.reset_flag(flag_class)
    Controller.reset_flag(flag_class)

    # Assert that flags remain in their default state after multiple resets
    for flag in flag_class:
        assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag], f"{flag} should remain in default state"


@pytest.mark.parametrize("invalid_flag_class", [123, "InvalidType", 4.5, None, []])
def test_reset_flag_invalid_type(invalid_flag_class):
    """
    Test resetting flags with an invalid type.
    """
    with pytest.raises(TypeError, match="Invalid flag type"):
        Controller.reset_flag(invalid_flag_class)
