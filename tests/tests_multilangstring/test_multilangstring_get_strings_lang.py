from langstring import MultiLangString


def test_get_strings_lang_with_existing_language():
    """
    Test retrieving all text entries for a specific language that exists in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_strings_lang("en")
    expected = ["Hello", "Hi"]
    assert set(result) == set(expected), "get_strings_lang should return all text entries for the specified language"


def test_get_strings_lang_with_nonexistent_language():
    """
    Test retrieving all text entries for a language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_strings_lang("fr")
    assert result == [], "get_strings_lang should return an empty list for a nonexistent language"


def test_get_strings_lang_with_empty_multilangstring():
    """
    Test retrieving all text entries for any language from an empty MultiLangString.
    """
    mls = MultiLangString()
    result = mls.get_strings_lang("en")
    assert result == [], "get_strings_lang should return an empty list for an empty MultiLangString"


def test_get_strings_lang_with_invalid_language_type():
    """
    Test retrieving all text entries with an invalid language type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert not mls.get_strings_lang(123), "Should return empty list."
