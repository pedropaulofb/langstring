import pytest

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

    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
        LangString("Hello", "invalid-lang")


def test_langstring_with_all_flags_enabled_empty_text() -> None:
    """Test LangString initialization with all flags enabled and empty text."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_TEXT enabled: LangString's 'text' field cannot"):
        LangString("", "en")


def test_langstring_with_all_flags_enabled_empty_language() -> None:
    """Test LangString initialization with all flags enabled and empty language."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
        LangString("Hello", "")


def test_langstring_with_mixed_flags() -> None:
    """Test LangString initialization with ENSURE_TEXT and ENSURE_VALID_LANG enabled, but ENSURE_ANY_LANG disabled."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, False)
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang'"):
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


def test_langstring_equality() -> None:
    """Test that two LangString instances with the same text and language are equal."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "en")
    assert lang_str1 == lang_str2, "LangString instances with the same text and language should be equal"


def test_langstring_inequality() -> None:
    """Test that LangString instances with different text or language are not equal."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "fr")
    lang_str3 = LangString("Bonjour", "en")
    assert lang_str1 != lang_str2, "LangString instances with different languages should not be equal"
    assert lang_str1 != lang_str3, "LangString instances with different text should not be equal"


def test_langstring_hash() -> None:
    """Test the hash functionality of LangString."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "en")
    assert hash(lang_str1) == hash(lang_str2), "Hash values should be the same for identical LangString instances"


def test_langstring_string_representation() -> None:
    """Test the string representation of LangString."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", None)
    assert str(lang_str1) == '"Hello"@en', "String representation with language should be correct"
    assert str(lang_str2) == '"Hello"', "String representation without language should be correct"
