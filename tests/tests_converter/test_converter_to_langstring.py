import pytest

from langstring import Converter
from langstring import LangString
from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (SetLangString(texts={"Hello", "Hi"}, lang="en"), [LangString("Hello", "en"), LangString("Hi", "en")]),
        (
            MultiLangString(mls_dict={"en": {"Hello"}, "es": {"Hola"}}),
            [LangString("Hello", "en"), LangString("Hola", "es")],
        ),
    ],
)
def test_to_langstring_valid(input_data, expected_output):
    """
    Test converting valid SetLangString or MultiLangString to a list of LangStrings.

    :param input_data: A SetLangString or MultiLangString instance.
    :param expected_output: The expected list of LangString instances.
    :return: None
    """
    result = Converter.to_langstring(input_data)
    assert all(
        langstring in result for langstring in expected_output
    ), "to_langstring should return correct LangStrings for valid input"


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}, "string", LangString("Hello", "en")])
def test_to_langstring_invalid_type(invalid_input):
    """
    Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not SetLangString or MultiLangString).
    :return: None
    :raises TypeError: If input is not of type SetLangString or MultiLangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected SetLangString or MultiLangString, got"):
        Converter.to_langstring(invalid_input)
