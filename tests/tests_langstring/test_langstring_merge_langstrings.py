import pytest

from langstring import LangString
from tests.conftest import TYPEERROR_MSG_SINGULAR


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Adjusted test cases for individual strings instead of sets
        ([LangString("a", "EN"), LangString("a", "en")], [LangString("a", "en")]),
        ([LangString("a", "EN"), LangString("a", "EN")], [LangString("a", "EN")]),
        ([LangString("hello", "En"), LangString("hello", "EN")], [LangString("hello", "en")]),
        (
            [LangString("hello", "EN"), LangString("world", "EN")],
            [LangString("hello", "EN"), LangString("world", "EN")],
        ),
        ([LangString(" Καλημέρα", "en")], [LangString(" Καλημέρα", "en")]),  # Spaces before, Greek characters
        (
            [LangString("🚀", "emoji"), LangString("🌟", "emoji")],
            [LangString("🚀", "emoji"), LangString("🌟", "emoji")],
        ),  # Emojis
        (
            [LangString("data", " DE "), LangString("science", " de ")],
            [LangString("data", " de "), LangString("science", " de ")],
        ),  # Spaces in lang
        (
            [LangString("Привет", "ru"), LangString("Мир", "RU")],
            [LangString("Привет", "ru"), LangString("Мир", "ru")],
        ),  # Cyrillic
        (
            [LangString("!@#$%^&*()", "spec"), LangString("{}[]:;\"'<>?,./", "spec")],
            [LangString("!@#$%^&*()", "spec"), LangString("{}[]:;\"'<>?,./", "spec")],
        ),  # Special chars
        (
            [LangString("hello", ""), LangString("world", "")],
            [LangString("hello", ""), LangString("world", "")],
        ),  # Empty lang value
        (
            [LangString("A", "en"), LangString("a", "en")],
            [LangString("A", "en"), LangString("a", "en")],
        ),  # Case sensitivity in content
        (
            [LangString("hello", "en"), LangString("HELLO", "en")],
            [LangString("hello", "en"), LangString("HELLO", "en")],
        ),  # Different content, same lang
    ],
)
def test_merge_langstrings_success(input_data, expected_output):
    """Adapted test to verify merge_langstrings successfully merges LangStrings with different or same case language tags."""
    result = LangString.merge_langstrings(input_data)
    assert result == expected_output, "Expected merged LangString instances did not match actual result."


@pytest.mark.parametrize(
    "invalid_input",
    [
        # Incorrect types, not LangString instance
        ([{"a"}, "EN"]),
        ("Not a list",),
        ([LangString("a", "en"), "Random String"]),  # Mixed with incorrect type
    ],
)
def test_merge_langstrings_type_error(invalid_input):
    """Test `merge_langstrings` raises TypeError with invalid input types."""
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        LangString.merge_langstrings(invalid_input)


def test_merge_langstrings_empty_input():
    """Test `merge_langstrings` with an empty list input returns an empty list."""
    result = LangString.merge_langstrings([])
    assert result == [], "Expected empty list as output when merging an empty input list."


@pytest.mark.parametrize(
    "input_data",
    [
        (None),
        ([None]),
    ],
)
def test_merge_langstrings_null_input(input_data):
    """Test merge_langstrings handling of null inputs."""
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        LangString.merge_langstrings(input_data)
