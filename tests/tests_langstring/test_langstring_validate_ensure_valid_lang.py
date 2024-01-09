import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


def test_langstring_init_invalid_lang_without_ensure_valid_lang_flag() -> None:
    """Test LangString initialization with an invalid language tag but without ENSURE_VALID_LANG flag."""
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, False)
    lang_str = LangString("Hello", "invalid-lang")
    assert (
        lang_str.lang == "invalid-lang"
    ), "LangString should accept invalid language tag when ENSURE_VALID_LANG is not set"


# Test cases for _validate_ensure_valid_lang method of LangString class


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("en", True),  # valid language code
        ("fr", True),  # another valid language code
        ("eng", True),  # valid ISO 639-3 code
        ("xyz", False),  # invalid language code
        ("123", False),  # numeric string, invalid language code
        ("", False),  # empty string, invalid language code
        (None, False),  # None should not trigger validation
    ],
)
def test_validate_ensure_valid_lang(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_valid_lang method for various language codes.

    :param lang: The language code to test.
    :param is_valid: Expected validity of the language code.
    """
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    if is_valid:
        # No exception expected for valid language codes
        try:
            LangString("Test", lang)
        except ValueError as e:
            pytest.fail(f"Unexpected ValueError for valid language code '{lang}': {e}")
    else:
        # Expect ValueError for invalid language codes
        with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


def test_langstring_init_invalid_lang_with_ensure_valid_lang_flag_disabled() -> None:
    """Test LangString initialization with an invalid language tag with ENSURE_VALID_LANG flag disabled."""
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, False)
    lang_str = LangString("Hello", "invalid-lang")
    assert (
        lang_str.lang == "invalid-lang"
    ), "LangString should accept invalid language tag when ENSURE_VALID_LANG is disabled"


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("En", True),  # mixed case, valid
        ("eN", True),  # mixed case, valid
    ],
)
def test_validate_ensure_valid_lang_mixed_case(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_valid_lang method for mixed case language codes."""
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("en-US", True),  # valid extended language tag
        ("fr-CA", True),  # another valid extended language tag
    ],
)
def test_validate_ensure_valid_lang_extended(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_valid_lang method for extended language tags."""
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        (" en ", False),  # leading and trailing whitespace
        ("fr ", False),  # trailing whitespace
    ],
)
def test_validate_ensure_valid_lang_whitespace(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_valid_lang method for language codes with whitespace."""
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("en", True),  # valid language code
        ("invalid-lang", False),  # invalid language code
    ],
)
def test_langstring_init_empty_text(lang: str, is_valid: bool) -> None:
    """Test LangString initialization with empty text and various language codes."""
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, False)
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    if is_valid:
        assert LangString("", lang), "Should be possible to create when both flags are enabled."
    else:
        with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
            LangString("", lang)


@pytest.mark.parametrize(
    "lang",
    [
        "abc-",  # note that "abc" is valid
        "abc ",
        " abc",
        "123",  # numeric string, invalid language code
        "en-@",  # special character in language code
    ],
)
def test_validate_ensure_valid_lang_non_standard_codes(lang: str) -> None:
    """
    Test the _validate_ensure_valid_lang method with non-standard language codes when ENSURE_VALID_LANG is enabled.

    :param lang: The language code to test.
    :raises AssertionError: If LangString accepts a non-standard language code when ENSURE_VALID_LANG is enabled.
    """
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
        LangString("Test", lang)


@pytest.mark.parametrize(
    "lang",
    [None, "undefined"],
)
def test_validate_ensure_valid_lang_null_or_undefined(lang) -> None:
    """
    Test the _validate_ensure_valid_lang method with null or undefined language codes when ENSURE_VALID_LANG is enabled.

    :param lang: The language code to test (None or "undefined").
    :raises AssertionError: If LangString accepts null or undefined language codes when ENSURE_VALID_LANG is enabled.
    """
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    with pytest.raises(ValueError, match="ENSURE_VALID_LANG enabled: LangString's 'lang' field cannot"):
        LangString("Test", lang)
