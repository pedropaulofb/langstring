import pytest

from langstring_lib.langstring import LangString


def test_initialization() -> None:
    """Test the initialization of a LangString object without specifying a language."""
    ls = LangString("hello")
    assert ls.text == "hello", f'Expected text to be "hello", but got {ls.text}'
    assert isinstance(ls.text, str)
    assert ls.lang is None, f"Expected lang to be None, but got {ls.lang}"


def test_language_initialization() -> None:
    """Test the initialization of a LangString object with a specified language."""
    ls = LangString("hola", "es")
    assert ls.text == "hola", f'Expected text to be "hola", but got {ls.text}'
    assert isinstance(ls.text, str)
    assert ls.lang == "es", f'Expected lang to be "es", but got {ls.lang}'
    assert isinstance(ls.lang, str)


def test_empty_initialization() -> None:
    """Test the initialization of a LangString object with empty text and no specified language."""
    ls = LangString("")
    assert ls.text == "", f"Expected text to be an empty string, but got {ls.text}"
    assert ls.lang is None, f"Expected lang to be None, but got {ls.lang}"


def test_empty_language_initialization() -> None:
    """Test the initialization of a LangString object with empty text and a specified language."""
    ls = LangString("", "es")
    assert ls.text == "", f"Expected text to be an empty string, but got {ls.text}"
    assert ls.lang == "es", f'Expected lang to be "es", but got {ls.lang}'


def test_wrong_type_initialization() -> None:
    """Test initialization with wrong types."""
    with pytest.raises(TypeError):
        LangString(123)


def test_wrong_type_language_initialization() -> None:
    """Test language initialization with wrong types."""
    with pytest.raises(TypeError):
        LangString("hola", 123)


def test_whitespace_and_special_characters() -> None:
    ls = LangString(" hello world! @#$%^&*()_+ ")
    assert ls.text == " hello world! @#$%^&*()_+ ", f"Unexpected text: {ls.text}"


def test_very_long_string() -> None:
    long_string = "a" * 10000  # 10,000 characters
    ls = LangString(long_string)
    assert ls.text == long_string, f"Unexpected text: {ls.text}"
    assert ls.to_string() == f'"{long_string}"', f"Unexpected string representation: {ls.to_string()}"
