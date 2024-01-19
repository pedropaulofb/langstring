import pytest

from langstring import Converter
from langstring import LangString
from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (LangString(text="Hello", lang="en"), SetLangString(texts={"Hello"}, lang="en")),
        (MultiLangString(mls_dict={"en": {"Hello", "Hi"}}), [SetLangString(texts={"Hello", "Hi"}, lang="en")]),
    ],
)
def test_to_setlangstring_valid(input_data, expected_output):
    """
    Test converting valid LangString or MultiLangString to SetLangString or list of SetLangStrings.

    :param input_data: A LangString or MultiLangString instance.
    :param expected_output: The expected SetLangString or list of SetLangStrings.
    :return: None
    """
    result = Converter.to_setlangstring(input_data)
    assert (
        result == expected_output
    ), "to_setlangstring should return correct SetLangString or list of SetLangStrings for valid input"


@pytest.mark.parametrize(
    "invalid_input", [123, 5.5, True, None, [], {}, "string", SetLangString(texts={"Hello"}, lang="en")]
)
def test_to_setlangstring_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not LangString or MultiLangString).
    :return: None
    :raises TypeError: If input is not of type LangString or MultiLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected LangString or MultiLangString, got"):
        Converter.to_setlangstring(invalid_input)
