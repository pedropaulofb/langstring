import pytest

from langstring_lib.langstring import LangString


def test_to_string() -> None:
    """Test the to_string method to ensure it returns the correct string representation of the LangString object."""
    ls = LangString("hello")
    assert ls.to_string() == '"hello"', f'Expected to_string() to return "hello", but got {ls.to_string()}'


def test_to_string_invalid_argument():
    """Test passing an invalid argument to the to_string method."""
    ls = LangString("hello")
    with pytest.raises(TypeError):
        ls.to_string("abc")


def test_str() -> None:
    """Test the __str__ method to ensure it returns the correct string representation of the LangString object."""
    ls = LangString("hola", "es")
    assert str(ls) == '"hola"@es', f'Expected str() to return "hola"@es, but got {str(ls)}'
