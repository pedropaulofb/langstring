import pytest

from langstring import LangString
from langstring import MultiLangString


def test_get_langstrings_pref_lang_with_existing_language():
    """
    Test retrieving all LangStrings for the preferred language that exists in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}}, pref_lang="en")
    result = mls.get_langstrings_pref_lang()
    expected = [LangString("Hello", "en"), LangString("Hi", "en")]
    assert all(
        langstring in result for langstring in expected
    ), "get_langstrings_pref_lang should return all LangStrings for the preferred language"


def test_get_langstrings_pref_lang_with_nonexistent_language():
    """
    Test retrieving all LangStrings for a preferred language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}}, pref_lang="fr")
    result = mls.get_langstrings_pref_lang()
    assert result == [], "get_langstrings_pref_lang should return an empty list for a nonexistent preferred language"


def test_get_langstrings_pref_lang_with_empty_multilangstring():
    """
    Test retrieving all LangStrings for the preferred language from an empty MultiLangString.
    """
    mls = MultiLangString(pref_lang="en")
    result = mls.get_langstrings_pref_lang()
    assert result == [], "get_langstrings_pref_lang should return an empty list for an empty MultiLangString"


def test_get_langstrings_pref_lang_with_invalid_pref_lang_type():
    """
    Test retrieving all LangStrings with an invalid preferred language type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(TypeError, match="Invalid pref_lang type"):
        mls.preferred_lang = 123
        mls.get_langstrings_pref_lang()
