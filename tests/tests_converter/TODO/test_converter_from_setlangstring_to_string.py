import pytest
from langstring import Converter, SetLangString


@pytest.mark.parametrize(
    "texts, lang, expected_output",
    [
        ({"Hello", "World"}, "en", "Hello, World"),
        (set(), "en", ""),  # Use set() for an empty set
        ({"Bonjour"}, "fr", "Bonjour"),
        ({"Hola", "Mundo"}, "es", "Hola, Mundo"),
    ],
)
def test_from_setlangstring_to_string_valid(texts, lang, expected_output):
    set_lang_string = SetLangString(texts=texts, lang=lang)
    result = Converter.from_setlangstring_to_string(set_lang_string)
    assert result == expected_output, f"Expected output '{expected_output}' but got '{result}'."




@pytest.mark.parametrize(
    "texts, lang, delimiter, expected_output",
    [
        ({"Hello", "World"}, "en", "; ", "Hello; World"),  # Custom delimiter
        ({"One", "Two", "Three"}, "en", " - ", "One - Two - Three"),  # Another delimiter
    ],
)
def test_from_setlangstring_to_string_with_custom_delimiter(
    texts: set[str], lang: str, delimiter: str, expected_output: str
):
    """
    Test conversion of SetLangString to a string using a custom delimiter.

    :param texts: The texts to include in the SetLangString.
    :param lang: The language tag for the SetLangString.
    :param delimiter: The delimiter to use in the output string.
    :param expected_output: The expected string output.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)
    result = Converter.from_setlangstring_to_string(set_lang_string, delimiter=delimiter)
    assert (
        result == expected_output
    ), f"Expected output '{expected_output}' but got '{result}' with delimiter '{delimiter}'."


def test_from_setlangstring_to_string_invalid_type():
    """
    Test conversion of SetLangString to a string with invalid input type, expecting a TypeError.
    """
    with pytest.raises(TypeError, match="Expected input of type SetLangString"):
        Converter.from_setlangstring_to_string("not a SetLangString")


@pytest.mark.parametrize(
    "texts, lang, expected_output",
    [
        ({"Hello, World", "Greetings: Earth"}, "en", "Hello, World, Greetings: Earth"),  # Texts with punctuation
        ({"こんにちは", "世界"}, "ja", "こんにちは, 世界"),  # Non-Latin scripts
        ({"😀", "🌍"}, "emoji", "😀, 🌍"),  # Emoji texts
    ],
)
def test_from_setlangstring_to_string_special_characters(texts: set[str], lang: str, expected_output: str):
    """
    Test conversion of SetLangString to a string with texts containing special characters.

    :param texts: The texts to include in the SetLangString, containing special characters.
    :param lang: The language tag for the SetLangString.
    :param expected_output: The expected string output, including special characters.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)
    result = Converter.from_setlangstring_to_string(set_lang_string)
    assert result == expected_output, f"Expected output '{expected_output}' but got '{result}'."
