from langstring import MultiLangString


def test_str_for_empty_multilangstring():
    """
    Test the __str__ method for an empty MultiLangString object.
    """
    mls = MultiLangString()
    assert str(mls) == "", "The __str__ output for an empty MultiLangString should be an empty string"


def test_str_for_multilangstring_with_content():
    """
    Test the __str__ method for a MultiLangString object with content.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    expected_str = '"Hello"@en, "Bonjour"@fr'  # Adjusted to single quotes
    assert str(mls) == expected_str, "The __str__ output should match the expected format with content"


def test_str_for_multilangstring_with_multiple_entries_per_language():
    """
    Test the __str__ method for a MultiLangString object with multiple entries per language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour", "Salut"}})
    result_str = str(mls)
    expected_entries = {'"Hello"@en', '"Hi"@en', '"Bonjour"@fr', '"Salut"@fr'}
    result_entries = set(result_str.split(", "))
    assert (
        result_entries == expected_entries
    ), "The __str__ output should include all entries for each language, formatted as '\"text\"@lang'"
