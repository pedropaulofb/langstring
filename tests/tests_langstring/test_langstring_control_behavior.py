from unittest.mock import patch

import pytest
from loguru import logger

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


# Test cases for LangString initialization with various flag settings
@pytest.mark.parametrize(
    "text, lang, ensure_text, ensure_any_lang, ensure_valid_lang, expected_exception",
    [
        ("Hello", "en", False, False, False, None),
        ("", "en", True, False, False, ValueError),
        ("Hello", "", False, True, False, ValueError),
        ("Hello", "invalid-lang", False, False, True, ValueError),
        ("", "", True, True, False, ValueError),
    ],
)
def test_langstring_init_with_flags(text, lang, ensure_text, ensure_any_lang, ensure_valid_lang, expected_exception):
    """Test LangString initialization with various flag settings.

    :param text: The text to initialize the LangString with.
    :param lang: The language tag to initialize the LangString with.
    :param ensure_text: The state of the ENSURE_TEXT flag.
    :param ensure_any_lang: The state of the ENSURE_ANY_LANG flag.
    :param ensure_valid_lang: The state of the ENSURE_VALID_LANG flag.
    :param expected_exception: The expected exception type, if any.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, ensure_text)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, ensure_any_lang)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, ensure_valid_lang)

    if expected_exception:
        with pytest.raises(expected_exception):
            LangString(text, lang)
    else:
        lang_str = LangString(text, lang)
        assert lang_str.text == text and lang_str.lang == lang


# Test for VERBOSE_MODE flag affecting warnings
def test_verbose_mode_warnings():
    """Test that enabling VERBOSE_MODE flag triggers warnings in LangString."""
    LangStringControl.set_flag(LangStringFlag.VERBOSE_MODE, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

    with patch.object(logger, "warning") as mock_logger:
        with pytest.raises(ValueError):
            LangString("")

        mock_logger.assert_any_call("Langstring's 'text' field received empty string.")
