import pytest

from langstring import Converter
from langstring import LangString
from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (LangString(text="Hello", lang="en"), MultiLangString(mls_dict={"en": {"Hello"}})),
        (SetLangString(texts={"Hello", "Hi"}, lang="en"), MultiLangString(mls_dict={"en": {"Hello", "Hi"}})),
    ],
)
def test_convert_to_multilangstring_valid(input_data, expected_output):
    """
    Test converting valid LangString or SetLangString to MultiLangString.

    :param input_data: A LangString or SetLangString instance.
    :param expected_output: The expected MultiLangString instance.
    :return: None
    """
    result = Converter.convert_to_multilangstring(input_data)
    assert result == expected_output, "convert_to_multilangstring should return correct MultiLangString for valid input"


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, "string", MultiLangString()])
def test_convert_to_multilangstring_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not LangString or SetLangString).
    :return: None
    :raises TypeError: If input is not of type LangString or SetLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected LangString or SetLangString, got"):
        Converter.convert_to_multilangstring(invalid_input)
