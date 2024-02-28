import pytest

from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "lang, expected_texts, expected_lang",
    [
        ("en", {"Hello"}, "en"),  # Language exists with one entry
        ("fr", {"Bonjour", "Salut"}, "fr"),  # Language exists with multiple entries
        ("de", set(), "de"),  # Language does not exist
        (" ", set(), " "),  # Test with space as lang
        ("", set(), ""),  # Test with empty string as lang
        ("Ελ", set(), "Ελ"),  # Test with Greek characters
        ("Ру", {"Привет"}, "Ру"),  # Test with Cyrillic characters
        ("en😀", set(), "en😀"),  # Test with emojis
    ],
)
def test_get_setlangstring_valid_inputs(lang: str, expected_texts: set, expected_lang: str):
    """
    Test `get_setlangstring` with valid language inputs.

    :param lang: The language code to retrieve texts for.
    :param expected_texts: The expected set of texts for the given language.
    :param expected_lang: The expected language of the returned `SetLangString`.
    """
    mls = MultiLangString({"en": {"Hello"}, "fr": {"Bonjour", "Salut"}, "Ру": {"Привет"}})
    result = mls.get_setlangstring(lang)
    assert isinstance(result, SetLangString), "Result must be a SetLangString instance."
    assert result.texts == expected_texts, f"Expected texts for '{lang}' not matched."
    assert result.lang == expected_lang, f"Expected language '{expected_lang}' not matched."


@pytest.mark.parametrize(
    "lang, match_error",
    [
        (123, "Expected 'str', got 'int'."),  # Non-string input
        ([], "Expected 'str', got 'list'."),  # Non-string input
        (None, "Expected 'str', got 'NoneType'."),  # Non-string input
    ],
)
def test_get_setlangstring_invalid_inputs(lang: str, match_error: str):
    """
    Test `get_setlangstring` with invalid language inputs.

    :param lang: The invalid language code input.
    :param match_error: The expected error message part.
    """
    mls = MultiLangString()
    with pytest.raises(TypeError, match=match_error):
        mls.get_setlangstring(lang)


def test_get_setlangstring_unusual_but_valid_usage():
    """
    Test `get_setlangstring` with unusual but valid inputs to ensure it handles edge cases appropriately.
    """
    mls = MultiLangString({"EN-us": {"Hello"}, "EN-gb": {"Hello"}})
    result = mls.get_setlangstring("EN-us")
    assert result.lang == "EN-us", "Should handle case-sensitive and region-specific language codes correctly."
