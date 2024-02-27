from typing import Any
from typing import Optional

import pytest

from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "lang, expected_output, default",
    [
        ("en", SetLangString(texts={"Hello", "World"}, lang="en"), None),
        ("fr", SetLangString(texts=set(), lang="fr"), SetLangString(texts=set(), lang="fr")),
        ("es", None, "Default case when language does not exist"),
        ("", None, None),  # Testing with empty language code
    ],
)
def test_get_setlangstring_valid_cases(lang: str, expected_output: Optional[SetLangString], default: Any) -> None:
    """Test get_setlangstring method with various valid input cases.

    :param lang: The language code to search the texts in.
    :param expected_output: The expected SetLangString output or None if not found.
    :param default: The default value to return if the language does not exist.
    :return: None
    """
    input_dict = {"en": {"Hello", "World"}, "de": {"Hallo", "Welt"}}
    mls = MultiLangString(input_dict)
    result = mls.get_setlangstring(lang=lang, default=default)
    assert result == expected_output or (
        isinstance(result, str) and result == default
    ), f"Expected {expected_output} for lang '{lang}', got {result}"


@pytest.mark.parametrize(
    "lang, default",
    [
        (123, TypeError("Language code must be a string")),
        ([], TypeError("Language code must be a string")),
        ("nonexistent", "No texts found for language and no default provided"),  # Providing a string as default
        ("nonexistent", []),  # Providing a list as default
        ("nonexistent", {}),  # Providing a dict as default
        ("upperCASE", None),  # Testing case sensitivity in language codes
        ("trimmed ", None),  # Lang code with trailing space
    ],
)
def test_get_setlangstring_edge_cases(lang: Any, default: Any) -> None:
    """Test get_setlangstring with edge cases, including invalid language types and unusual defaults.

    :param lang: The language code, which might be invalid or nonexistent.
    :param default: The default value to return if the language does not exist or the input type is invalid.
    """
    input_dict = {"en": {"Hello"}}
    mls = MultiLangString(input_dict)
    if isinstance(default, TypeError):
        with pytest.raises(TypeError, match="Invalid argument 'lang' received. Expected 'str', got"):
            mls.get_setlangstring(lang=lang, default=default)
    else:
        result = mls.get_setlangstring(lang=lang, default=default)
        assert result == default, f"Expected default {default} for lang '{lang}', got {result}"


@pytest.mark.parametrize(
    "lang, default, expected_type, expected_texts",
    [
        ("en", None, SetLangString, {"Hello", "World"}),  # Existing language
        ("de", "Default Value", str, "Default Value"),  # Non-existing language with string default
        ("es", [], list, []),  # Non-existing language with list default
        ("", None, type(None), None),  # Empty language code
    ],
)
def test_get_setlangstring_cases(lang: Any, default: Any, expected_type: Any, expected_texts: Any) -> None:
    """Test the get_setlangstring method for various scenarios including valid and invalid inputs.

    :param lang: The language code to retrieve SetLangString for.
    :param default: Default value to return if language not found.
    :param expected_type: The expected type of the result.
    :param expected_texts: The expected texts or default value.
    """
    input_dict = {"en": {"Hello", "World"}, "fr": {"Bonjour", "Salut"}}
    mls = MultiLangString(input_dict)
    result = mls.get_setlangstring(lang=lang, default=default)

    if isinstance(result, expected_type):
        assert isinstance(result, expected_type), f"Expected result type {expected_type}, got {type(result)}"
        if expected_type == SetLangString:
            assert result.texts == expected_texts, f"Expected texts {expected_texts}, got {result.texts}"
    else:
        with pytest.raises(default, match="Language code must be a string"):
            mls.get_setlangstring(lang=lang, default=default)


@pytest.mark.parametrize(
    "lang, expected_exception",
    [
        (123, TypeError),
    ],
)
def test_get_setlangstring_invalid_lang_type(lang: Any, expected_exception: Any) -> None:
    """Test get_setlangstring with invalid types for the lang parameter.

    :param lang: The language code, which might be invalid.
    :param expected_exception: The expected exception to be raised.
    """
    input_dict = {"en": {"Hello", "World"}}
    mls = MultiLangString(input_dict)
    with pytest.raises(expected_exception, match="Invalid argument 'lang' received. Expected 'str', got 'int'."):
        mls.get_setlangstring(lang=lang, default=None)


@pytest.mark.parametrize(
    "lang, default, expected_result",
    [
        ("", None, None),  # Empty lang code with no default provided
        ("non-existent", [], []),  # Non-existent language with an empty list as default
        ("non-existent", {}, {}),  # Non-existent language with an empty dict as default
    ],
)
def test_get_setlangstring_special_defaults(lang: Optional[str], default: Any, expected_result: Any) -> None:
    """Test get_setlangstring with special default values for non-existent languages.

    :param lang: The language code to retrieve texts for.
    :param default: Special default values including None, empty list, and empty dict.
    :param expected_result: Expected result based on the default provided.
    """
    input_dict = {"en": {"Hello"}}
    mls = MultiLangString(input_dict)
    result = mls.get_setlangstring(lang=lang, default=default)
    assert (
        result == expected_result
    ), f"Expected {expected_result} for lang '{lang}' with default {default}, got {result}"


@pytest.mark.parametrize(
    "lang, expected_exception, match_message",
    [
        (None, TypeError, "Invalid argument 'lang' received. Expected 'str', got 'NoneType'"),
    ],
)
def test_get_setlangstring_with_none_lang_type(
    lang: Optional[str], expected_exception: Any, match_message: str
) -> None:
    """Test get_setlangstring method handling None as language code.

    :param lang: The language code, which is None for this test case.
    :param expected_exception: The type of exception expected to be raised.
    :param match_message: The message expected to be part of the raised exception.
    """
    input_dict = {"en": {"Hello"}}
    mls = MultiLangString(input_dict)
    with pytest.raises(expected_exception, match=match_message):
        mls.get_setlangstring(lang=lang, default=None)
