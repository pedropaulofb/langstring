import pytest

from langstring import MultiLangString
from tests.conftest import TYPEERROR_MSG_SINGULAR


@pytest.mark.parametrize(
    "text, lang, expected_exception ",
    [
        (123, "en", TypeError),
        ("123", "en", ValueError),
        ("hello", 123, TypeError),
        (" hello", "en", ValueError),
        ("Hello", "en", ValueError),
        ("hello", " en", ValueError),
        ("hello", "", ValueError),
    ],
)
def test_remove_entry_exceptions(text, lang, expected_exception):
    """
    Test remove_entry method raises expected exceptions with corresponding messages for invalid inputs or when an entry does not exist.

    :param text: Text of the entry to be removed.
    :param lang: Language of the entry to be removed.
    :param expected_exception: Expected exception type.
    :param expected_message: Expected error message.
    """
    mls = MultiLangString({"en": {"hello", "world"}})
    with pytest.raises(expected_exception, match=TYPEERROR_MSG_SINGULAR):
        mls.remove_entry(text, lang)


@pytest.mark.parametrize(
    "initial_contents, text_to_remove, lang_to_remove, expected_contents",
    [
        ({"en": {"hello", "world"}, "fr": {"bonjour"}}, "hello", "en", {"en": {"world"}, "fr": {"bonjour"}}),
        ({"en": {"hello", "world"}, "fr": {"bonjour"}}, "hello", "En", {"en": {"world"}, "fr": {"bonjour"}}),
        ({"en": {"hello", "world"}, "fr": {"bonjour"}}, "hello", "EN", {"en": {"world"}, "fr": {"bonjour"}}),
        ({"en": {"hello"}, "fr": {"bonjour"}}, "hello", "en", {"en": set(), "fr": {"bonjour"}}),
        (
            {"en": {"   hello   ", "world"}, "fr": {"bonjour"}},
            "   hello   ",
            "en",
            {"en": {"world"}, "fr": {"bonjour"}},
        ),
        ({"en": {"HELLO", "world"}, "fr": {"bonjour"}}, "HELLO", "en", {"en": {"world"}, "fr": {"bonjour"}}),
        ({"gr": {"Γειά"}, "ru": {"привет"}}, "Γειά", "gr", {"gr": set(), "ru": {"привет"}}),
        ({"emoji": {"👋"}}, "👋", "emoji", {"emoji": set()}),
        ({"en-special": {"hello-world"}}, "hello-world", "en-special", {"en-special": set()}),
        (
            {"ru": {"Привет", "Мир"}, "gr": {"Γεια", "Κόσμος"}},
            "Привет",
            "ru",
            {"ru": {"Мир"}, "gr": {"Γεια", "Κόσμος"}},
        ),
        ({"mixed": {"hello", "HELLO"}}, "hello", "mixed", {"mixed": {"HELLO"}}),  # Case sensitivity
        ({"spaces": {" hello ", "world"}}, " hello ", "spaces", {"spaces": {"world"}}),  # Leading/trailing spaces
        (
            {"special-chars": {"hello-world!", "hello"}},
            "hello-world!",
            "special-chars",
            {"special-chars": {"hello"}},
        ),  # Special characters
    ],
)
def test_remove_entry_content(initial_contents, text_to_remove, lang_to_remove, expected_contents):
    """
    Test remove_entry method correctly modifies the content of the MultiLangString instance.

    :param initial_contents: Initial contents of the MultiLangString.
    :param text_to_remove: Text of the entry to be removed.
    :param lang_to_remove: Language of the entry to be removed.
    :param expected_contents: Expected contents of the MultiLangString after removal.
    """
    mls = MultiLangString(initial_contents)
    mls.remove_entry(text_to_remove, lang_to_remove)
    assert (
        mls.mls_dict == expected_contents
    ), f"Expected contents after removal: {expected_contents}, got: {mls.mls_dict}"


