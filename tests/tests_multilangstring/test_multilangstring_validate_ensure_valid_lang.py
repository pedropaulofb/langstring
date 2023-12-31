import pytest

from langstring import MultiLangString
from langstring import MultiLangStringControl
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "lang, flag_state, is_valid_lang, expected_exception",
    [
        ("en", True, True, None),
        ("invalid-lang", True, False, ValueError),
        ("invalid-lang", False, False, None),
        ("en", False, True, None),
    ],
)
def test_validate_ensure_valid_lang(lang, flag_state, is_valid_lang, expected_exception):
    """
    Test the _validate_ensure_valid_lang method under different flag settings and language inputs.

    :param lang: The language code to test.
    :param flag_state: The state of the ENSURE_VALID_LANG flag.
    :param is_valid_lang: Indicates if the language code is valid.
    :param expected_exception: The expected exception, if any.
    """
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, flag_state)
    mls = MultiLangString()

    # Mocking the tag_is_valid function based on is_valid_lang
    mls.tag_is_valid = lambda _: is_valid_lang

    # Directly accessing the protected method for testing purposes
    if expected_exception:
        with pytest.raises(expected_exception, match="cannot be invalid"):
            mls._validate_ensure_valid_lang(lang)
    else:
        mls._validate_ensure_valid_lang(lang)  # Should not raise an exception
