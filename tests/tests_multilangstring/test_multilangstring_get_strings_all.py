from langstring import MultiLangString


def test_get_strings_all_with_multiple_languages():
    """
    Test retrieving all text entries across all languages in a MultiLangString with multiple languages.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = mls.get_strings_all()
    expected = ["Hello", "Hi", "Bonjour"]
    assert all(text in result for text in expected), "get_strings_all should return all text entries for all languages"


def test_get_strings_all_with_empty_multilangstring():
    """
    Test retrieving all text entries from an empty MultiLangString.
    """
    mls = MultiLangString()
    result = mls.get_strings_all()
    assert result == [], "get_strings_all should return an empty list for an empty MultiLangString"


def test_get_strings_all_with_single_language():
    """
    Test retrieving all text entries from a MultiLangString with a single language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_strings_all()
    expected = ["Hello"]
    assert (
        result == expected
    ), "get_strings_all should return all text entries for a MultiLangString with a single language"
