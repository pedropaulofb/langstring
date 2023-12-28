import pytest

from langstring import LangString


def test_to_string() -> None:
    """Test the to_string method to ensure it returns the correct string representation of the LangString object."""
    ls = LangString("hello")
    assert ls.to_string() == '"hello"', f'Expected to_string() to return "hello", but got {ls.to_string()}'


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
def test_langstring_string_representation(text, lang, expected_str) -> None:
    """Test LangString string representation.

    :param text: Text for the LangString.
    :param lang: Language tag for the LangString.
    :param expected_str: Expected string representation.
    """
    lang_str = LangString(text, lang)
    assert str(lang_str) == expected_str, "LangString string representation is incorrect"
    assert lang_str.to_string() == expected_str, "LangString to_string method returned incorrect representation"
