import pytest

from langstring import Converter
from langstring import MultiLangString
from langstring import SetLangString


def test_convert_multilangstring_to_setlangstrings_with_multiple_languages():
    """
    Test converting a MultiLangString with multiple languages to a list of SetLangStrings.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})
    result = Converter.convert_multilangstring_to_setlangstrings(mls)
    expected = [SetLangString(texts={"Hello", "Hi"}, lang="en"), SetLangString(texts={"Bonjour"}, lang="fr")]
    assert all(
        setlangstring in result for setlangstring in expected
    ), "convert_multilangstring_to_setlangstrings should return SetLangStrings for all languages"


def test_convert_multilangstring_to_setlangstrings_with_single_language():
    """
    Test converting a MultiLangString with a single language to a list of SetLangStrings.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = Converter.convert_multilangstring_to_setlangstrings(mls)
    expected = [SetLangString(texts={"Hello"}, lang="en")]
    assert result == expected, "convert_multilangstring_to_setlangstrings should handle single language correctly"


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, "string"])
def test_convert_multilangstring_to_setlangstrings_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not MultiLangString).
    :return: None
    :raises TypeError: If input is not of type MultiLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected MultiLangString, got"):
        Converter.convert_multilangstring_to_setlangstrings(invalid_input)
