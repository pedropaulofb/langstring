import pytest

from langstring.langstring import LangString


@pytest.mark.parametrize(
    "text, lang, expected_text",
    [
        ("hello world", "en", "Hello world"),
        ("HELLO WORLD", "en", "Hello world"),
        ("123 hello", "en", "123 hello"),
        ("", "en", ""),
        ("bonjour", "fr", "Bonjour"),
        ("你好", "zh", "你好"),  # Non-Latin script
    ],
)
def test_capitalize_basic(text, lang, expected_text):
    """Test the capitalize method for basic usage."""
    lang_str = LangString(text, lang)
    result = lang_str.capitalize()
    assert (
        result.text == expected_text and result.lang == lang
    ), "capitalize should correctly capitalize the text while preserving the language tag"


@pytest.mark.parametrize(
    "text, lang",
    [
        (" hello world ", "en"),
        ("  hello world  ", "en"),
        ("hello world ", "en"),
    ],
)
def test_capitalize_with_whitespace(text, lang):
    """Test the capitalize method with leading and trailing whitespaces in the text."""
    lang_str = LangString(text, lang)
    result = lang_str.capitalize()
    assert (
        result.text == text.capitalize() and result.lang == lang
    ), "capitalize should handle whitespaces correctly while preserving the language tag"


@pytest.mark.parametrize(
    "text, lang",
    [
        (None, "en"),
        (123, "en"),
        ([], "en"),
    ],
)
def test_capitalize_invalid_text(text, lang):
    """Test the capitalize method with invalid text inputs."""
    with pytest.raises(TypeError, match="Expected 'str', got"):
        LangString(text, lang).capitalize()


@pytest.mark.parametrize(
    "text, lang",
    [
        ("hello world", "en"),
        ("hola mundo", "es"),
        ("bonjour le monde", "fr"),
    ],
)
def test_capitalize_different_lang_tags(text, lang):
    """Test the capitalize method with different language tags."""
    lang_str = LangString(text, lang)
    result = lang_str.capitalize()
    assert (
        result.text == text.capitalize() and result.lang == lang
    ), "capitalize should correctly capitalize the text while preserving different language tags"


@pytest.mark.parametrize("lang", ["en", "es", "fr"])
def test_capitalize_empty_string(lang):
    """Test the capitalize method with an empty string."""
    lang_str = LangString("", lang)
    result = lang_str.capitalize()
    assert (
        result.text == "" and result.lang == lang
    ), "capitalize should return an empty string with the same language tag for an empty LangString"


@pytest.mark.parametrize("text, lang", [("hello world", "en"), ("hola mundo", "es")])
def test_capitalize_does_not_modify_original(text, lang):
    """Test that the capitalize method does not modify the original LangString object."""
    lang_str = LangString(text, lang)
    _ = lang_str.capitalize()
    assert (
        lang_str.text == text and lang_str.lang == lang
    ), "capitalize should not modify the original LangString object"
