import pytest

from langstring import LangString
from langstring import MultiLangString


def test_get_langstring_with_existing_entry():
    """
    Test retrieving a LangString for an existing text and language combination.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = mls.get_langstring("Hello", "en")
    expected = LangString(text="Hello", lang="en")
    assert result == expected, "get_langstring should return the correct LangString for an existing entry"


def test_get_langstring_with_nonexistent_entry():
    """
    Test retrieving a LangString for a text and language combination that does not exist.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="Text 'Hi' with language 'en' not found in mls_dict."):
        mls.get_langstring("Hi", "en")


def test_get_langstring_with_nonexistent_language():
    """
    Test retrieving a LangString for a nonexistent language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="Text 'Hello' with language 'fr' not found in mls_dict."):
        mls.get_langstring("Hello", "fr")


def test_get_langstring_with_invalid_text_type():
    """
    Test retrieving a LangString with an invalid text type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="not found in mls_dict."):
        mls.get_langstring(123, "en")


def test_get_langstring_with_invalid_language_type():
    """
    Test retrieving a LangString with an invalid language type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(ValueError, match="not found in mls_dict."):
        mls.get_langstring("Hello", 123)
