import pytest

from langstring import Converter
from langstring import LangString
from langstring import SetLangString


def test_convert_setlangstring_to_langstrings_with_multiple_texts():
    """
    Test converting a SetLangString with multiple texts to a list of LangStrings.
    """
    set_lang_string = SetLangString(texts={"Hello", "Hi"}, lang="en")
    result = Converter.convert_setlangstring_to_langstrings(set_lang_string)
    expected = [LangString("Hello", "en"), LangString("Hi", "en")]
    assert all(
        langstring in result for langstring in expected
    ), "convert_setlangstring_to_langstrings should return LangStrings for all texts"


def test_convert_setlangstring_to_langstrings_with_single_text():
    """
    Test converting a SetLangString with a single text to a list of LangStrings.
    """
    set_lang_string = SetLangString(texts={"Hello"}, lang="en")
    result = Converter.convert_setlangstring_to_langstrings(set_lang_string)
    expected = [LangString("Hello", "en")]
    assert result == expected, "convert_setlangstring_to_langstrings should handle single text correctly"



@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, "string", LangString("Hello", "en")])
def test_convert_setlangstring_to_langstrings_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not SetLangString).
    :return: None
    :raises TypeError: If input is not of type SetLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected SetLangString, got"):
        Converter.convert_setlangstring_to_langstrings(invalid_input)
