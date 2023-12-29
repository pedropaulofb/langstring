from langstring import LangString
from langstring import MultiLangString


def test_get_langstrings_all_with_multiple_languages():
    """
    Test retrieving all LangStrings from a MultiLangString with multiple languages.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_langstrings_all()
    expected = [LangString("Hello", "en"), LangString("Hi", "en"), LangString("Bonjour", "fr")]
    assert all(
        langstring in result for langstring in expected
    ), "get_langstrings_all should return all LangStrings for all languages"


def test_get_langstrings_all_with_empty_multilangstring():
    """
    Test retrieving all LangStrings from an empty MultiLangString.
    """
    mls = MultiLangString()
    result = mls.get_langstrings_all()
    assert result == [], "get_langstrings_all should return an empty list for an empty MultiLangString"


def test_get_langstrings_all_with_single_language():
    """
    Test retrieving all LangStrings from a MultiLangString with a single language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_langstrings_all()
    expected = [LangString("Hello", "en")]
    assert (
        result == expected
    ), "get_langstrings_all should return all LangStrings for a MultiLangString with a single language"
