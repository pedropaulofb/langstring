import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("en", True),  # valid language code
        ("fr", True),  # another valid language code
        ("", False),  # empty string, invalid language code
        (None, False),  # None should not be accepted
    ],
)
def test_validate_ensure_any_lang(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_any_lang method for various language codes."""
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    if is_valid:
        try:
            LangString("Test", lang)
        except ValueError as e:
            pytest.fail(f"Unexpected ValueError for language code '{lang}': {e}")
    else:
        with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


def test_langstring_init_with_ensure_any_lang_flag_disabled() -> None:
    """Test LangString initialization with various language tags with ENSURE_ANY_LANG flag disabled."""
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, False)
    # Test with an empty string as language code
    lang_str = LangString("Hello", "")
    assert lang_str.lang == "", "LangString should accept empty language tag when ENSURE_ANY_LANG is disabled"


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        (" en ", True),  # leading and trailing whitespace
        ("fr ", True),  # trailing whitespace
    ],
)
def test_validate_ensure_any_lang_whitespace(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_any_lang method for language codes with whitespace."""
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("En", True),  # mixed case, valid if language code itself is valid
        ("eN", True),  # mixed case, valid if language code itself is valid
    ],
)
def test_validate_ensure_any_lang_mixed_case(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_any_lang method for mixed case language codes."""
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang, is_valid",
    [
        ("en-US", True),  # valid extended language tag
        ("fr-CA", True),  # another valid extended language tag
    ],
)
def test_validate_ensure_any_lang_extended(lang: str, is_valid: bool) -> None:
    """Test the _validate_ensure_any_lang method for extended language tags."""
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    if is_valid:
        LangString("Test", lang)
    else:
        with pytest.raises(ValueError, match="ENSURE_ANY_LANG enabled: LangString's 'lang' field cannot"):
            LangString("Test", lang)


@pytest.mark.parametrize(
    "lang",
    [
        "123",  # numeric language code
        "en-@",  # special character in language code
        "fr#CA",  # another example with special character
        "!",
        " ",
        "\n",
    ],
)
def test_validate_ensure_any_lang_numeric_and_special_chars(lang: str) -> None:
    """Test the _validate_ensure_any_lang method with invalid language codes when ENSURE_ANY_LANG is enabled.

    :param lang: The language code to test.
    """
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    assert LangString("Test", lang), "ENSURE_ANY_LANG should accept every string."
