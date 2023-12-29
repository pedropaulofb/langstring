import pytest

from langstring import MultiLangStringControl


def test_multilangstringcontrol_instantiation_prohibited():
    """
    Test if attempting to instantiate MultiLangStringControl raises a TypeError.
    """
    with pytest.raises(TypeError, match="class cannot be instantiated"):
        MultiLangStringControl()


def test_multilangstringcontrol_initial_flag_states():
    """
    Test if the initial flag states in MultiLangStringControl are set to their default values.
    """
    expected_default_states = {
        MultiLangStringControl._get_flags_type().ENSURE_TEXT: True,
        MultiLangStringControl._get_flags_type().ENSURE_ANY_LANG: False,
        MultiLangStringControl._get_flags_type().ENSURE_VALID_LANG: False,
    }
    assert (
        MultiLangStringControl.get_flags() == expected_default_states
    ), "Initial flag states in MultiLangStringControl should be set to their default values"
