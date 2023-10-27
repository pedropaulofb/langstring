"""Tests for the MultiLangString class's method get_pref_langstring."""
import pytest

from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def test_get_pref_langstring_existing() -> None:
    """Test if the correct LangString is returned for an existing preferred language."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1, preferred_lang="en")
    assert mls.get_pref_langstring() == ["Hello"], "Expected 'Hello' for the preferred language 'en'"


def test_get_pref_langstring_non_existing() -> None:
    """Test if None is returned when the preferred language doesn't exist."""
    lang_str1 = LangString("Hola", "es")
    mls = MultiLangString(lang_str1, preferred_lang="en")
    assert mls.get_pref_langstring() is None, "Expected None for the nonexistent preferred language 'en'"


def test_get_pref_langstring_multiple_entries_allow() -> None:
    """Test if the first LangString is returned when multiple are associated with the preferred language."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hi", "en")
    mls = MultiLangString(lang_str1, lang_str2, preferred_lang="en")
    assert mls.get_pref_langstring() == [
        "Hello",
        "Hi",
    ], "Expected both 'Hello' and 'Hi' for the preferred language 'en'"


def test_get_pref_langstring_with_overwrite() -> None:
    """Test behavior when the control is set to OVERWRITE and multiple LangStrings are added for
    the preferred language."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hi", "en")
    mls = MultiLangString(lang_str1, control="OVERWRITE", preferred_lang="en")
    mls.add(lang_str2)
    assert mls.get_pref_langstring() == ["Hi"], "Expected 'Hi' as the last LangString should overwrite the previous one"


def test_get_pref_langstring_with_block_error() -> None:
    """Test behavior when the control is set to BLOCK_ERROR and a duplicate LangString for the preferred language
    is added."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hi", "en")
    mls = MultiLangString(lang_str1, control="BLOCK_ERROR", preferred_lang="en")
    with pytest.raises(ValueError):
        mls.add(lang_str2)
    assert mls.get_pref_langstring() == ["Hello"], "Expected 'Hello' as the second addition should be blocked"


def test_get_pref_langstring_empty_pref_lang() -> None:
    """Test if None is returned when the preferred language is an empty string."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1, preferred_lang="")
    assert mls.get_pref_langstring() is None, "Expected None for an empty preferred language"


def test_get_pref_langstring_invalid_pref_lang() -> None:
    """Test if None is returned when the preferred language is invalid."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1, preferred_lang="invalid_language_code")
    assert mls.get_pref_langstring() is None, "Expected None for an invalid preferred language"


def test_get_pref_langstring_with_invalid_type() -> None:
    """Test behavior when the preferred language is set to a non-string type."""
    lang_str1 = LangString("Hello", "en")
    with pytest.raises(TypeError):
        MultiLangString(lang_str1, preferred_lang=123)


def test_get_pref_langstring_with_none_pref_lang() -> None:
    """Test if English string is returned when the preferred language is set to None."""
    lang_str1 = LangString("Hello", "en")
    mls = MultiLangString(lang_str1, preferred_lang=None)
    assert mls.get_pref_langstring() == ["Hello"], "Expected 'Hello' for a None preferred language defaulting to 'en'"
