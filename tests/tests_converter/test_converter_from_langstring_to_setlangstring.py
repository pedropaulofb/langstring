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
def test_langstring_to_setlangstring_valid(input_text: str, input_lang: str, expected_output: SetLangString):
    """Test conversion of valid LangString to SetLangString.

    :param input_text: The text of the LangString.
    :param input_lang: The language code of the LangString.
    :param expected_output: The expected SetLangString output.
    :return: None
    """
    lang_string = LangString(text=input_text, lang=input_lang)
    result = Converter.from_langstring_to_setlangstring(lang_string)
    assert result == expected_output, "Conversion of LangString to SetLangString did not produce expected result."


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}])
def test_langstring_to_setlangstring_invalid_type(invalid_input):
    """Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not LangString).
    :return: None
    :raises TypeError: If input is not of type LangString.
    """
    with pytest.raises(TypeError, match="Argument '.+' must be of type 'LangString', but got"):
        Converter.from_langstring_to_setlangstring(invalid_input)


def test_langstring_to_setlangstring_empty_string():
    """Test conversion of LangString with empty string to SetLangString.

    :return: None
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    lang_string = LangString(text="", lang="en")
    result = Converter.from_langstring_to_setlangstring(lang_string)
    assert result == SetLangString(
        texts={""}, lang="en"
    ), "Conversion of empty LangString did not produce expected SetLangString."


@pytest.mark.parametrize(
    "input_text, input_lang",
    [
        ("", ""),  # Both text and language are empty
        ("Hello", ""),  # Valid text but empty language
        ("", "en"),  # Empty text but valid language
        ("こんにちは", "ja"),  # Non-ASCII text
        ("12345", "num"),  # Numeric text
        ("True", "bool"),  # Boolean-like text
    ],
)
def test_langstring_to_setlangstring_varied_inputs(input_text: str, input_lang: str):
    """Test conversion of LangString with varied inputs to SetLangString.

    :param input_text: The text of the LangString.
    :param input_lang: The language code of the LangString.
    :return: None
    """
    lang_string = LangString(text=input_text, lang=input_lang)
    result = Converter.from_langstring_to_setlangstring(lang_string)
    expected_output = SetLangString(texts={input_text}, lang=input_lang)
    assert result == expected_output, "Conversion did not handle varied inputs correctly."


def test_langstring_to_setlangstring_with_flags():
    """Test conversion behavior when specific flags are set.

    :return: None
    """
    # Set flags that might affect LangString behavior
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    Controller.set_flag(LangStringFlag.LOWERCASE_LANG, True)

    lang_string = LangString(text="Test", lang="EN")
    result = Converter.from_langstring_to_setlangstring(lang_string)
    expected_output = SetLangString(texts={"Test"}, lang="en")

    # Reset flags to default
    Controller.reset_flags()

    assert result == expected_output, "Conversion did not respect LangString flags."


def test_langstring_to_setlangstring_with_custom_langstring():
    """Test conversion using a custom LangString subclass.

    :return: None
    """

    class CustomLangString(LangString):
        pass

    custom_lang_string = CustomLangString(text="Custom", lang="custom")
    result = Converter.from_langstring_to_setlangstring(custom_lang_string)
    expected_output = SetLangString(texts={"Custom"}, lang="custom")

    assert result == expected_output, "Conversion did not handle custom LangString subclass correctly."


def test_langstring_to_setlangstring_with_duplicate_text():
    """Test conversion of LangString with duplicate text to SetLangString.

    :return: None
    """
    lang_string = LangString(text="Duplicate", lang="en")
    result = Converter.from_langstring_to_setlangstring(lang_string)
    expected_output = SetLangString(texts={"Duplicate"}, lang="en")

    assert result == expected_output, "Conversion did not handle duplicate text correctly."
