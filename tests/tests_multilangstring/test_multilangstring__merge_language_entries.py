from typing import Any

import pytest

from langstring import MultiLangString


@pytest.mark.parametrize(
    "input_mls_dict,expected",
    [
        ({"en": {"Hello"}, "fr": {"Bonjour"}}, {"en": {"Hello"}, "fr": {"Bonjour"}}),
        ({"es": {"Hola"}, "de": {"Hallo"}}, {"es": {"Hola"}, "de": {"Hallo"}}),
        ({"EN": {"HELLO"}, "en": {"Hello"}}, {"EN": {"HELLO", "Hello"}}),
        ({"en": {"Hello, world!"}, "fr": {"Bonjour, monde!"}}, {"en": {"Hello, world!"}, "fr": {"Bonjour, monde!"}}),
        ({"en": {" Hello "}, "fr": {" Bonjour "}}, {"en": {" Hello "}, "fr": {" Bonjour "}}),
        ({"en": {"Hello", "Hi"}, "EN": {"Greetings"}}, {"en": {"Hello", "Hi", "Greetings"}}),
        ({}, {}),
        ({"en": set(), "fr": set()}, {"en": set(), "fr": set()}),
        ({"en": {"Hello"}, "en": {"Hello"}}, {"en": {"Hello"}}),
        # Multiple casing
        (
            {"En": {"Hello"}, "FR": {"Bonjour"}, "en": {"hello"}, "fr": {"bonjour"}},
            {"En": {"Hello", "hello"}, "FR": {"Bonjour", "bonjour"}},
        ),
        # Different char sets (Cyrillic, Greek, Chinese)
        ({"ru": {"Привет"}, "el": {"Γειά"}, "zh": {"你好"}}, {"ru": {"Привет"}, "el": {"Γειά"}, "zh": {"你好"}}),
        # Different spacing
        ({"en": {"  Hello  "}, "fr": {"  Bonjour  "}}, {"en": {"  Hello  "}, "fr": {"  Bonjour  "}}),
        # Special chars
        (
            {"en": {"Hello!"}, "fr": {"Bonjour?"}, "es": {"¡Hola!"}, "de": {"Guten Tag."}},
            {"en": {"Hello!"}, "fr": {"Bonjour?"}, "es": {"¡Hola!"}, "de": {"Guten Tag."}},
        ),
        # Mixed casing, char sets, spacing, and special chars
        (
            {
                "EN": {"HELLO", "HELLO!"},
                "en": {"hello", "hello?"},
                "fr": {"  Bonjour  ", "Bonjour?"},
                "zh": {"  你好  ", "你好!"},
            },
            {
                "EN": {"HELLO", "HELLO!", "hello", "hello?"},
                "fr": {"  Bonjour  ", "Bonjour?"},
                "zh": {"  你好  ", "你好!"},
            },
        ),
    ],
)
def test_merge_with_non_overlapping_keys(input_mls_dict: dict[str, Any], expected: dict[str, Any]) -> None:
    """
    Test _merge_language_entries with dictionaries having non-overlapping keys.

    :param input_mls_dict: First input dictionary to merge.
    :param dict_b: Second input dictionary to merge, with no overlapping keys with input_mls_dict.
    :param expected: The expected result of merging input_mls_dict and dict_b.
    :return: None
    :raises: AssertionError if the merged result does not correctly include all entries from both dictionaries.
    """
    mls = MultiLangString()
    result = mls._merge_language_entries(input_mls_dict)
    assert result == expected, f"Merging {input_mls_dict} failed to produce {expected}."


@pytest.mark.parametrize(
    "input_mls_dict,exception_message",
    [
        (["en"], ".+ object has no attribute 'keys'"),
        ("not a dict", ".+ object has no attribute 'keys'"),
        (12345, ".+ object has no attribute 'keys'"),
        (None, ".+ object has no attribute 'keys'"),
        ({"str"}, ".+ object has no attribute 'keys'"),
    ],
)
def test_merge_with_invalid_input_types(input_mls_dict: Any, exception_message: str) -> None:
    """
    Test _merge_language_entries with invalid input types to ensure it raises TypeError.

    :param input_mls_dict: First input to the merge function, potentially invalid type.
    :param dict_b: Second input to the merge function, potentially invalid type.
    :param exception_message: Expected exception message for the TypeError.
    :return: None
    :raises: TypeError if input types are not dictionaries.
    """
    mls = MultiLangString()
    with pytest.raises(AttributeError, match=exception_message):
        mls._merge_language_entries(input_mls_dict)
