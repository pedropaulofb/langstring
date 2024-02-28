import pytest

from langstring import Controller
from langstring import MultiLangString
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "initial_contents, text, lang, expected_result",
    [
        ({"en": {"Hello", "World"}}, "Hello", "en", True),  # Existing text and language
        ({"en": {"Hello", "World"}}, "Bonjour", "en", False),  # Non-existing text in existing language
        ({"en": {"Hello", "World"}}, "Hello", "fr", False),  # Valid text in non-existing language
        ({"en": {"", "World"}}, "", "en", True),  # Empty text in existing language
        ({"": {"Hello"}}, "Hello", "", True),  # Valid text in empty language code
        ({"": {""}}, "", "", True),  # Both text and language are empty
        ({"de": {"Fenster", "Tür"}}, "Tür", "de", True),  # Text with special character in existing language
        ({"ru": {"Привет", "Мир"}}, "Привет", "ru", True),  # Cyrillic text in existing language
        # Verifying case-insensitive language code handling
        ({"en": {"Hello", "World"}}, "Hello", "EN", True),
        ({"EN": {"Hello", "World"}}, "Hello", "en", True),
        ({"en": {"", "World"}}, "", "EN", True),
        ({"en-GB": {"Cheers", "Mate"}}, "Cheers", "EN-gb", True),
        ({"EN-gb": {"Cheers", "Mate"}}, "Cheers", "en-GB", True),
        # Testing with non-standard but valid language codes
        ({"en-GB": {"Cheers"}}, "Cheers", "en-GB", True),
        ({"zh-Hans-CN": {"你好"}}, "你好", "zh-Hans-CN", True),
        # Testing with mixed-case text
        ({"en": {"hello", "world"}}, "Hello", "en", False),
        # Testing with leading and trailing spaces in text
        ({"en": {"  hello  ", "world"}}, "  hello  ", "en", True),
        ({"en": {"hello", "world"}}, " hello ", "en", False),
    ],
)
def test_contains_entry_various_scenarios(initial_contents, text, lang, expected_result):
    """
    Test the `contains_entry` method with various text and language combinations to verify if a specific
    entry exists within the MultiLangString instance.

    :param initial_contents: The initial dictionary contents of the MultiLangString instance.
    :param text: The text to check for existence.
    :param lang: The language of the text to check for.
    :param expected_result: The expected boolean result indicating if the text exists in the given language.
    """
    mls = MultiLangString(mls_dict=initial_contents)
    assert (
        mls.contains_entry(text, lang) == expected_result
    ), f"Expected {expected_result} for text '{text}' in language '{lang}'."


@pytest.mark.parametrize(
    "text, lang",
    [
        (None, "en"),
        ("Hello", None),
        (None, None),
    ],
)
def test_contains_entry_with_none(text, lang):
    mls = MultiLangString({"en": {"Hello"}})
    with pytest.raises(TypeError, match="Argument '.+' must be of type 'str', but got"):
        mls.contains_entry(text, lang)


@pytest.mark.parametrize(
    "text, lang, expected_result",
    [
        ("Hello", "xx-klingon", True),  # Assuming "xx-klingon" is a valid but unusual language code
    ],
)
def test_contains_entry_with_unusual_language_codes(text, lang, expected_result):
    mls = MultiLangString({"xx-klingon": {"Hello"}})
    assert mls.contains_entry(text, lang) == expected_result, "Method did not correctly handle unusual language codes."


@pytest.mark.parametrize(
    "flag_state, text, lang, expected_result",
    [
        # Test with CLEAR_EMPTY_LANG flag set to False
        (False, "Hello", "en", True),
        # Test with CLEAR_EMPTY_LANG flag set to True
        (True, "Hello", "en", True),
    ],
)
def test_contains_entry_with_clear_empty_lang_flag(flag_state, text, lang, expected_result):
    """
    Test the `contains_entry` method with the CLEAR_EMPTY_LANG flag set to various states to ensure it does not affect the outcome.

    :param flag_state: The state to set for the CLEAR_EMPTY_LANG flag.
    :param text: The text to check for in the MultiLangString.
    :param lang: The language under which to check for the text.
    :param expected_result: The expected result of the contains_entry check.
    """
    Controller.set_flag(MultiLangStringFlag.CLEAR_EMPTY_LANG, flag_state)
    mls = MultiLangString({"en": {"Hello", "World"}})
    assert (
        mls.contains_entry(text, lang) == expected_result
    ), f"contains_entry did not return expected result with CLEAR_EMPTY_LANG flag set to {flag_state}."