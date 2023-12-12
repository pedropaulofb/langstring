import pytest

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags():
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
    yield


@pytest.mark.parametrize(
    "text1, lang1, text2, lang2, expected",
    [
        ("Hello", "en", "Hello", "en", True),
        ("Hello", "en", "Hello", None, False),
        ("Hello", None, "Hello", "en", False),
        ("Hello", "en", "Hola", "en", False),
        ("Hello", "en", "Hello", "es", False),
        ("Hello", None, "Hello", None, True),
        ("", "", "", "", True),
        ("Hello", "en", "hello", "en", False),
    ],
)
def test_eq_with_various_strings(text1: str, lang1: str, text2: str, lang2: str, expected: bool):
    """
    Test the __eq__ method with various combinations of text and language.

    :param text1: Text for the first LangString object.
    :param lang1: Language for the first LangString object.
    :param text2: Text for the second LangString object.
    :param lang2: Language for the second LangString object.
    :param expected: Expected result of the equality comparison.
    """
    lang_string1 = LangString(text1, lang1)
    lang_string2 = LangString(text2, lang2)
    assert (lang_string1 == lang_string2) is expected, (
        f"Equality check failed for LangString objects with "
        f"text1='{text1}', lang1='{lang1}', text2='{text2}', "
        f"and lang2='{lang2}'"
    )


def test_eq_with_different_types():
    """
    Test the __eq__ method when compared with a different type.
    """
    lang_string = LangString("Hello", "en")
    assert (lang_string == 42) is False, "LangString object should not be equal to an object of a different type"


def test_eq_with_none():
    """
    Test the __eq__ method when compared with None.
    """
    lang_string = LangString("Hello", "en")
    assert (lang_string is None) is False, "LangString object should not be equal to None"


# Fixtures for creating LangString instances
@pytest.fixture
def langstring_en_hello():
    return LangString("Hello", "en")


@pytest.fixture
def langstring_en_hi():
    return LangString("Hi", "en")


@pytest.fixture
def langstring_es_hello():
    return LangString("Hello", "es")


@pytest.fixture
def langstring_en_hello_duplicate():
    return LangString("Hello", "en")


# Tests for __ne__ method
def test_neq_different_texts(langstring_en_hello, langstring_en_hi):
    """Test inequality with different texts but same language."""
    assert (
        langstring_en_hello != langstring_en_hi
    ), "LangStrings with different texts but same language should be unequal"


def test_neq_different_languages(langstring_en_hello, langstring_es_hello):
    """Test inequality with same text but different languages."""
    assert (
        langstring_en_hello != langstring_es_hello
    ), "LangStrings with same text but different languages should be unequal"


def test_neq_different_texts_and_languages(langstring_en_hello):
    """Test inequality with different texts and different languages."""
    langstring_es_hi = LangString("Hola", "es")
    assert langstring_en_hello != langstring_es_hi, "LangStrings with different texts and languages should be unequal"


def test_neq_same_text_language(langstring_en_hello, langstring_en_hello_duplicate):
    """Test equality with same text and language."""
    assert (
        langstring_en_hello == langstring_en_hello_duplicate
    ), "LangStrings with same text and language should be equal"


def test_neq_with_different_type(langstring_en_hello):
    """Test inequality when compared with a different type."""
    assert langstring_en_hello != "Hello", "LangString should be unequal to a non-LangString object"


def test_neq_with_none(langstring_en_hello):
    """Test inequality when compared with None."""
    assert langstring_en_hello is not None, "LangString should be unequal to None"
