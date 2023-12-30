from langstring import MultiLangString


def test_get_strings_langstring_all_with_multiple_languages():
    """
    Test retrieving all text entries across all languages in a MultiLangString with multiple languages, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_strings_langstring_all()
    expected = ['"Hello"@en', '"Hi"@en', '"Bonjour"@fr']
    assert set(result) == set(
        expected
    ), "get_strings_langstring_all should return all text entries for all languages, formatted as '\"text\"@lang'"


def test_get_strings_langstring_all_with_empty_multilangstring():
    """
    Test retrieving all text entries from an empty MultiLangString, formatted as '"text"@lang'.
    """
    mls = MultiLangString()
    result = mls.get_strings_langstring_all()
    assert result == [], "get_strings_langstring_all should return an empty list for an empty MultiLangString"


def test_get_strings_langstring_all_with_single_language():
    """
    Test retrieving all text entries from a MultiLangString with a single language, formatted as '"text"@lang'.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_strings_langstring_all()
    expected = ['"Hello"@en']
    assert result == expected, (
        "get_strings_langstring_all should return all text entries for a MultiLangString with a single language, "
        "formatted as '\"text\"@lang'"
    )
