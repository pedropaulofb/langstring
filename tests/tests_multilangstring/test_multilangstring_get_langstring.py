"""Tests for the MultiLangString class's method get_langstring."""
import pytest

from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def test_get_langstring_existing_language() -> None:
    """Test retrieving LangStrings for an existing language tag."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hi", "en")
    mls = MultiLangString(lang_str1, lang_str2, control="ALLOW")
    result = mls.get_langstring("en")
    assert result == ["Hello", "Hi"], f"Expected ['Hello', 'Hi'] but got {result}"


def test_get_langstring_non_existing_language() -> None:
    """Test retrieving LangStrings for a non-existing language tag."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    result = mls.get_langstring("fr")
    assert result == [], f"Expected [] but got {result}"


def test_get_langstring_invalid_language() -> None:
    """Test retrieving LangStrings for an invalid language tag."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    result = mls.get_langstring("INVALID_LANG")
    assert result == [], f"Expected [] but got {result}"


def test_get_langstring_with_preferred_language() -> None:
    """Test retrieving LangStrings with preferred language."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Bonjour", "fr")
    mls = MultiLangString(lang_str1, lang_str2, preferred_lang="fr")
    result = mls.get_langstring("fr")
    assert result == ["Bonjour"], f"Expected ['Bonjour'] but got {result}"


@pytest.mark.parametrize("lang, expected", [("en", ["Hello"]), ("fr", []), ("es", ["Hola"])])
def test_get_langstring_parametrized(lang, expected):
    """Parametrized test for retrieving LangStrings for various language tags."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hola", "es")
    mls = MultiLangString(lang_str1, lang_str2)
    result = mls.get_langstring(lang)
    assert result == expected, f"Expected {expected} but got {result}"


def test_get_langstring_with_non_string_arg() -> None:
    """Test retrieving LangStrings using a non-string argument."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    with pytest.raises(TypeError):
        mls.get_langstring(123)  # Pass a number instead of a string


def test_get_langstring_with_empty_string() -> None:
    """Test retrieving LangStrings using an empty string."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    result = mls.get_langstring("")  # Pass an empty string
    assert result == [], f"Expected [] but got {result}"


def test_get_langstring_with_none_arg() -> None:
    """Test retrieving LangStrings using None as an argument."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    with pytest.raises(TypeError):
        mls.get_langstring(None)


def test_get_langstring_with_long_string_arg() -> None:
    """Test retrieving LangStrings using an unusually long string argument."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1)
    result = mls.get_langstring("a" * 1000)  # Pass a long string
    assert result == [], f"Expected [] but got {result}"
