from typing import Optional

import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


def test_to_string() -> None:
    """Test the to_string method to ensure it returns the correct string representation of the LangString object."""
    ls = LangString("hello")
    assert ls.to_string() == "hello", f"Expected to_string() to return 'hello', but got {ls.to_string()}"


def test_to_string_invalid_argument() -> None:
    """Test passing an invalid argument to the to_string method."""
    ls = LangString("hello")
    with pytest.raises(TypeError):
        ls.to_string("abc")


def test_str() -> None:
    """Test the __str__ method to ensure it returns the correct string representation of the LangString object."""
    ls = LangString("hola", "es")
    assert str(ls) == '"hola"@es', f'Expected str() to return "hola"@es, but got {str(ls)}'


@pytest.mark.parametrize(
    "text, lang, expected_str",
    [
        ("Hello", "en", '"Hello"@en'),
        ("Hello", None, '"Hello"'),
        ("", "en", '""@en'),
        ("", None, '""'),
    ],
)
def test_langstring_string_representation(text: str, lang: Optional[str], expected_str: str) -> None:
    """Test LangString string representation.

    :param text: Text for the LangString.
    :type text: str
    :param lang: Language tag for the LangString.
    :type lang: Optional[str]
    :param expected_str: Expected string representation.
    :type expected_str: str
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    lang_str = LangString(text, lang)
    assert str(lang_str) == expected_str, "LangString string representation is incorrect"
    assert lang_str.to_string() == expected_str, "LangString to_string method returned incorrect representation"


def test_langstring_string_representation() -> None:
    """Test the string representation of LangString."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", None)
    assert str(lang_str1) == '"Hello"@en', "String representation with language should be correct"
    assert str(lang_str2) == "Hello", "String representation without language should be correct"


def test_to_string_with_different_flag_settings() -> None:
    """
    Test the to_string method of LangString under different flag settings.

    :raises AssertionError: If the string representation does not match the expected output under different flag settings.
    """
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    lang_str = LangString("Hello", "en")
    assert lang_str.to_string() == '"Hello"@en', "String representation should be correct with DEFINED_TEXT enabled"

    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    assert (
        lang_str.to_string() == '"Hello"@en'
    ), "String representation should remain correct with DEFINED_TEXT disabled"
