import pytest

from langstring import Converter
from langstring import LangString
from langstring import MultiLangString


def test_convert_multilangstring_to_langstrings_with_multiple_languages():
    """
    Test retrieving all LangStrings from a MultiLangString with multiple languages.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = Converter.convert_multilangstring_to_langstrings(mls)
    expected = [LangString("Hello", "en"), LangString("Hi", "en"), LangString("Bonjour", "fr")]
    assert all(
        langstring in result for langstring in expected
    ), "convert_multilangstring_to_langstrings should return all LangStrings for all languages"


def test_convert_multilangstring_to_langstrings_with_empty_multilangstring():
    """
    Test retrieving all LangStrings from an empty MultiLangString.
    """
    mls = MultiLangString()
    result = Converter.convert_multilangstring_to_langstrings(mls)
    assert (
        result == []
    ), "convert_multilangstring_to_langstrings should return an empty list for an empty MultiLangString"


def test_convert_multilangstring_to_langstrings_with_single_language():
    """
    Test retrieving all LangStrings from a MultiLangString with a single language.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = Converter.convert_multilangstring_to_langstrings(mls)
    expected = [LangString("Hello", "en")]
    assert (
        result == expected
    ), "convert_multilangstring_to_langstrings should return all LangStrings for a MultiLangString with a single language"


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, LangString("Hello", "en")])
def test_convert_multilangstring_to_langstrings_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not MultiLangString).
    :return: None
    :raises TypeError: If input is not of type MultiLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected MultiLangString, got"):
        Converter.convert_multilangstring_to_langstrings(invalid_input)
