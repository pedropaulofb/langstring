from langstring import Controller
from langstring import MultiLangStringFlag


def test_reset_flags_resets_all_flags_to_default():
    """
    Test if the reset_flags method resets all flags to their default values.
    """
    # Change the state of a flag to ensure it's not in its default state
    Controller.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, True)

    # Reset flags to default
    Controller.reset_flags_all()
    flags_after_reset = Controller.get_flags()

    # Define the expected default states for all flags
    expected_default_states = {
        MultiLangStringFlag.ENSURE_TEXT: True,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
    }

    assert flags_after_reset == expected_default_states, "reset_flags should reset all flags to their default values"


def test_reset_flags_effect_persists_after_multiple_set_flag_calls():
    """
    Test if the effect of reset_flags persists after multiple calls to set_flag.
    """
    # Change the state of flags multiple times
    Controller.set_flag(MultiLangStringFlag.ENSURE_TEXT, False)
    Controller.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, True)

    # Reset flags to default
    Controller.reset_flags_all()
    flags_after_reset = Controller.get_flags()

    # Define the expected default states for all flags
    expected_default_states = {
        MultiLangStringFlag.ENSURE_TEXT: True,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
    }

    assert (
        flags_after_reset == expected_default_states
    ), "reset_flags should still reset all flags to default values after multiple set_flag calls"
