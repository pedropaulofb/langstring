from langstring import MultiLangString


def test_len_langs_empty_multilangstring():
    """
    Test len_langs method for an empty MultiLangString object.
    """
    mls = MultiLangString()
    assert mls.len_langs() == 0, "len_langs should return 0 for an empty MultiLangString"


def test_len_langs_with_single_language():
    """
    Test len_langs method for a MultiLangString object with entries in a single language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert mls.len_langs() == 1, "len_langs should return the correct number of languages for a single language"


def test_len_langs_with_multiple_languages():
    """
    Test len_langs method for a MultiLangString object with entries in multiple languages.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}, "es": {"Hola"}})
    assert mls.len_langs() == 3, "len_langs should return the correct number of languages for multiple languages"
