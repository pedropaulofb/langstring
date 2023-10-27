import pytest

from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString


def test_empty_multilangstring_length() -> None:
    """Ensure that an empty MultiLangString has a length of 0."""
    mls = MultiLangString()
    assert len(mls) == 0, "Expected an empty MultiLangString to have a length of 0."


def test_single_langstring_multilangstring_length() -> None:
    """Ensure that a MultiLangString with one LangString has a length of 1."""
    langstring = LangString(text="Hello", lang="en")
    mls = MultiLangString(langstring)
    assert len(mls) == 1, "Expected a MultiLangString with one LangString to have a length of 1."


def test_multiple_same_langstrings_multilangstring_length() -> None:
    """Ensure correct length for MultiLangString with multiple LangStrings of the same language."""
    langstring1 = LangString(text="Hello", lang="en")
    langstring2 = LangString(text="World", lang="en")
    mls = MultiLangString(langstring1, langstring2)
    assert len(mls) == 2, "Expected a MultiLangString with two LangStrings of the same language to have a length of 2."


def test_multiple_diff_langstrings_multilangstring_length() -> None:
    """Ensure correct length for MultiLangString with LangStrings of different languages."""
    langstring1 = LangString(text="Hello", lang="en")
    langstring2 = LangString(text="Hola", lang="es")
    mls = MultiLangString(langstring1, langstring2)
    assert len(mls) == 2, "Expected a MultiLangString with LangStrings of different languages to have a length of 2."


def test_remove_langstring_affects_length() -> None:
    """Ensure that removing a LangString from MultiLangString updates its length."""
    langstring1 = LangString(text="Hello", lang="en")
    langstring2 = LangString(text="World", lang="en")
    mls = MultiLangString(langstring1, langstring2)

    initial_length = len(mls)
    mls.remove_langstring(langstring1)
    new_length = len(mls)

    assert new_length == initial_length - 1, "Expected the MultiLangString's length to decrease by 1 after removal."


def test_multilangstring_length_with_empty_langstring() -> None:
    """Ensure that a MultiLangString with an empty LangString has a length of 1."""
    langstring = LangString(text="", lang="en")
    mls = MultiLangString(langstring)
    assert len(mls) == 1, "Expected a MultiLangString with an empty LangString to have a length of 1."


def test_multilangstring_length_empty() -> None:
    """Ensure that an empty MultiLangString has a length of 0."""
    mls = MultiLangString()
    assert len(mls) == 0, "Expected length for an empty MultiLangString to be 0."


def test_multilangstring_length_same_language() -> None:
    """Test MultiLangString length when multiple LangStrings of the same language are added."""
    en_string1 = LangString(text="Hello", lang="en")
    en_string2 = LangString(text="World", lang="en")
    mls = MultiLangString(en_string1, en_string2, control="ALLOW")
    assert len(mls) == 2, "Expected length should include multiple LangStrings of the same language."


def test_multilangstring_length_diff_languages() -> None:
    """Test length with LangStrings of different languages."""
    en_string = LangString(text="Hello", lang="en")
    fr_string = LangString(text="Bonjour", lang="fr")
    mls = MultiLangString(en_string, fr_string)
    assert len(mls) == 2, "Expected length should count LangStrings of different languages separately."


def test_multilangstring_length_after_removal() -> None:
    """Test length after removing LangStrings."""
    en_string = LangString(text="Hello", lang="en")
    fr_string = LangString(text="Bonjour", lang="fr")
    mls = MultiLangString(en_string, fr_string)
    mls.remove_langstring(en_string)
    assert len(mls) == 1, "Length should decrease after removing a LangString."


def test_multilangstring_length_block_on_duplicate() -> None:
    """Ensure that length is unaffected when adding duplicate LangString is blocked."""
    en_string1 = LangString(text="Hello", lang="en")
    en_string2 = LangString(text="Hello", lang="en")
    mls = MultiLangString(en_string1, control="BLOCK_ERROR")
    with pytest.raises(ValueError):
        mls.add(en_string2)
    assert len(mls) == 1, "Length should not change when addition of duplicate LangString is blocked."
