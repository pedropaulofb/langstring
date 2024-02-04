import pytest

from langstring import Controller
from langstring import Converter
from langstring import SetLangString
from langstring import SetLangStringFlag


@pytest.mark.parametrize(
    "texts, lang, flags, expected",
    [
        ({"Hello", "World"}, "en", (False, False), ["Hello", "World"]),
        ({"Bonjour", "Monde"}, "fr", (True, False), ['"Bonjour"', '"Monde"']),
        ({"Hola", "Mundo"}, "es", (False, True), ["Hola@es", "Mundo@es"]),
        ({"Ciao", "Mondo"}, "it", (True, True), ['"Ciao"@it', '"Mondo"@it']),
    ],
)
def test_from_setlangstring_to_strings_flags(texts, lang, flags, expected):
    Controller.set_flag(SetLangStringFlag.PRINT_WITH_QUOTES, flags[0])
    Controller.set_flag(SetLangStringFlag.PRINT_WITH_LANG, flags[1])
    set_lang_string = SetLangString(texts=texts, lang=lang)
    result = Converter.from_setlangstring_to_strings(set_lang_string)
    assert sorted(result) == sorted(expected), f"Expected {expected} but got {result} under flags {flags}."


@pytest.mark.parametrize(
    "invalid_input",
    [123, "not a SetLangString", None],
)
def test_from_setlangstring_to_strings_invalid_input(invalid_input):
    """Test from_setlangstring_to_strings with various invalid input types.

    :param invalid_input: The invalid input to test.
    :param expected_error: The expected error message.
    """
    with pytest.raises(TypeError, match="Argument '.+' must be of type 'SetLangString', but got"):
        Converter.from_setlangstring_to_strings(invalid_input)


@pytest.mark.parametrize(
    "texts, lang, expected",
    [
        (set(), "en", []),  # Testing with an empty set
        ({"123", "456"}, "en", ["123", "456"]),  # Numeric strings
        ({"👋🌍"}, "emoji", ["👋🌍"]),  # Emojis
        ({"This is a very long string" * 10}, "en", ["This is a very long string" * 10]),  # Long string
    ],
)
def test_from_setlangstring_to_strings_edge_cases(texts, lang, expected):
    """Test from_setlangstring_to_strings with various edge cases.

    :param texts: A set of strings to be included in the SetLangString.
    :param lang: The language tag associated with the texts. Can be None.
    :param expected: The expected list of strings after conversion.
    """
    Controller.set_flag(SetLangStringFlag.PRINT_WITH_QUOTES, False)
    Controller.set_flag(SetLangStringFlag.PRINT_WITH_LANG, False)
    set_lang_string = SetLangString(texts=texts, lang=lang)
    result = Converter.from_setlangstring_to_strings(set_lang_string)
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}."
