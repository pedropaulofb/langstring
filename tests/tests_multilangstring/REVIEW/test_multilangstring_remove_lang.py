import pytest

from langstring import MultiLangString


def test_remove_lang_existing_language():
    """
    Test remove_lang method for removing an existing language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    mls.remove_lang("en")
    assert "en" not in mls.mls_dict, "Language 'en' should be removed from the MultiLangString"


def test_remove_lang_nonexistent_language():
    """
    Test remove_lang method for a language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="Lang 'fr' not found in the MultiLangString."):
        mls.remove_lang("fr")


def test_remove_lang_empty_multilangstring():
    """
    Test remove_lang method for an empty MultiLangString.
    """
    mls = MultiLangString()
    with pytest.raises(ValueError, match="Lang 'en' not found in the MultiLangString."):
        mls.remove_lang("en")
