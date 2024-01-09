from langstring import Controller
from langstring import MultiLangStringFlag


def test_get_flags_returns_current_flag_states():
    """
    Test if the get_flags method returns a dictionary with the current states of all flags.
    """
    expected_flags = {
        MultiLangStringFlag.ENSURE_TEXT: True,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
    }
    assert Controller.get_flags() == expected_flags, "get_flags should return the correct initial states for all flags"


def test_get_flags_reflects_updated_flag_states():
    """
    Test if the get_flags method reflects updated states after using set_flag method.
    """
    Controller.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, True)
    updated_flags = Controller.get_flags()
    assert (
        updated_flags[MultiLangStringFlag.ENSURE_ANY_LANG] is True
    ), "get_flags should reflect updated state for ENSURE_ANY_LANG flag"


def test_get_flags_returns_copy_of_flag_states():
    """
    Test if the get_flags method returns a copy of the flag states, ensuring original flags are not modified.
    """
    original_flags = Controller.get_flags()
    flags_copy = Controller.get_flags()
    flags_copy[MultiLangStringFlag.ENSURE_TEXT] = False
    assert (
        Controller.get_flags() == original_flags
    ), "Modifying the dictionary returned by get_flags should not affect the original flag states"
