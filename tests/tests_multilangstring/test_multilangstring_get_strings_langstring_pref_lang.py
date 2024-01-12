import pytest

from langstring import MultiLangString


def test_get_strings_langstring_pref_lang_with_existing_language():
    """
    Test retrieving all text entries for the preferred language in a MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}}, pref_lang="en")
    result = mls.get_strings_langstring_pref_lang()
    expected = ['"Hello"@en', '"Hi"@en']
    assert set(result) == set(
        expected
    ), "get_strings_langstring_pref_lang should return all text entries for the preferred language, formatted as '\"text\"@lang'"


def test_get_strings_langstring_pref_lang_with_nonexistent_language():
    """
    Test retrieving all text entries for a preferred language that does not exist in the MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}}, pref_lang="fr")
    result = mls.get_strings_langstring_pref_lang()
    assert (
        result == []
    ), "get_strings_langstring_pref_lang should return an empty list for a nonexistent preferred language"


def test_get_strings_langstring_pref_lang_with_empty_multilangstring():
    """
    Test retrieving all text entries for the preferred language from an empty MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString(pref_lang="en")
    result = mls.get_strings_langstring_pref_lang()
    assert result == [], "get_strings_langstring_pref_lang should return an empty list for an empty MultiLangString"


def test_get_strings_langstring_pref_lang_with_invalid_pref_lang_type():
    """
    Test retrieving all text entries with an invalid preferred language type, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(TypeError, match="Invalid pref_lang type"):
        mls.pref_lang = 123
        mls.get_strings_langstring_pref_lang()
