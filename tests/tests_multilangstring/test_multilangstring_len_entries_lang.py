from langstring import MultiLangString


def test_len_entries_lang_with_existing_language():
    """
    Test len_entries_lang method for a language that exists in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    assert (
        mls.len_entries_lang("en") == 2
    ), "len_entries_lang should return the correct number of entries for an existing language"


def test_len_entries_lang_with_nonexistent_language():
    """
    Test len_entries_lang method for a language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert mls.len_entries_lang("fr") == 0, "len_entries_lang should return 0 for a nonexistent language"


def test_len_entries_lang_with_empty_multilangstring():
    """
    Test len_entries_lang method for an empty MultiLangString.
    """
    mls = MultiLangString()
    assert mls.len_entries_lang("en") == 0, "len_entries_lang should return 0 for an empty MultiLangString"


def test_len_entries_lang_with_invalid_language_type():
    """
    Test len_entries_lang method with an invalid language type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert mls.len_entries_lang(123) == 0, "len_entries_lang should return 0 for an empty MultiLangString"
