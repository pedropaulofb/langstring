import pytest

from langstring import Controller


def test_multilangstringcontrol_instantiation_prohibited():
    """
    Test if attempting to instantiate Controller raises a TypeError.
    """
    with pytest.raises(TypeError, match="class cannot be instantiated"):
        Controller()


def test_multilangstringcontrol_initial_flag_states():
    """
    Test if the initial flag states in Controller are set to their default values.
    """
    expected_default_states = {
        Controller._get_flags_type().ENSURE_TEXT: True,
        Controller._get_flags_type().ENSURE_VALID_LANG: False,
    }
    assert (
        Controller.get_flags() == expected_default_states
    ), "Initial flag states in Controller should be set to their default values"
