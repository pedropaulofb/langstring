import pytest

from langstring import Controller
from langstring import Converter
from langstring import LangString
from langstring import LangStringFlag
from langstring import MultiLangString
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "input_text, input_lang, expected_output",
    [
        ("Hello", "en", MultiLangString(mls_dict={"en": {"Hello"}}, pref_lang="en")),
        ("Hola", "es", MultiLangString(mls_dict={"es": {"Hola"}}, pref_lang="es")),
        ("Bonjour", "fr", MultiLangString(mls_dict={"fr": {"Bonjour"}}, pref_lang="fr")),
    ],
)
def test_convert_langstring_to_multilangstring_valid(
    input_text: str, input_lang: str, expected_output: MultiLangString
):
    """Test conversion of valid LangString to MultiLangString.

    :param input_text: The text of the LangString.
    :param input_lang: The language code of the LangString.
    :param expected_output: The expected MultiLangString output.
    :return: None
    """
    lang_string = LangString(text=input_text, lang=input_lang)
    result = Converter.convert_langstring_to_multilangstring(lang_string)
    assert result == expected_output, "Conversion of LangString to MultiLangString did not produce expected result."


@pytest.mark.parametrize("invalid_input", [123, 5.5, True, None, [], {}])
def test_convert_langstring_to_multilangstring_invalid_type(invalid_input):
    """Test conversion with invalid input types, expecting a TypeError.

    :param invalid_input: An input of invalid type (not LangString).
    :return: None
    :raises TypeError: If input is not of type LangString.
    """
    with pytest.raises(TypeError, match="Invalid input argument type. Expected LangString, got"):
        Converter.convert_langstring_to_multilangstring(invalid_input)


def test_convert_langstring_to_multilangstring_empty_string():
    """Test conversion of LangString with empty string to MultiLangString.

    :return: None
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.set_flag(MultiLangStringFlag.DEFINED_TEXT, False)
    lang_string = LangString(text="", lang="en")
    result = Converter.convert_langstring_to_multilangstring(lang_string)
    assert result == MultiLangString(
        mls_dict={"en": {""}}, pref_lang="en"
    ), "Conversion of empty LangString did not produce expected MultiLangString."


def test_convert_langstring_to_multilangstring_none_language():
    """Test conversion of LangString with None as language to MultiLangString.

    :return: None
    """
    lang_string = LangString(text="Hello", lang=None)
    result = Converter.convert_langstring_to_multilangstring(lang_string)
    assert result == MultiLangString(
        mls_dict={None: {"Hello"}}, pref_lang=None
    ), "Conversion of LangString with None language did not produce expected MultiLangString."


def test_convert_langstring_to_multilangstring_empty_langstring():
    """Test conversion of an empty LangString (no text and no language) to MultiLangString.

    :return: None
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.set_flag(MultiLangStringFlag.DEFINED_TEXT, False)
    lang_string = LangString()
    result = Converter.convert_langstring_to_multilangstring(lang_string)
    assert result == MultiLangString(
        mls_dict={None: {""}}, pref_lang=None
    ), "Conversion of empty LangString did not produce expected MultiLangString."