@pytest.mark.parametrize(
    "initial_contents, lang_to_remove, expected_exception",
    [
        ({"en": {"hello", "world"}}, None, TypeError),
        ({"en": {"hello", "world"}}, "", ValueError),
    ],
)
def test_remove_entry_edge_cases_lang(initial_contents, lang_to_remove, expected_exception):
    """
    Test remove_entry method with edge cases for 'lang' parameter, such as null and empty string values.

    :param initial_contents: Initial contents of the MultiLangString.
    :param lang_to_remove: Language code to remove entry from, testing null and empty values.
    :param expected_exception: Expected exception type for edge cases.
    :param expected_message: Expected error message for edge cases.
    """
    mls = MultiLangString(initial_contents)
    with pytest.raises(expected_exception, match=TYPEERROR_MSG_SINGULAR):
        mls.remove_entry("hello", lang_to_remove)


@pytest.mark.parametrize(
    "text, lang, expected_exception",
    [
        (None, "en", TypeError),
        ("", "en", ValueError),
    ],
)
def test_remove_entry_invalid_types_and_values(text, lang, expected_exception):
    """
    Test remove_entry method handles null, empty, and invalid type parameters correctly.

    :param text: Text of the entry to be removed, testing null and empty values.
    :param lang: Language of the entry to be removed.
    :param expected_exception: Expected exception type for invalid inputs.
    :param expected_message: Expected error message for invalid inputs.
    """
    mls = MultiLangString({"en": {"hello", "world"}})
    with pytest.raises(expected_exception, match=TYPEERROR_MSG_SINGULAR):
        mls.remove_entry(text, lang)


@pytest.mark.parametrize(
    "initial_contents, text_to_remove, lang_to_remove, expected_contents",
    [
        # Correct expectations to match the class's behavior
        (
            {"gr": {"Γειά"}, "ru": {"привет"}},
            "Γειά",
            "gr",
            {"gr": set(), "ru": {"привет"}},
        ),  # gr remains with an empty set
        ({"emoji": {"👋"}}, "👋", "emoji", {"emoji": set()}),  # emoji remains with an empty set
        (
            {"en-special": {"hello-world"}},
            "hello-world",
            "en-special",
            {"en-special": set()},
        ),  # en-special remains with an empty set
    ],
)
def test_remove_entry_various_inputs(initial_contents, text_to_remove, lang_to_remove, expected_contents):
    mls = MultiLangString(initial_contents)
    mls.remove_entry(text_to_remove, lang_to_remove)
    assert (
        mls.mls_dict == expected_contents
    ), f"Expected contents after removal: {expected_contents}, got: {mls.mls_dict}"


@pytest.mark.parametrize(
    "initial_contents, text, lang, clean_empty, expected_contents",
    [
        ({"en": {"hello", "world"}, "fr": {"bonjour"}}, "world", "en", True, {"en": {"hello"}, "fr": {"bonjour"}}),
        (
            {"en": {"world"}, "fr": {"bonjour"}},
            "world",
            "en",
            True,
            {"fr": {"bonjour"}},
        ),  # en becomes empty and should be removed
        (
            {"en": {"world"}, "fr": {"bonjour"}},
            "world",
            "en",
            False,
            {"en": set(), "fr": {"bonjour"}},
        ),  # en remains but is empty
        (
            {"en": {"hello"}, "fr": {"bonjour", "salut"}},
            "bonjour",
            "fr",
            True,
            {"en": {"hello"}, "fr": {"salut"}},
        ),  # fr remains
    ],
)
def test_remove_entry_with_clean_empty(initial_contents, text, lang, clean_empty, expected_contents):
    """
    Test the `remove_entry` method with the `clean_empty` parameter affecting the final state of `mls_dict`.

    :param initial_contents: Initial contents of the MultiLangString.
    :param text: The text of the entry to be removed.
    :param lang: The language of the entry to be removed.
    :param clean_empty: Whether to remove empty language sets after removal.
    :param expected_contents: Expected state of `mls_dict` after the operation.
    """
    mls = MultiLangString(initial_contents)
    mls.remove_entry(text, lang, clean_empty=clean_empty)
    assert mls.mls_dict == expected_contents, "The `mls_dict` did not match expected contents after the operation."
