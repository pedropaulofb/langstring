from langstring import MultiLangString


def test_get_strings_langstring_lang_with_existing_language():
    """
    Test retrieving all text entries for a specific language in a MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_strings_langstring_lang("en")
    expected = ['"Hello"@en', '"Hi"@en']
    assert set(result) == set(
        expected
    ), "get_strings_langstring_lang should return all text entries for the specified language, formatted as '\"text\"@lang'"


def test_get_strings_langstring_lang_with_nonexistent_language():
    """
    Test retrieving all text entries for a language that does not exist in the MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_strings_langstring_lang("fr")
    assert result == [], "get_strings_langstring_lang should return an empty list for a nonexistent language"


def test_get_strings_langstring_lang_with_empty_multilangstring():
    """
    Test retrieving all text entries for any language from an empty MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString()
    result = mls.get_strings_langstring_lang("en")
    assert result == [], "get_strings_langstring_lang should return an empty list for an empty MultiLangString"


def test_get_strings_langstring_lang_with_invalid_language_type():
    """
    Test retrieving all text entries with an invalid language type, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert not mls.get_strings_langstring_lang(123), "Should be an empty list."
