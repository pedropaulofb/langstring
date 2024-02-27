from typing import Any
from typing import Optional

import pytest

from langstring import LangString
from langstring import MultiLangString


@pytest.mark.parametrize(
    "input_dict, text, lang, expected_output",
    [
        ({"en": {"Hello", "World"}, "fr": {"Bonjour"}}, "Hello", "en", LangString(text="Hello", lang="en")),
        ({"en": {"Hello", "World"}, "fr": {"Bonjour", "Monde"}}, "Monde", "fr", LangString(text="Monde", lang="fr")),
        ({"en": {"Hello"}, "fr": {"Bonjour"}}, "Hola", "es", None),
        ({"en": {"Hello"}, "fr": {"Bonjour"}}, "Hello", "fr", None),
        ({"ru": {"Привет"}}, "Привет", "ru", LangString(text="Привет", lang="ru")),
        ({"emoji": {"😊", "😂"}}, "😊", "emoji", LangString(text="😊", lang="emoji")),
        ({"en": {" "}}, " ", "en", LangString(text=" ", lang="en")),  # Testing with whitespace
        (
            {"gr": {"Γειά σου"}},
            "Γειά σου",
            "gr",
            LangString(text="Γειά σου", lang="gr"),
        ),  # Non-Latin characters (Greek)
        ({"cy": {"Привет"}}, "Привет", "cy", LangString(text="Привет", lang="cy")),  # Cyrillic characters
        ({"special": {"@#$%"}}, "@#$%", "special", LangString(text="@#$%", lang="special")),  # Special characters
    ],
)
def test_get_langstring_valid_cases(
    input_dict: dict, text: str, lang: str, expected_output: Optional[LangString]
) -> None:
    """Test get_langstring method with various valid input cases.

    :param input_dict: A dictionary to initialize MultiLangString with language keys and sets of texts.
    :param text: The text to search for within a specific language.
    :param lang: The language code to search the text in.
    :param expected_output: The expected LangString output or None if not found.
    :return: None
    """
    mls = MultiLangString(input_dict)
    result = mls.get_langstring(text=text, lang=lang)
    assert result == expected_output, f"Expected {expected_output} for text '{text}' in lang '{lang}', got {result}"


@pytest.mark.parametrize(
    "text, lang, default, expected_output",
    [
        ("NonExistent", "en", LangString(text="Default", lang="en"), LangString(text="Default", lang="en")),
        ("NonExistent", "en", "DefaultText", "DefaultText"),
        ("NonExistent", "en", None, None),
        ("NonExistent", "en", [], []),  # Testing with an empty list as default
        ("NonExistent", "en", {}, {}),  # Testing with an empty dict as default
        ("NonExistent", "en", True, True),  # Testing with a boolean True as default
        ("NonExistent", "en", False, False),  # Testing with a boolean False as default
    ],
)
def test_get_langstring_with_default(text: str, lang: str, default: Any, expected_output: Optional[LangString]) -> None:
    """Test get_langstring method with a default value for non-existing text.

    :param text: The text to search for within a specific language.
    :param lang: The language code to search the text in.
    :param default: The default value to return if the text is not found.
    :param expected_output: The expected output, either a LangString or the default value.
    :return: None
    """
    mls = MultiLangString({"en": {"Hello"}})
    result = mls.get_langstring(text=text, lang=lang, default=default)
    assert (
        result == expected_output
    ), f"Expected {expected_output} as default for text '{text}' in lang '{lang}', got {result}"


@pytest.mark.parametrize(
    "lang, text",
    [
        ("en", None),
        (None, "Hello"),
        (123, "Hello"),
        ("en", 123),
    ],
)
def test_get_langstring_invalid_inputs(lang, text) -> None:
    """Test get_langstring with invalid types and values for lang and text parameters.

    :param lang: The language code, which might be invalid.
    :param text: The text to search for, which might be invalid.
    """
    mls = MultiLangString({"en": {"Hello"}})
    with pytest.raises(TypeError, match="Invalid argument .+ received. Expected 'str', got"):
        mls.get_langstring(text=text, lang=lang)


@pytest.mark.parametrize(
    "input_dict, text, lang, expected_output",
    [
        (
            {"mixedCase": {"HelloWorld"}},
            "HelloWorld",
            "mixedCase",
            LangString(text="HelloWorld", lang="mixedCase"),
        ),  # Mixed case lang
        ({"": {"emptyKey"}}, "emptyKey", "", LangString(text="emptyKey", lang="")),  # Empty string as lang
    ],
)
def test_get_langstring_edge_cases(
    input_dict: dict, text: str, lang: str, expected_output: Optional[LangString]
) -> None:
    """Test get_langstring method with edge cases including empty and mixed case language codes.

    :param input_dict: A dictionary to initialize MultiLangString with language keys and sets of texts.
    :param text: The text to search for within a specific language.
    :param lang: The language code to search the text in, which may include unusual cases like empty strings or mixed cases.
    :param expected_output: The expected LangString output or None if not found.
    :return: None
    """
    mls = MultiLangString(input_dict)
    result = mls.get_langstring(text=text, lang=lang)
    assert result == expected_output, f"Expected {expected_output} for text '{text}' in lang '{lang}', got {result}"
