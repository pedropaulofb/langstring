import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


@pytest.mark.parametrize(
    "text1, lang1, text2, lang2, expected",
    [
        ("Hello, World!", "en", "Hello, World!", "en", True),
        ("Привет, мир!", "ru", "Привет, мир!", "ru", True),
        ("Γειά σου Κόσμε!", "el", "Γειά σου Κόσμε!", "el", True),
        ("Hello, World!", "en", "Bonjour, Monde!", "fr", False),
        ("😊", "emoji", "😊", "emoji", True),
        ("Hello, World!", "en", "Hello, World! ", "en", False),  # Trailing space
        ("", "en", "", "en", True),  # Empty strings
    ],
)
def test_ne_with_various_langstrings(text1: str, lang1: str, text2: str, lang2: str, expected: bool) -> None:
    """
    Test the `__ne__` method for equality with various LangString objects.

    :param text1: The text of the first LangString.
    :param lang1: The language tag of the first LangString.
    :param text2: The text of the second LangString.
    :param lang2: The language tag of the second LangString.
    :param expected: The expected result of the equality comparison.
    :return: None
    """
    lang_string1 = LangString(text1, lang1)
    lang_string2 = LangString(text2, lang2)
    assert (lang_string1 != lang_string2) != expected, f"Equality check failed for texts '{text1}' and '{text2}'"


@pytest.mark.parametrize(
    "lang_string_text, other_object",
    [
        ("Hello, World!", "Hello, World!"),
        ("Hello, World!", 42),
        ("Hello, World!", ["Hello", "World"]),
        ("Hello, World!", {"text": "Hello, World!"}),
        ("Hello, World!", None),
    ],
)
def test_ne_with_different_object_types(lang_string_text: str, other_object) -> None:
    """
    Test the `__ne__` method for equality with objects of different types.

    :param lang_string_text: The text of the LangString.
    :param other_object: An object of a different type.
    :return: None
    """
    lang_string = LangString(lang_string_text, "en")
    assert lang_string != other_object, f"LangString should not be equal to object of type {type(other_object)}"


@pytest.mark.parametrize(
    "text1, text2, lang, expected",
    [
        ("Hello, World!", "hello, world!", "en", False),  # Different casing in text
        ("HELLO, WORLD!", "hello, world!", "en", False),
        ("Hello, World!", "HELLO, WORLD!", "en", False),
    ],
)
def test_ne_case_insensitive_text(text1: str, text2: str, lang: str, expected: bool) -> None:
    """
    Test the `__ne__` method for case-insensitive text comparison.

    :param text1: The text of the first LangString.
    :param text2: The text of the second LangString.
    :param lang: The language tag of the LangStrings.
    :param expected: The expected result of the equality comparison.
    :return: None
    """
    lang_string1 = LangString(text1, lang)
    lang_string2 = LangString(text2, lang)
    assert (
        lang_string1 != lang_string2
    ) != expected, f"Text case-insensitivity check failed for '{text1}' and '{text2}'"


@pytest.mark.parametrize(
    "lang1, lang2",
    [
        ("en", "EN"),
        ("fr", "FR"),
        ("es", "Es"),
        ("EN", "en"),
        ("Fr", "fr"),
    ],
)
def test_ne_case_insensitive_language_tag(lang1: str, lang2: str) -> None:
    """
    Test the `__ne__` method for case-insensitive language tag comparison.

    :param lang1: The language tag of the first LangString.
    :param lang2: The language tag of the second LangString.
    :return: None
    """
    lang_string1 = LangString("Hello, World!", lang1)
    lang_string2 = LangString("Hello, World!", lang2)
    assert (
        lang_string1 == lang_string2
    ), f"LangString objects should be equal with case-insensitive language tags '{lang1}' and '{lang2}'"


@pytest.mark.parametrize(
    "text1, lang1, text2, lang2, flag_state, expected",
    [
        ("Hello, World!", "EN", "Hello, World!", "en", True, False),
        ("Hello, World!", "EN", "Hello, World!", "en", False, False),
        ("Hello, World!", "En", "Hello, World!", "En", True, False),
        ("Hello, World!", "En", "Hello, World!", "En", False, False),
        ("HELLO, WORLD!", "en", "hello, world!", "en", True, True),
        ("HELLO, WORLD!", "en", "hello, world!", "en", False, True),
    ],
)
def test_ne_with_text_and_lang_casing(
    text1: str, lang1: str, text2: str, lang2: str, flag_state: bool, expected: bool
) -> None:
    """
    Test the `__ne__` method for equality with different casing in text and language tags.

    :param text1: The text of the first LangString.
    :param lang1: The language tag of the first LangString.
    :param text2: The text of the second LangString.
    :param lang2: The language tag of the second LangString.
    :param flag_state: The state of the LOWERCASE_LANG flag.
    :param expected: The expected result of the equality comparison.
    :return: None
    """
    Controller.set_flag(LangStringFlag.LOWERCASE_LANG, flag_state)
    lang_string1 = LangString(text1, lang1)
    lang_string2 = LangString(text2, lang2)
    assert (
        lang_string1 != lang_string2
    ) == expected, f"Equality check failed under LOWERCASE_LANG flag state {flag_state}"
