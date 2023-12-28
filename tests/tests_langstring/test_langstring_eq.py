import pytest

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


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
def test_eq_with_various_strings(text1: str, lang1: str, text2: str, lang2: str, expected: bool) -> None:
    """Test the __eq__ method with various combinations of text and language.

    :param text1: Text for the first LangString object.
    :param lang1: Language for the first LangString object.
    :param text2: Text for the second LangString object.
    :param lang2: Language for the second LangString object.
    :param expected: Expected result of the equality comparison.
    """
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    lang_string1 = LangString(text1, lang1)
    lang_string2 = LangString(text2, lang2)
    assert (lang_string1 == lang_string2) is expected, (
        f"Equality check failed for LangString objects with "
        f"text1='{text1}', lang1='{lang1}', text2='{text2}', "
        f"and lang2='{lang2}'"
    )


def test_eq_with_different_types() -> None:
    """Test the __eq__ method when compared with a different type."""
    lang_string = LangString("Hello", "en")
    assert (lang_string == 42) is False, "LangString object should not be equal to an object of a different type"


def test_eq_with_none() -> None:
    """Test the __eq__ method when compared with None."""
    lang_string = LangString("Hello", "en")
    assert (lang_string is None) is False, "LangString object should not be equal to None"


# Fixtures for creating LangString instances
@pytest.fixture
def langstring_en_hello() -> LangString:
    return LangString("Hello", "en")


@pytest.fixture
def langstring_en_hi() -> LangString:
    return LangString("Hi", "en")


@pytest.fixture
def langstring_es_hello() -> LangString:
    return LangString("Hello", "es")


@pytest.fixture
def langstring_en_hello_duplicate() -> LangString:
    return LangString("Hello", "en")


@pytest.mark.parametrize(
    "text, lang, other_text, other_lang, are_equal",
    [
        ("Hello", "en", "Hello", "en", True),
        ("Hello", "en", "Hello", None, False),
        ("Hello", "en", "Hi", "en", False),
        ("Hello", None, "Hello", None, True),
    ],
)
def test_langstring_equality(text, lang, other_text, other_lang, are_equal) -> None:
    """Test LangString equality and hashing.

    :param text: Text for the first LangString.
    :param lang: Language tag for the first LangString.
    :param other_text: Text for the second LangString.
    :param other_lang: Language tag for the second LangString.
    :param are_equal: Expected equality result.
    """
    lang_str1 = LangString(text, lang)
    lang_str2 = LangString(other_text, other_lang)
    assert (lang_str1 == lang_str2) is are_equal, "LangString equality check failed"


# Tests for __ne__ method
def test_neq_different_texts(langstring_en_hello, langstring_en_hi) -> None:
    """Test inequality with different texts but same language."""
    assert (
        langstring_en_hello != langstring_en_hi
    ), "LangStrings with different texts but same language should be unequal"


def test_neq_different_languages(langstring_en_hello, langstring_es_hello) -> None:
    """Test inequality with same text but different languages."""
    assert (
        langstring_en_hello != langstring_es_hello
    ), "LangStrings with same text but different languages should be unequal"


def test_neq_different_texts_and_languages(langstring_en_hello) -> None:
    """Test inequality with different texts and different languages."""
    langstring_es_hi = LangString("Hola", "es")
    assert langstring_en_hello != langstring_es_hi, "LangStrings with different texts and languages should be unequal"


def test_neq_same_text_language(langstring_en_hello, langstring_en_hello_duplicate) -> None:
    """Test equality with same text and language."""
    assert (
        langstring_en_hello == langstring_en_hello_duplicate
    ), "LangStrings with same text and language should be equal"


def test_neq_with_different_type(langstring_en_hello) -> None:
    """Test inequality when compared with a different type."""
    assert langstring_en_hello != "Hello", "LangString should be unequal to a non-LangString object"


def test_neq_with_none(langstring_en_hello) -> None:
    """Test inequality when compared with None."""
    assert langstring_en_hello is not None, "LangString should be unequal to None"


def test_langstring_equality() -> None:
    """Test that two LangString instances with the same text and language are equal."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "en")
    assert lang_str1 == lang_str2, "LangString instances with the same text and language should be equal"


def test_langstring_inequality() -> None:
    """Test that LangString instances with different text or language are not equal."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "fr")
    lang_str3 = LangString("Bonjour", "en")
    assert lang_str1 != lang_str2, "LangString instances with different languages should not be equal"
    assert lang_str1 != lang_str3, "LangString instances with different text should not be equal"


def test_eq_with_different_flag_settings() -> None:
    """
    Test the __eq__ method of LangString under different flag settings.

    :raises AssertionError: If the equality comparison does not behave as expected under different flag settings.
    """
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "en")
    assert lang_str1 == lang_str2, "LangString objects should be equal under the same flag settings"
    LangStringControl.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    assert lang_str1 == lang_str2, "LangString objects should be equal under different flag settings"
    LangStringControl.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)
    assert lang_str1 == lang_str2, "LangString objects should be equal under different flag settings"
    LangStringControl.reset_flags()
    assert lang_str1 == lang_str2, "LangString objects should be equal under different flag settings"
