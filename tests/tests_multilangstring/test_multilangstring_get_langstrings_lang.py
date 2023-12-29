from langstring import LangString
from langstring import MultiLangString


def test_get_langstrings_lang_with_existing_language():
    """
    Test retrieving all LangStrings for a specific language that exists in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_langstrings_lang("en")
    expected = [LangString("Hello", "en"), LangString("Hi", "en")]
    assert all(
        langstring in result for langstring in expected
    ), "get_langstrings_lang should return all LangStrings for the specified language"


def test_get_langstrings_lang_with_nonexistent_language():
    """
    Test retrieving all LangStrings for a language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_langstrings_lang("fr")
    assert result == [], "get_langstrings_lang should return an empty list for a nonexistent language"


def test_get_langstrings_lang_with_empty_multilangstring():
    """
    Test retrieving all LangStrings for any language from an empty MultiLangString.
    """
    mls = MultiLangString()
    result = mls.get_langstrings_lang("en")
    assert result == [], "get_langstrings_lang should return an empty list for an empty MultiLangString"


def test_get_langstrings_lang_with_invalid_language_type():
    """
    Test retrieving all LangStrings with an invalid language type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert not mls.get_langstrings_lang(123), "The return must be an empty list, as there is nothing to be returned."
