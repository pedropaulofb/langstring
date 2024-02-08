from typing import List
from typing import Set
from typing import Union

import pytest

from langstring.converter import Converter
from langstring.setlangstring import SetLangString


@pytest.mark.parametrize(
    "input, lang, expected_texts",
    [
        ({"Hello", "World"}, "en", {"Hello", "World"}),
        (["Hello", "World"], "en", {"Hello", "World"}),
        ({"Привет", "Мир"}, "ru", {"Привет", "Мир"}),
        ({"こんにちは", "世界"}, "ja", {"こんにちは", "世界"}),
        ({"Hello", "Hello"}, "en", {"Hello"}),  # Duplicate elimination
    ],
)
def test_from_strings_to_setlangstring_valid(input: Union[Set[str], List[str]], lang: str, expected_texts: Set[str]):
    """
    Test the conversion of valid string sets or lists to SetLangString objects.

    :param input: The input set or list of strings to convert.
    :param lang: The language code for the SetLangString.
    :param expected_texts: The expected set of texts in the resulting SetLangString.
    """
    result = Converter.from_strings_to_setlangstring(input, lang)
    assert isinstance(result, SetLangString), "The result is not an instance of SetLangString."
    assert result.texts == expected_texts, f"Expected texts {expected_texts} but got {result.texts}."
    assert result.lang == lang, f"Expected language '{lang}' but got '{result.lang}'."


@pytest.mark.parametrize(
    "input, lang, match_text",
    [
        (123, "en", "must be of types 'set\\[str\\]' or 'list\\[str\\]' but got 'int'"),
        ("not a set or list", "en", "must be of types 'set\\[str\\]' or 'list\\[str\\]' but got 'str'"),
        ({"Hello", 123}, "en", "Invalid element type inside input argument. Expected 'str', got 'int'."),
    ],
)
def test_from_strings_to_setlangstring_invalid_types(input, lang: str, match_text: str):
    """
    Test the conversion function with invalid types to ensure proper error handling.

    :param input: The invalid input to trigger the TypeError.
    :param lang: A dummy language code.
    :param match_text: The regex pattern to match against the expected error message.
    """
    with pytest.raises(TypeError, match=match_text):
        Converter.from_strings_to_setlangstring(input, lang)


@pytest.mark.parametrize(
    "input, lang",
    [
        (None, "en"),
        ([], "en"),
        (set(), "en"),
    ],
)
def test_from_strings_to_setlangstring_empty_or_none(input, lang: str):
    """
    Test the conversion function with empty or None inputs to ensure ValueError is raised.

    :param input: The input that is empty or None.
    :param lang: A dummy language code.
    """
    with pytest.raises(ValueError, match="Cannot convert the empty input to a SetLangString."):
        Converter.from_strings_to_setlangstring(input, lang)


@pytest.mark.parametrize(
    "input, lang, expected_message",
    [
        ({"    ", "\t"}, "en", "SetLangString should handle strings with whitespace."),
        ({"Special@@chars", "#$%^"}, "en", "SetLangString should handle strings with special characters."),
    ],
)
def test_from_strings_to_setlangstring_unusual_valid_usage(input, lang, expected_message):
    """
    Test conversion with unusual but valid inputs.

    :param input: The input set or list of strings with unusual characters.
    :param lang: The language code.
    :param expected_message: Description of what the test verifies.
    """
    result = Converter.from_strings_to_setlangstring(input, lang)
    assert isinstance(result, SetLangString), expected_message


@pytest.mark.parametrize(
    "input, lang",
    [
        (["Hello", 123], "en"),  # Mixed types in list
        ({"Hello", None}, "en"),  # Mixed types in set
    ],
)
def test_from_strings_to_setlangstring_mixed_input_types(input, lang):
    """
    Test conversion with mixed input types within the collection.

    :param input: The input collection containing mixed types.
    :param lang: A dummy language code.
    """
    with pytest.raises(TypeError, match="Invalid element type inside input argument."):
        Converter.from_strings_to_setlangstring(input, lang)
