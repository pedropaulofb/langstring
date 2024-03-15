import pytest

from langstring import LangString


@pytest.mark.parametrize(
    "text, lang, print_quotes, separator, print_lang, expected",
    [
        # Regular cases
        ("Hello", "en", True, "@", True, '"Hello"@en'),
        ("Hola", "es", False, "@", True, "Hola@es"),
        ("Bonjour", "fr", True, "#", True, '"Bonjour"#fr'),
        ("Hello", "en", True, "@", False, '"Hello"'),
        # Edge cases
        ("", "", True, "@", True, '""@'),
        ("", "en", True, "@", True, '""@en'),
        ("Hello", "", True, "@", True, '"Hello"@'),
        ("Hello", "en", False, "@", True, "Hello@en"),
        ("Hello", "en", True, "", True, '"Hello"en'),
        ("Hello", "en", True, "@", False, '"Hello"'),
        # Lower and upper case
        ("hello", "EN", True, "@", True, '"hello"@EN'),
        ("HELLO", "en", True, "@", True, '"HELLO"@en'),
        # Emojis
        ("👋", "en", True, "@", True, '"👋"@en'),
        # Different charset
        ("Привет", "ru", True, "@", True, '"Привет"@ru'),
    ],
)
def test_to_string(text, lang, print_quotes, separator, print_lang, expected):
    """Test the to_string method of the LangString class.

    This test covers different combinations of text, language, print_quotes, separator, and print_lang parameters.

    :param text: The text string.
    :type text: str
    :param lang: The language tag of the text.
    :type lang: str
    :param print_quotes: Whether to print quotes around the text.
    :type print_quotes: bool
    :param separator: The separator between the text and the language tag.
    :type separator: str
    :param print_lang: Whether to print the language tag.
    :type print_lang: bool
    :param expected: The expected output of the to_string method.
    :type expected: str
    """
    ls = LangString(text, lang)
    result = ls.to_string(print_quotes, separator, print_lang)
    assert result == expected, f"Expected '{expected}', but got '{result}'"


@pytest.mark.parametrize(
    "text, lang, print_quotes, separator, print_lang, expected",
    [
        ("Hello", "en", True, None, True, TypeError),
        # Invalid types for print_quotes
        ("Hello", "en", "True", "@", True, TypeError),
        ("Hello", "en", 1, "@", True, TypeError),
        ("Hello", "en", [], "@", True, TypeError),
        ("Hello", "en", {}, "@", True, TypeError),
        # Invalid types for separator
        ("Hello", "en", True, True, True, TypeError),
        ("Hello", "en", True, 1, True, TypeError),
        ("Hello", "en", True, [], True, TypeError),
        ("Hello", "en", True, {}, True, TypeError),
        # Invalid types for print_lang
        ("Hello", "en", True, "@", "True", TypeError),
        ("Hello", "en", True, "@", 1, TypeError),
        ("Hello", "en", True, "@", [], TypeError),
        ("Hello", "en", True, "@", {}, TypeError),
    ],
)
def test_to_string_invalid_types(text, lang, print_quotes, separator, print_lang, expected):
    """Test the to_string method of the LangString class with invalid types.

    :param text: The text string.
    :type text: str
    :param lang: The language tag of the text.
    :type lang: str
    :param print_quotes: Whether to print quotes around the text.
    :type print_quotes: bool
    :param separator: The separator between the text and the language tag.
    :type separator: str
    :param print_lang: Whether to print the language tag.
    :type print_lang: bool
    :param expected: The expected output of the to_string method.
    :type expected: str
    """
    ls = LangString(text, lang)
    with pytest.raises(expected, match="Argument '.+' must be of type"):
        ls.to_string(print_quotes, separator, print_lang)
