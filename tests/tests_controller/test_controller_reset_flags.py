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
def test_reset_flags_to_default(flag) -> None:
    # Set the flag to a non-default state for testing
    Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    # Reset all flags
    Controller.reset_flags()

    # Assert that the flag is reset to its default state
    assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag]


@pytest.mark.parametrize("flag", all_flags)
def test_reset_flags_idempotence(flag) -> None:
    """
    Test the idempotence of the reset_flags method.
    """
    Controller.reset_flags()
    Controller.reset_flags()
    assert (
        Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag]
    ), "Flag should remain in default state after multiple resets"


@pytest.mark.parametrize("flag", all_flags)
def test_reset_flags_effectiveness(flag) -> None:
    """
    Test the effectiveness of the reset_flags method in resetting all flags to False.
    """
    # Invert the value of the flag
    Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    Controller.reset_flags()

    # Check if the flag is reset to default
    assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag], "Flag should reset to default state"


@pytest.mark.parametrize("flag", all_flags)
def test_reset_flags_changes_state(flag) -> None:
    """
    Test that the reset_flags method changes the state of flags from a modified state back to the default state.
    """
    # Modify the state of the flag
    Controller.set_flag(flag, not Controller.DEFAULT_FLAGS[flag])

    # Reset flags
    Controller.reset_flags()

    # Check if the flag is reset to default
    assert Controller.get_flag(flag) == Controller.DEFAULT_FLAGS[flag], "Flag should reset to default state"
