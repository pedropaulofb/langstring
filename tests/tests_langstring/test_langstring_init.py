import pytest

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


def test_initialization() -> None:
    """Test the initialization of a LangString object without specifying a language."""
    ls = LangString("hello")
    assert ls.text == "hello", f'Expected text to be "hello", but got {ls.text}'
    assert isinstance(ls.text, str), f"Expected text type to be str, but got {type(ls.text).__name__}"
    assert ls.lang is None, f"Expected lang to be None, but got {ls.lang}"


def test_language_initialization() -> None:
    """Test the initialization of a LangString object with a specified language."""
    ls = LangString("hola", "es")
    assert ls.text == "hola", f'Expected text to be "hola", but got {ls.text}'
    assert isinstance(ls.text, str), f"Expected text type to be str, but got {type(ls.text).__name__}"
    assert ls.lang == "es", f'Expected lang to be "es", but got {ls.lang}'
    assert isinstance(ls.lang, str), f"Expected lang type to be str, but got {type(ls.lang).__name__}"


def test_empty_text_lang_initialization() -> None:
    """Test the initialization of a LangString object with empty text and no specified language."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    ls = LangString("")
    assert ls.text == "", f"Expected text to be an empty string, but got {ls.text}"
    assert ls.lang is None, f"Expected lang to be None, but got {ls.lang}"


def test_empty_language_initialization() -> None:
    """Test the initialization of a LangString object with empty text and a specified language."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    ls = LangString("", "es")
    assert ls.text == "", f"Expected text to be an empty string, but got {ls.text}"
    assert ls.lang == "es", f'Expected lang to be "es", but got {ls.lang}'


def test_wrong_type_initialization() -> None:
    """Test initialization with wrong types."""
    with pytest.raises(TypeError):
        LangString(123)


def test_wrong_type_language_initialization() -> None:
    """Test language initialization with wrong types."""
    with pytest.raises(TypeError):
        LangString("hola", 123)


def test_whitespace_and_special_characters() -> None:
    ls = LangString(" hello world! @#$%^&*()_+ ")
    assert ls.text == " hello world! @#$%^&*()_+ ", f"Unexpected text: {ls.text}"


def test_very_long_string() -> None:
    long_string = "a" * 10000  # 10,000 characters
    ls = LangString(long_string)
    assert ls.text == long_string, f"Unexpected text: {ls.text}"
    assert ls.to_string() == f"{long_string}", f"Unexpected string representation: {ls.to_string()}"


def test_no_warning_on_valid_language_tag() -> None:
    """Test that no warning is generated when a valid language tag is used."""
    with pytest.warns(None) as record:
        LangString("Hello", "en")

    # Confirming that no warnings were captured
    assert len(record) == 0


def test_no_warning_on_no_language_tag() -> None:
    """Test that no warning is generated when no language tag is provided."""
    with pytest.warns(None) as record:
        LangString("Hello")

    # Confirming that no warnings were captured
    assert len(record) == 0


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


def test_empty_text_and_language_with_flags_enabled() -> None:
    """
    Test the initialization of a LangString object with empty text and language when relevant flags are enabled.

    :raises AssertionError: If LangString initialization does not raise an exception as expected.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    with pytest.raises(ValueError, match="ENSURE_TEXT enabled: LangString's 'text' field cannot"):
        LangString("", "")


def test_invalid_language_with_ensure_valid_lang_disabled() -> None:
    """
    Test the initialization of a LangString object with an invalid language when ENSURE_VALID_LANG is disabled.

    :raises AssertionError: If LangString initialization does not behave as expected.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, False)
    ls = LangString("Hello", "invalid-lang")
    assert ls.lang == "invalid-lang", "LangString should allow invalid language when ENSURE_VALID_LANG is disabled"


def test_nonempty_text_no_language_with_ensure_any_lang_enabled() -> None:
    """
    Test the initialization of a LangString object with non-empty text and no language when ENSURE_ANY_LANG is enabled.

    :raises AssertionError: If LangString initialization does not raise an exception as expected.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
        LangString("Hello")
