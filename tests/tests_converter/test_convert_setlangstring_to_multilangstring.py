import pytest

from langstring import Converter
from langstring import MultiLangString
from langstring import SetLangString


def test_convert_setlangstring_to_multilangstring_with_multiple_texts():
    """
    Test converting a SetLangString with multiple texts to a MultiLangString.
    """
    set_lang_string = SetLangString(texts={"Hello", "Hi"}, lang="en")
    result = Converter.convert_setlangstring_to_multilangstring(set_lang_string)
    expected = MultiLangString(mls_dict={"en": {"Hello", "Hi"}})
    assert result == expected, "convert_setlangstring_to_multilangstring should return MultiLangString with all texts"


def test_convert_setlangstring_to_multilangstring_with_single_text():
    """
    Test converting a SetLangString with a single text to a MultiLangString.
    """
    set_lang_string = SetLangString(texts={"Hello"}, lang="en")
    result = Converter.convert_setlangstring_to_multilangstring(set_lang_string)
    expected = MultiLangString(mls_dict={"en": {"Hello"}})
    assert result == expected, "convert_setlangstring_to_multilangstring should handle single text correctly"


def test_convert_setlangstring_to_multilangstring_with_null_language():
    """
    Test converting a SetLangString with null language to a MultiLangString.
    """
    set_lang_string = SetLangString(texts={"Hello"}, lang=None)
    result = Converter.convert_setlangstring_to_multilangstring(set_lang_string)
    expected = MultiLangString(mls_dict={None: {"Hello"}})
    assert result == expected, "convert_setlangstring_to_multilangstring should handle null language correctly"


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, "string", MultiLangString()])
def test_convert_setlangstring_to_multilangstring_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not SetLangString).
    :return: None
    :raises TypeError: If input is not of type SetLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected SetLangString, got"):
        Converter.convert_setlangstring_to_multilangstring(invalid_input)
