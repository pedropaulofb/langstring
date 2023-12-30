import pytest

from langstring import MultiLangString
from langstring import MultiLangStringControl
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "lang, flag_state, expected_exception", [("", True, ValueError), ("en", True, None), ("", False, None)]
)
def test_validate_ensure_any_lang(lang, flag_state, expected_exception):
    """
    Test the _validate_ensure_any_lang method under different flag settings and language inputs.

    :param lang: The language code to test.
    :param flag_state: The state of the ENSURE_ANY_LANG flag.
    :param expected_exception: The expected exception, if any.
    """
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, flag_state)
    mls = MultiLangString()

    # Directly accessing the protected method for testing purposes
    if expected_exception:
        with pytest.raises(expected_exception, match="cannot receive empty string"):
            mls._validate_ensure_any_lang(lang)
    else:
        mls._validate_ensure_any_lang(lang)  # Should not raise an exception
