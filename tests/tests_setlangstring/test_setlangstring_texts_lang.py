from typing import Optional
from typing import Set

import pytest

from langstring import SetLangString


@pytest.mark.parametrize(
    "texts, lang, expected_texts, expected_lang_str",
    [
        ({"hello", "world"}, "en", {"hello", "world"}, "en"),
        (set(), "en", set(), "en"),  # Adjusted to use set directly for comparison
        ({"привет", "мир"}, "ru", {"привет", "мир"}, "ru"),
        ({"😊", "😂"}, "en", {"😊", "😂"}, "en"),
        ({"", " "}, "en", {"", " "}, "en"),
        ({"UPPER", "lower"}, "en", {"UPPER", "lower"}, "en"),
        ({"   leading", "trailing   "}, "en", {"   leading", "trailing   "}, "en"),
        ({"Γειά", "σου"}, "el", {"Γειά", "σου"}, "el"),
        ({"mixedCASE", "TEXT"}, "en", {"mixedCASE", "TEXT"}, "en"),
        ({"    "}, "en", {"    "}, "en"),  # Strings with only spaces
        ({"", "non-empty"}, "en", {"", "non-empty"}, "en"),  # Empty and non-empty
    ],
)
def test_setlangstring_texts_and_lang_initialization(
    texts: Set[str], lang: str, expected_texts: Set[str], expected_lang_str: str
) -> None:
    """
    Test the initialization of SetLangString with various sets of texts and languages.

    :param texts: The set of texts to initialize the SetLangString with.
    :param lang: The language code to initialize the SetLangString with.
    :param expected_texts: The expected set of texts after initialization.
    :param expected_lang_str: The expected language code after initialization.
    :return: None. Asserts if the texts and language are correctly initialized and represented.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)
    assert set_lang_string.texts == expected_texts, (
        f"Expected texts {expected_texts} but got {set_lang_string.texts} "
        f"when initializing with texts {texts} and language '{lang}'"
    )
    assert set_lang_string.lang == expected_lang_str, (
        f"Expected language '{expected_lang_str}' but got '{set_lang_string.lang}' "
        f"when initializing with language '{lang}'"
    )


@pytest.mark.parametrize(
    "invalid_texts, exception",
    [
        (["list", "of", "strings"], TypeError),
        ("string", TypeError),
        (123, TypeError),
        ((None,), TypeError),
        (({"nested": "dict"},), TypeError),
    ],
)
def test_setlangstring_invalid_texts_initialization(invalid_texts: Optional[Set[str]], exception: Exception) -> None:
    """
    Test the initialization of SetLangString with invalid types for texts.

    :param invalid_texts: The invalid type of texts to initialize the SetLangString with.
    :param exception: The exception type that is expected to be raised.
    :param match: The regex pattern that the exception message is expected to match.
    :return: None. Asserts if the correct exception is raised with the expected message.
    """
    with pytest.raises(exception, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString(texts=invalid_texts)


@pytest.mark.parametrize(
    "invalid_lang, exception",
    [
        (123, TypeError),
        ([], TypeError),
        (None, TypeError),
    ],
)
def test_setlangstring_invalid_lang_initialization(invalid_lang: str, exception: Exception) -> None:
    """
    Test the initialization of SetLangString with invalid types for lang.

    :param invalid_lang: The invalid type of language to initialize the SetLangString with.
    :param exception: The exception type that is expected to be raised.
    :param match: The regex pattern that the exception message is expected to match.
    :return: None. Asserts if the correct exception is raised with the expected message.
    """
    with pytest.raises(exception, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString(texts={"valid", "set"}, lang=invalid_lang)


@pytest.mark.parametrize(
    "invalid_texts, invalid_lang",
    [
        ([], 123),  # Invalid types
    ],
)
def test_setlangstring_invalid_initialization(invalid_texts, invalid_lang):
    """Test SetLangString initialization with invalid texts and language types or null values."""
    with pytest.raises(TypeError, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString(texts=invalid_texts)
    with pytest.raises(TypeError, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString(lang=invalid_lang)


@pytest.mark.parametrize(
    "texts, lang",
    [
        ({" singleword "}, "en"),
        ({"UPPERCASE", "lowercase", "Numbers123"}, "en"),
        ({"Καλημέρα", "κόσμε"}, "el"),  # Greek characters
        ({"Привет", "мир"}, "ru"),  # Cyrillic characters
        ({"Emoji😊", "Symbols#@"}, "en"),
        # Additional valid but unusual usages
        ({" leading space", "trailing space "}, "en"),  # Leading and trailing spaces
        ({"MixedCASEusage", "anotherOne"}, "en"),  # Mixed case usage
        ({"", "  "}, "en"),  # Empty string and string with spaces
        ({"123", "@!#"}, "en"),  # Numbers and special characters
        ({"\nNewLine", "\tTab"}, "en"),  # Escape sequences
    ],
)
def test_setlangstring_unusual_but_valid_usage(texts: Set[str], lang: str) -> None:
    """
    Test SetLangString initialization and usage with unusual but valid texts and languages.

    :param texts: A set of strings representing the texts to be used for initialization.
    :param lang: A string representing the language code.
    :return: None. Asserts if the SetLangString instance does not correctly initialize or represent the texts and language.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)
    assert set_lang_string.texts == texts, (
        f"Failed to initialize or represent texts correctly. " f"Expected {texts}, got {set_lang_string.texts}."
    )
    assert set_lang_string.lang == lang, (
        f"Failed to initialize or represent the language correctly. " f"Expected {lang}, got {set_lang_string.lang}."
    )


@pytest.mark.parametrize(
    "texts",
    [
        {"hello", "world"},  # Valid usage
        set(),  # Empty set
    ],
)
def test_setlangstring_operation_on_itself(texts):
    """Test operations on SetLangString instance itself if applicable."""
    lang_string = SetLangString(texts=texts, lang="en")
    lang_string.texts = texts  # Re-assigning to itself
    assert lang_string.texts == texts, "Failed operation on itself with texts reassignment."
