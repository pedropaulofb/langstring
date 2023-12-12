from unittest.mock import patch

import pytest
from loguru import logger

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags():
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
    yield


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


# Test LangString initialization with invalid language tag but without ENSURE_VALID_LANG flag
def test_langstring_init_invalid_lang_without_ensure_valid_lang_flag():
    """Test LangString initialization with an invalid language tag but without ENSURE_VALID_LANG flag."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, False)
    lang_str = LangString("Hello", "invalid-lang")
    assert (
        lang_str.lang == "invalid-lang"
    ), "LangString should accept invalid language tag when ENSURE_VALID_LANG is not set"


# Test LangString equality and hashing
@pytest.mark.parametrize(
    "text, lang, other_text, other_lang, are_equal",
    [
        ("Hello", "en", "Hello", "en", True),
        ("Hello", "en", "Hello", None, False),
        ("Hello", "en", "Hi", "en", False),
        ("Hello", None, "Hello", None, True),
    ],
)
def test_langstring_equality_and_hashing(text, lang, other_text, other_lang, are_equal):
    """Test LangString equality and hashing.

    :param text: Text for the first LangString.
    :param lang: Language tag for the first LangString.
    :param other_text: Text for the second LangString.
    :param other_lang: Language tag for the second LangString.
    :param are_equal: Expected equality result.
    """
    lang_str1 = LangString(text, lang)
    lang_str2 = LangString(other_text, other_lang)
    assert (lang_str1 == lang_str2) is are_equal, "LangString equality check failed"
    if are_equal:
        assert hash(lang_str1) == hash(lang_str2), "Equal LangStrings should have the same hash"


# Test LangString string representation
@pytest.mark.parametrize(
    "text, lang, expected_str",
    [
        ("Hello", "en", '"Hello"@en'),
        ("Hello", None, '"Hello"'),
        ("", "en", '""@en'),
        ("", None, '""'),
    ],
)
def test_langstring_string_representation(text, lang, expected_str):
    """Test LangString string representation.

    :param text: Text for the LangString.
    :param lang: Language tag for the LangString.
    :param expected_str: Expected string representation.
    """
    lang_str = LangString(text, lang)
    assert str(lang_str) == expected_str, "LangString string representation is incorrect"
    assert lang_str.to_string() == expected_str, "LangString to_string method returned incorrect representation"
