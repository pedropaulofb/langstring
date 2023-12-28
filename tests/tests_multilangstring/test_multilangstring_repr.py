import pytest

from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString
from tests.tests_multilangstring.sample_multilangstring import create_sample_multilangstring


def test_repr_basic_representation() -> None:
    """Check the representation of a standard MultiLangString with multiple languages."""
    multi_lang_string = create_sample_multilangstring()
    expected_repr = (
        "MultiLangString({'en': ['Hello'], 'fr': ['Bonjour'], 'de': ['Hallo']}, control='ALLOW', preferred_lang='en')"
    )
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_with_preferred_lang() -> None:
    """Check the representation when a preferred language is set."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), preferred_lang="en")
    expected_repr = "MultiLangString({'en': ['Hello']}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_empty_multilangstring() -> None:
    """Check the representation of a MultiLangString with no LangStrings."""
    multi_lang_string = MultiLangString()
    expected_repr = "MultiLangString({}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_with_control() -> None:
    """Check the representation when a specific control flag is set."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), control="OVERWRITE")
    expected_repr = "MultiLangString({'en': ['Hello']}, control='OVERWRITE', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_invalid_langstrings_type() -> None:
    """Ensure a TypeError is raised if the provided mls_dict are not in dictionary format."""
    with pytest.raises(TypeError):
        MultiLangString(["Hello", "Bonjour"])


def test_repr_invalid_control_value() -> None:
    """Ensure a ValueError is raised if an unrecognized control value is provided."""
    with pytest.raises(ValueError):
        MultiLangString(LangString("Hello", "en"), control="INVALID")


def test_repr_invalid_preferred_lang_type() -> None:
    """Ensure a TypeError is raised if preferred_lang is not a string."""
    with pytest.raises(TypeError):
        MultiLangString(LangString("Hello", "en"), preferred_lang=123)


def test_repr_long_value() -> None:
    """Check the representation of a MultiLangString with a long string value."""
    long_string = "Hello " * 1000
    multi_lang_string = MultiLangString(LangString(long_string, "en"))
    expected_repr = f"MultiLangString({{{repr('en')}: {repr([long_string])}}}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_special_characters() -> None:
    """Check the representation of a MultiLangString with special characters."""
    special_value = "Hello\nWorld\"!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    multi_lang_string = MultiLangString(LangString(special_value, "en"))
    expected_repr = f"MultiLangString({{{repr('en')}: {repr([special_value])}}}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_unicode_characters() -> None:
    """Check the representation of a MultiLangString containing Unicode characters."""
    unicode_value = "こんにちは世界"
    multi_lang_string = MultiLangString(LangString(unicode_value, "ja"))
    expected_repr = f"MultiLangString({{{repr('ja')}: {repr([unicode_value])}}}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_empty_langstring() -> None:
    """Check the representation of a MultiLangString with an empty LangString."""
    multi_lang_string = MultiLangString(LangString("", "en"))
    expected_repr = "MultiLangString({'en': ['']}, control='ALLOW', preferred_lang='en')"
    assert repr(multi_lang_string) == expected_repr, f"Got {repr(multi_lang_string)}, expected {expected_repr}"


def test_repr_invalid_language_code() -> None:
    """Ensure a ValueError is raised for invalid language codes."""
    with pytest.raises(TypeError):
        MultiLangString(LangString("Hello", 123))


def test_repr_multiple_langstrings() -> None:
    """Check the representation of a MultiLangString with a large number of LangStrings."""
    # Create a list of LangString objects
    langstrings = [LangString(f"string{i}", f"lang{i}") for i in range(100)]
    multi_lang_string = MultiLangString(*langstrings)

    # Create the expected representation
    multiple_entries_repr = {f"lang{i}": [f"string{i}"] for i in range(100)}
    expected_repr = f"MultiLangString({multiple_entries_repr}, control='ALLOW', preferred_lang='en')"

    # Assert the actual representation matches the expected representation
    assert (
        repr(multi_lang_string) == expected_repr
    ), f"Expected representation '{expected_repr}' but got '{repr(multi_lang_string)}'."
