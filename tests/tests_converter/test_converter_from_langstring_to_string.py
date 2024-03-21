import pytest

from langstring import Converter
from langstring import LangString
from tests.conftest import TYPEERROR_MSG_SINGULAR


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        ("Hello, World!", "en", '"Hello, World!"@en'),
        ("Bonjour, le monde!", "fr", '"Bonjour, le monde!"@fr'),
        ("", "", '""@'),
        ("Hello, World!", "", '"Hello, World!"@'),
        ("", "en", '""@en'),
    ],
)
def test_from_langstring_to_string_valid_inputs(text: str, lang: str, expected: str):
    """Test conversion from LangString to string with various valid inputs.

    :param text: The text part of the LangString.
    :param lang: The language tag of the LangString.
    :param expected: The expected string output from the conversion.
    :return: None
    """
    lang_string = LangString(text=text, lang=lang)
    result = Converter.from_langstring_to_string(lang_string)
    assert (
        result == expected
    ), f"Expected conversion result '{expected}' but got '{result}' for LangString(text='{text}', lang='{lang}')."


@pytest.mark.parametrize(
    "text, lang",
    [
        (None, "en"),
        ("Hello, World!", None),
        (None, None),
    ],
)
def test_from_langstring_to_string_none_values(text: str, lang: str):
    """Test conversion from LangString to string handling None values for text and/or lang, expecting TypeError.

    :param text: The text part of the LangString, potentially None.
    :param lang: The language tag of the LangString, potentially None.
    :return: None
    :raises TypeError: When text or lang is None.
    """
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        Converter.from_langstring_to_string(LangString(text=text, lang=lang))


@pytest.mark.parametrize(
    "lang_string, expected",
    [
        (LangString("Hello, World!", "en-US"), '"Hello, World!"@en-US'),
        (LangString("こんにちは、世界！", "ja"), '"こんにちは、世界！"@ja'),
    ],
)
def test_from_langstring_to_string_language_tags(lang_string: LangString, expected: str):
    """Test conversion from LangString to string with language tags including region subtags.

    :param lang_string: The LangString object to convert.
    :param expected: The expected string representation including the language tag.
    :return: None
    """
    result = Converter.from_langstring_to_string(lang_string)
    assert (
        result == expected
    ), f"Expected '{expected}' but got '{result}' for LangString with language tag '{lang_string.lang}'."


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        ("Test", "en", '"Test"@en'),  # Expect language tag to be included
    ],
)
def test_from_langstring_to_string_consistent_behavior(text: str, lang: str, expected: str):
    """Test the consistent behavior of including language tags in the conversion from LangString to string.

    This test reflects the current implementation where the language tag is always included in the output string.

    :param text: The text part of the LangString.
    :param lang: The language tag of the LangString.
    :param expected: The expected string output.
    :return: None
    """
    lang_string = LangString(text=text, lang=lang)
    result = Converter.from_langstring_to_string(lang_string)
    assert (
        result == expected
    ), f"Expected '{expected}' but got '{result}' for LangString with text '{text}' and lang '{lang}'."
