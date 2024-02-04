import pytest

from langstring import Converter
from langstring import LangString


@pytest.mark.parametrize(
    "input_strings, lang, expected_results",
    [
        ({"Hello", "World"}, "en", [("Hello", "en"), ("World", "en")]),
        (set(), "en", []),
        ({"😀", "🌍"}, "emoji", [("😀", "emoji"), ("🌍", "emoji")]),
        ({"Привет", "Мир"}, "ru", [("Привет", "ru"), ("Мир", "ru")]),
        ({"Γειά", "Κόσμος"}, "el", [("Γειά", "el"), ("Κόσμος", "el")]),
        ({" Hello ", " World "}, "en", [(" Hello ", "en"), (" World ", "en")]),
        ({"Hello", "World"}, "EN", [("Hello", "EN"), ("World", "EN")]),
        ({"こんにちは", "世界"}, "ja", [("こんにちは", "ja"), ("世界", "ja")]),
        ({"123", "456"}, "num", [("123", "num"), ("456", "num")]),
        ({"Hello!", "World?"}, "en", [("Hello!", "en"), ("World?", "en")]),
        (
            {"This is a very long string indeed to test the edge case scenario.", "Another long string to test."},
            "en",
            [
                ("This is a very long string indeed to test the edge case scenario.", "en"),
                ("Another long string to test.", "en"),
            ],
        ),
        ({" Καλημέρα ", " Κόσμος "}, "el", [(" Καλημέρα ", "el"), (" Κόσμος ", "el")]),
        ({"HELLO", "world"}, "en", [("HELLO", "en"), ("world", "en")]),
    ],
)
def test_from_strings_to_langstrings_valid(input_strings, lang, expected_results):
    results = Converter.from_strings_to_langstrings(input_strings, lang)
    assert len(results) == len(expected_results), "The number of results does not match the expected number."
    # Sorting results and expected_results to ensure matching order for comparison
    sorted_results = sorted(results, key=lambda x: x.text)
    sorted_expected = sorted(expected_results, key=lambda x: x[0])
    for result, (expected_text, expected_lang) in zip(sorted_results, sorted_expected):
        assert isinstance(result, LangString), "The result is not an instance of LangString."
        assert result.text == expected_text, "The text of the LangString does not match the expected text."
        assert result.lang == expected_lang, "The language of the LangString does not match the expected language."


@pytest.mark.parametrize(
    "input_strings, lang",
    [
        (None, "en"),  # Null input
        (123, "en"),  # Invalid type: integer
        ("string", "en"),  # Invalid type: string
        ({"Hello", 123}, "en"),  # Invalid value type within set
    ],
)
def test_from_strings_to_langstrings_invalid_input(input_strings, lang):
    with pytest.raises(TypeError):
        Converter.from_strings_to_langstrings(input_strings, lang)


@pytest.mark.parametrize(
    "input_strings, lang",
    [
        ({"Hello", "World"}, None),  # Null lang
        ({"Hello", "World"}, 123),  # Invalid type for lang
        ({"Hello", "World"}, {}),
    ],
)
def test_from_strings_to_langstrings_invalid_lang(input_strings, lang):
    with pytest.raises(TypeError):
        Converter.from_strings_to_langstrings(input_strings, lang)


@pytest.mark.parametrize(
    "input_strings, lang, expected_results",
    [
        ({" ", "  "}, "en", [(" ", "en"), ("  ", "en")]),  # Strings that are only whitespace
    ],
)
def test_from_strings_to_langstrings_unusual_valid(input_strings, lang, expected_results):
    results = Converter.from_strings_to_langstrings(input_strings, lang)
    assert len(results) == len(expected_results), "Mismatch in number of results for unusual but valid inputs."
