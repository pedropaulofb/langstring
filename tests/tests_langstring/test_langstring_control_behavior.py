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
def test_langstring_init_with_flags(
    text, lang, ensure_text, ensure_any_lang, ensure_valid_lang, expected_exception
) -> None:
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
def test_verbose_mode_warnings() -> None:
    """Test that enabling VERBOSE_MODE flag triggers warnings in LangString."""
    LangStringControl.set_flag(LangStringFlag.VERBOSE_MODE, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

    with patch.object(logger, "warning") as mock_logger:
        with pytest.raises(ValueError):
            LangString("")

        mock_logger.assert_any_call("Langstring's 'text' field received empty string.")


def test_langstring_with_all_flags_enabled_valid_inputs() -> None:
    """Test LangString initialization with all flags enabled and valid inputs."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    assert LangString("Hello", "en")


def test_langstring_with_all_flags_enabled_invalid_language() -> None:
    """Test LangString initialization with all flags enabled and invalid language."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: Langstring's 'lang' field cannot"):
        LangString("Hello", "invalid-lang")


def test_langstring_with_all_flags_enabled_empty_text() -> None:
    """Test LangString initialization with all flags enabled and empty text."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_TEXT enabled: Langstring's 'text' field cannot"):
        LangString("", "en")


def test_langstring_with_all_flags_enabled_empty_language() -> None:
    """Test LangString initialization with all flags enabled and empty language."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: Langstring's 'lang' field cannot"):
        LangString("Hello", "")


def test_langstring_with_mixed_flags() -> None:
    """Test LangString initialization with ENSURE_TEXT and ENSURE_VALID_LANG enabled, but ENSURE_ANY_LANG disabled."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, False)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: Langstring's 'lang'"):
        LangString("Hello", "invalid-lang")


@pytest.mark.parametrize(
    "text, lang",
    [
        ("こんにちは", "ja"),  # Japanese characters
        ("Привет", "ru"),  # Cyrillic characters
        ("你好", "zh"),  # Chinese characters
        ("안녕하세요", "ko"),  # Korean characters
        ("مرحبا", "ar"),  # Arabic characters
    ],
)
def test_langstring_with_special_characters(text, lang) -> None:
    """Test LangString initialization with various special character sets."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    lang_str = LangString(text, lang)
    assert (
        lang_str.text == text and lang_str.lang == lang
    ), "LangString should correctly handle text with special characters"


def test_langstring_with_long_string_input() -> None:
    """Test LangString initialization with a very long string input."""
    long_text = "a" * 10000  # 10,000 characters long
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    lang_str = LangString(long_text, "en")
    assert lang_str.text == long_text, "LangString should correctly handle very long text inputs"
