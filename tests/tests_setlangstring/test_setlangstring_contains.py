import pytest

from langstring import LangString
from langstring import SetLangString


# Test cases for the __contains__ method
@pytest.mark.parametrize(
    "texts, lang, element, expected_result",
    [
        # String in SetLangString
        ({"hello", "world"}, "en", "hello", True),
        # String not in SetLangString
        ({"hello", "world"}, "en", "goodbye", False),
        # LangString with same language in SetLangString
        ({"hello", "world"}, "en", LangString("hello", "en"), True),
        # LangString with same language not in SetLangString
        ({"hello", "world"}, "en", LangString("goodbye", "en"), False),
        # LangString with different language
        ({"hello", "world"}, "en", LangString("hello", "fr"), ValueError),
        # Non-string, non-LangString type
        ({"hello", "world"}, "en", 5, TypeError),
        # Empty SetLangString
        (set(), "en", "hello", False),
        # Checking with empty string
        ({"hello", "world"}, "en", "", False),
        # Special characters in SetLangString
        ({"!", "@"}, "en", "!", True),
        # Emoji in SetLangString
        ({"😊", "😂"}, "en", "😊", True),
        # Mixed content in SetLangString
        ({"hello", "1", "😊"}, "en", "1", True),
    ],
)
def test_setlangstring_contains(texts, lang, element, expected_result):
    """
    Test the __contains__ method of SetLangString.

    :param texts: A set of texts for the SetLangString.
    :param lang: The language of the SetLangString.
    :param element: The element to check for containment.
    :param expected_result: The expected result of the containment check.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)

    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result, match=f".*{type(element).__name__}.*"):
            _ = element in set_lang_string
    else:
        assert (
            element in set_lang_string
        ) == expected_result, (
            f"Containment check failed for element '{element}' in SetLangString with texts {texts} and lang '{lang}'"
        )


# Additional test cases for the __contains__ method
@pytest.mark.parametrize(
    "texts, lang, element, expected_result",
    [
        # Null value (None) as element
        ({"hello", "world"}, "en", None, TypeError),
        # Empty LangString with same language
        ({"hello", "world"}, "en", LangString("", "en"), False),
        # LangString with empty text but different language
        ({"hello", "world"}, "en", LangString("", "fr"), ValueError),
        # SetLangString with mixed types and checking for a non-existent complex string
        ({"hello", "1", "😊"}, "en", "hello world", False),
    ],
)
def test_setlangstring_contains_additional(texts, lang, element, expected_result):
    """
    Additional tests for the __contains__ method of SetLangString.

    :param texts: A set of texts for the SetLangString.
    :param lang: The language of the SetLangString.
    :param element: The element to check for containment.
    :param expected_result: The expected result of the containment check.
    """
    set_lang_string = SetLangString(texts=texts, lang=lang)

    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result, match=f".*{type(element).__name__}.*"):
            _ = element in set_lang_string
    else:
        assert (
            element in set_lang_string
        ) == expected_result, (
            f"Containment check failed for element '{element}' in SetLangString with texts {texts} and lang '{lang}'"
        )
