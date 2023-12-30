from langstring import MultiLangString


def test_repr_for_empty_multilangstring():
    """
    Test the __repr__ method for an empty MultiLangString object.
    """
    mls = MultiLangString()
    expected_repr = "MultiLangString({}, pref_lang='en')"
    assert (
        repr(mls) == expected_repr
    ), "The __repr__ output for an empty MultiLangString should match the expected format"


def test_repr_for_multilangstring_with_content():
    """
    Test the __repr__ method for a MultiLangString object with content.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}}, pref_lang="fr")
    expected_repr = "MultiLangString({'en': {'Hello'}, 'fr': {'Bonjour'}}, pref_lang='fr')"
    assert (
        repr(mls) == expected_repr
    ), "The __repr__ output should match the expected format with content and preferred language"


def test_repr_for_multilangstring_with_different_pref_lang():
    """
    Test the __repr__ method for a MultiLangString object with a different preferred language.
    """
    mls = MultiLangString(pref_lang="fr")
    expected_repr = "MultiLangString({}, pref_lang='fr')"
    assert repr(mls) == expected_repr, "The __repr__ output should reflect the different preferred language"
