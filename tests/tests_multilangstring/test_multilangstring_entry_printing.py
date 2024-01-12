from langstring import Controller
from langstring import MultiLangString
from langstring import MultiLangStringFlag


def test_single_entry_with_lang_tag():
    """
    Test various methods for a MultiLangString object with a single entry having a language tag.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})

    # Test __str__ method
    assert str(mls) == '"Hello"@en', "The __str__ output should match the single entry with language tag"

    # Test get_strings_all method
    assert mls.get_strings_all() == ["Hello"], "get_strings_all should return the single text entry"

    # Test get_strings_lang method
    assert mls.get_strings_lang("en") == [
        "Hello"
    ], "get_strings_lang should return the single text entry for the specified language"

    # Test get_strings_langstring_all method
    assert mls.get_strings_langstring_all() == [
        '"Hello"@en'
    ], "get_strings_langstring_all should return the single text entry formatted with language tag"


def test_single_entry_without_lang_tag():
    """
    Test various methods for a MultiLangString object with a single entry without a language tag.
    """
    mls = MultiLangString(mls_dict={"": {"Hello"}})

    # Test __str__ method
    assert str(mls) == "Hello", "The __str__ output should match the single entry without language tag"

    # Test get_strings_all method
    assert mls.get_strings_all() == ["Hello"], "get_strings_all should return the single text entry"

    # Test get_strings_lang method for empty language
    assert mls.get_strings_lang("") == [
        "Hello"
    ], "get_strings_lang should return the single text entry for empty language"


def test_multiple_entries_with_lang_tag():
    """
    Test various methods for a MultiLangString object with multiple entries, all having language tags.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})

    # Test __str__ method
    result_str = str(mls)
    expected_entries = {'"Hello"@en', '"Hi"@en', '"Bonjour"@fr'}
    result_entries = set(result_str.split(", "))
    assert result_entries == expected_entries, "The __str__ output should include all entries with language tags"

    # Test get_strings_all method
    assert set(mls.get_strings_all()) == {"Hello", "Hi", "Bonjour"}, "get_strings_all should return all text entries"


def test_multiple_entries_without_lang_tag():
    """
    Test various methods for a MultiLangString object with multiple entries, none having language tags.
    """
    mls = MultiLangString(mls_dict={"": {"Hello", "Hi"}})
    result = set(str(mls).split(", "))
    expected = {"Hello", "Hi"}
    assert result == expected, "The __str__ output should include all entries without language tags"


def test_mixed_entries_with_and_without_lang_tags():
    """
    Test various methods for a MultiLangString object with mixed entries (some with and some without language tags).
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "": {"Hi"}})

    # Test __str__ method
    result_str = str(mls)
    expected_entries = {'"Hello"@en', "Hi"}
    result_entries = set(result_str.split(", "))
    assert (
        result_entries == expected_entries
    ), "The __str__ output should include mixed entries with and without language tags"

    # Test get_strings_all method
    assert set(mls.get_strings_all()) == {"Hello", "Hi"}, "get_strings_all should return all text entries"


def test_empty_string_entries():
    """
    Test the behavior of MultiLangString with empty string entries.
    """
    Controller.set_flag(MultiLangStringFlag.DEFINED_TEXT, False)
    mls = MultiLangString(mls_dict={"en": {""}, "": {""}})
    assert str(mls) == '""@en, ', "Empty strings should be correctly represented"


def test_duplicate_entries():
    """
    Test the behavior of MultiLangString with duplicate entries.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hello"}})
    assert str(mls) == '"Hello"@en', "Duplicate entries should be handled (likely ignored)"


def test_special_characters_in_entries():
    """
    Test the behavior of MultiLangString with special characters in entries.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello\nWorld", "Hi\tthere"}})
    result = set(str(mls).split(", "))
    expected = {'"Hello\nWorld"@en', '"Hi\tthere"@en'}
    assert result == expected, "Special characters should be correctly represented"
