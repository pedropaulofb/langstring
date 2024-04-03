import pytest

from langstring import Converter, LangString, MultiLangString
from tests.conftest import TYPEERROR_MSG_SINGULAR


@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        ({"en": {"Hello"}}, [LangString("Hello", "en")]),
        ({"fr": {"Bonjour"}, "de": {"Hallo"}}, [LangString("Bonjour", "fr"), LangString("Hallo", "de")]),
        ({"": {""}}, [LangString("", "")]),  # Empty language and text
        ({"en": {" "}}, [LangString(" ", "en")]),  # Text with space
        ({"ru": {"Привет"}}, [LangString("Привет", "ru")]),  # Cyrillic script
        ({"el": {"Γειά σου"}}, [LangString("Γειά σου", "el")]),  # Greek script
        ({"en": {"Hello 😊"}}, [LangString("Hello 😊", "en")]),  # Text with emoji
        ({"en": {"Hello, world!"}}, [LangString("Hello, world!", "en")]),  # Text with special characters
        ({"EN": {"HELLO"}}, [LangString("HELLO", "EN")]),  # Upper case language code
    ],
)
def test_from_multilangstring_to_langstrings_basic(input_dict, expected_output):
    """Test conversion from MultiLangString to list of LangString objects with basic inputs."""
    mls = MultiLangString(mls_dict=input_dict)
    result = Converter.from_multilangstring_to_langstrings(mls)
    assert len(result) == len(expected_output), "Number of LangStrings does not match expected"
    for langstring in expected_output:
        assert langstring in result, f"LangString {langstring} not found in result"


@pytest.mark.parametrize(
    "input_dict, filter_langs, expected_output",
    [
        ({"en": {"Hello"}, "fr": {"Bonjour"}}, ["en"], [LangString("Hello", "en")]),
        ({"fr": {"Bonjour"}, "de": {"Hallo"}}, ["fr", "de"], [LangString("Bonjour", "fr"), LangString("Hallo", "de")]),
        ({"fr": {"Bonjour"}, "de": {"Hallo"}}, ["es"], []),
        (
            {"en": {"Hello"}, "fr": {"Bonjour"}, " ": {" "}},
            ["en", "fr", " "],
            [LangString("Hello", "en"), LangString("Bonjour", "fr"), LangString(" ", " ")],
        ),  # Include empty language
        (
            {"en": {"Hello"}, "EN": {"HELLO"}},
            ["en", "EN"],
            [
                LangString("Hello", "en"),
                LangString("HELLO", "en"),
                LangString("Hello", "en"),
                LangString("HELLO", "en"),
            ],
        ),  # Case-sensitive language codes
        ({"en": {"  Hello  "}}, ["en"], [LangString("  Hello  ", "en")]),  # Text with leading and trailing spaces
        ({"en": {"Hello\nWorld"}}, ["en"], [LangString("Hello\nWorld", "en")]),  # Text with newline character
        (
            {"es": {"Hola"}, "es-ES": {"Hola, mundo"}},
            ["es", "es-ES"],
            [LangString("Hola", "es"), LangString("Hola, mundo", "es-ES")],
        ),  # Language tag with subtags
    ],
)
def test_from_multilangstring_to_langstrings_with_language_filter(input_dict, filter_langs, expected_output):
    """Test conversion from MultiLangString to list of LangString objects with language filtering."""
    mls = MultiLangString(mls_dict=input_dict)
    result = Converter.from_multilangstring_to_langstrings(mls, languages=filter_langs)
    assert len(result) == len(expected_output), "Number of LangStrings after filtering does not match expected"
    for langstring in expected_output:
        assert langstring in result, f"Filtered LangString {langstring} not found in result"


def test_from_multilangstring_to_langstrings_empty():
    """Test conversion from an empty MultiLangString."""
    mls = MultiLangString()
    result = Converter.from_multilangstring_to_langstrings(mls)
    assert result == [], "Result is not an empty list for an empty MultiLangString"


@pytest.mark.parametrize(
    "invalid_input",
    [
        (123),
        ("not a MultiLangString"),
        ([LangString("Hello", "en")]),
        (None, "Expected 'MultiLangString', got 'NoneType'"),  # None as input
        ({"en": "Hello"}, "Expected 'MultiLangString', got 'dict'"),  # Incorrectly formed dict
        (LangString("Hello", "en"), "Expected 'MultiLangString', got 'LangString'"),  # LangString instance
    ],
)
def test_from_multilangstring_to_langstrings_invalid_input_type(invalid_input):
    """Test conversion with invalid input types."""
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        Converter.from_multilangstring_to_langstrings(invalid_input)


@pytest.mark.parametrize(
    "invalid_language_filter",
    [
        123,
        "not a list",
        {"lang": "en"},
        True,
        5.5,
        [123],
        [None],
    ],
)
def test_from_multilangstring_to_langstrings_invalid_language_filter(invalid_language_filter):
    """Test conversion with various invalid language filter types."""
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        Converter.from_multilangstring_to_langstrings(mls, languages=invalid_language_filter)


def test_from_multilangstring_to_langstrings_default_behavior():
    mls = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    result = Converter.from_multilangstring_to_langstrings(mls)
    assert len(result) == 2, "Expected default behavior to include all languages"


@pytest.mark.parametrize("languages", [None, []])
def test_from_multilangstring_to_langstrings_null_languages(languages):
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    result = Converter.from_multilangstring_to_langstrings(mls, languages=languages)
    if languages is None:
        assert len(result) == 1, "Passing None as languages should include all languages"
    else:
        assert len(result) == 0, "Passing empty list as languages should include any languages"


@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        ({"": {""}}, [LangString("", "")]),  # Edge case: empty text and language
        ({"en-GB": {"Colour"}, "en-US": {"Color"}}, [LangString("Colour", "en-GB"), LangString("Color", "en-US")]),
    ],
)
def test_from_multilangstring_to_langstrings_edge_cases(input_dict, expected_output):
    mls = MultiLangString(mls_dict=input_dict)
    result = Converter.from_multilangstring_to_langstrings(mls)
    assert len(result) == len(expected_output), "Edge cases not handled correctly"
