from langstring import MultiLangString


def test_len_entries_all_empty_multilangstring():
    """
    Test len_entries_all method for an empty MultiLangString object.
    """
    mls = MultiLangString()
    assert mls.len_entries_all() == 0, "len_entries_all should return 0 for an empty MultiLangString"


def test_len_entries_all_with_single_language():
    """
    Test len_entries_all method for a MultiLangString object with entries in a single language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}})
    assert mls.len_entries_all() == 2, "len_entries_all should return the correct total number of entries"


def test_len_entries_all_with_multiple_languages():
    """
    Test len_entries_all method for a MultiLangString object with entries in multiple languages.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour", "Salut"}})
    assert (
        mls.len_entries_all() == 3
    ), "len_entries_all should return the correct total number of entries for multiple languages"
