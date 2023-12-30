import pytest

from langstring import MultiLangString


def test_remove_entry_existing():
    """
    Test remove_entry method for removing an existing entry.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}})
    mls.remove_entry("Hello", "en")
    assert "Hello" not in mls.mls_dict["en"], "Entry 'Hello' should be removed from the 'en' language set"


def test_remove_entry_nonexistent_text():
    """
    Test remove_entry method for a text that does not exist in the specified language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="Entry 'Hi@en' not found in the MultiLangString."):
        mls.remove_entry("Hi", "en")


def test_remove_entry_nonexistent_language():
    """
    Test remove_entry method for a language that does not exist in the MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="Entry 'Hello@fr' not found in the MultiLangString."):
        mls.remove_entry("Hello", "fr")


def test_remove_entry_last_in_language():
    """
    Test remove_entry method for removing the last entry in a language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    mls.remove_entry("Hello", "en")
    assert "en" not in mls.mls_dict, "Language 'en' should be removed from mls_dict after last entry is removed"
