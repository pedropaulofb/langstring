import pytest

from langstring import Controller
from langstring import Converter
from langstring import LangString
from langstring import LangStringFlag
from langstring import SetLangString


@pytest.mark.parametrize(
    "input_text, input_lang, expected_output",
    [
        ("Hello", "en", SetLangString(texts={"Hello"}, lang="en")),
        ("Hola", "es", SetLangString(texts={"Hola"}, lang="es")),
        ("Bonjour", "fr", SetLangString(texts={"Bonjour"}, lang="fr")),
    ],
)
def test_convert_langstring_to_setlangstring_valid(input_text: str, input_lang: str, expected_output: SetLangString):
    """Test conversion of valid LangString to SetLangString.

    :param input_text: The text of the LangString.
    :param input_lang: The language code of the LangString.
    :param expected_output: The expected SetLangString output.
    :return: None
    """
    lang_string = LangString(text=input_text, lang=input_lang)
    result = Converter.convert_langstring_to_setlangstring(lang_string)
    assert result == expected_output, "Conversion of LangString to SetLangString did not produce expected result."


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}])
def test_convert_langstring_to_setlangstring_invalid_type(invalid_input):
    """Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not LangString).
    :return: None
    :raises TypeError: If input is not of type LangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected LangString, got"):
        Converter.convert_langstring_to_setlangstring(invalid_input)


def test_convert_langstring_to_setlangstring_empty_string():
    """Test conversion of LangString with empty string to SetLangString.

    :return: None
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    lang_string = LangString(text="", lang="en")
    result = Converter.convert_langstring_to_setlangstring(lang_string)
    assert result == SetLangString(
        texts={""}, lang="en"
    ), "Conversion of empty LangString did not produce expected SetLangString."


def test_convert_langstring_to_setlangstring_none_language():
    """Test conversion of LangString with None as language to SetLangString.

    :return: None
    """
    lang_string = LangString(text="Hello", lang=None)
    result = Converter.convert_langstring_to_setlangstring(lang_string)
    assert result == SetLangString(
        texts={"Hello"}, lang=None
    ), "Conversion of LangString with None language did not produce expected SetLangString."


def test_convert_langstring_to_setlangstring_empty_langstring():
    """Test conversion of an empty LangString (no text and no language) to SetLangString.

    :return: None
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    lang_string = LangString()
    result = Converter.convert_langstring_to_setlangstring(lang_string)
    assert result == SetLangString(
        texts={""}, lang=None
    ), "Conversion of empty LangString did not produce expected SetLangString."