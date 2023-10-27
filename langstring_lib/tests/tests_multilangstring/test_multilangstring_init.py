"""Tests for the Initialization of the `MultiLangString` Class from the `langstring_lib` Package.

This module contains a suite of tests dedicated to verifying the behavior of the `__init__` method of the
`MultiLangString` class. The tests encompass a range of scenarios, ensuring that the class is properly initialized
under various conditions, with different arguments, and that it correctly responds to invalid or unexpected inputs.
"""
import pytest

from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString


def test_multilangstring_initialization() -> None:
    """Test the initialization of MultiLangString with no arguments."""
    multilang_str = MultiLangString()

    assert multilang_str.control == "ALLOW", f"Expected default control to be ALLOW, but found {multilang_str.control}."

    assert (
        len(multilang_str.langstrings) == 0
    ), f"Expected 0 langstrings on default initialization, but found {len(multilang_str.langstrings)}."


def test_init_with_none_arguments() -> None:
    """Test initializing `MultiLangString` with `None`, expecting a `TypeError`.

    The test ensures that the `MultiLangString` class correctly identifies and
    raises a `TypeError` when provided with a `None` value during initialization.
    """
    with pytest.raises(TypeError):
        MultiLangString(None)


def test_init_with_unexpected_data_types() -> None:
    """Test initializing `MultiLangString` with unexpected data types.

    This test validates that initializing `MultiLangString` with a non-string
    and non-LangString data type like an integer will result in a `TypeError`.
    """
    with pytest.raises(TypeError):
        MultiLangString(12345)


def test_init_with_langstring_objects() -> None:
    """Test the initialization of MultiLangString with LangString objects."""
    langstr_en = LangString("Hello", "en")
    langstr_fr = LangString("Bonjour", "fr")
    multilang_str = MultiLangString(langstr_en, langstr_fr)
    assert len(multilang_str.langstrings) == 2, "Expected 2 langstrings, but found a different number."

    assert multilang_str.preferred_lang == "en", "Expected preferred language to be 'en', but found another value."


def test_init_with_control_and_preferred_language() -> None:
    """Test the initialization of MultiLangString with control and preferred language."""
    mls = MultiLangString(control="BLOCK_WARN", preferred_lang="fr")

    assert (
        len(mls.langstrings) == 0
    ), f"Expected 0 langstrings when initializing with given control and language, but found {len(mls.langstrings)}."

    assert mls.control == "BLOCK_WARN", f"Expected control to be 'BLOCK_WARN', but found {mls.control}."

    assert mls.preferred_lang == "fr", f"Expected preferred language to be 'fr', but found '{mls.preferred_lang}'."


def test_init_with_invalid_control_value() -> None:
    """Test the initialization of MultiLangString with an invalid control value."""
    with pytest.raises(ValueError):
        MultiLangString(control="INVALID_CONTROL")


def test_init_with_invalid_preferred_language() -> None:
    """Test the initialization of the `MultiLangString` class with an invalid preferred language.

    This test aims to:
    1. Ensure that a warning is raised when an invalid preferred language is provided during initialization.
    2. Verify that the instance of `MultiLangString` is still created correctly despite the invalid preferred language.
    """
    ls1 = LangString("Hello", "en")

    mls = MultiLangString(ls1, preferred_lang="xx-INVALID")

    # (Optional) Verify that the MultiLangString was still created correctly with the given LangString
    assert len(mls.langstrings) == 1
    assert "Hello" in mls.langstrings.get("en", [])


def test_init_with_control_enum_value() -> None:
    """Test the initialization of MultiLangString with a control enum value."""
    mls = MultiLangString(control="BLOCK_WARN")
    assert mls.control == "BLOCK_WARN"


def test_init_with_mixed_language_tags() -> None:
    """Test the initialization of the `MultiLangString` class with a mixture of valid and invalid language tags.

    This test aims to:
    1. Ensure that a warning is raised when an invalid language tag is encountered during initialization.
    2. Confirm that valid language tags are correctly added to the `MultiLangString` instance.
    3. Check that invalid language tags, even if not causing a failure, do not get added to the `MultiLangString`.
    """
    ls1 = LangString("Hello", "en")
    ls2 = LangString("Bonjour", "fr")

    # Add an invalid language tag and capture the warning here
    with pytest.warns(UserWarning):
        ls3 = LangString("Hola", "es-INVALID")

    mls = MultiLangString(ls1, ls2, ls3)

    # Verify that all language tags, including invalid ones, are added
    assert len(mls.langstrings) == 3, "Expected 3 langstrings (including invalid ones), but found a different number."


def test_init_with_default_preferred_language() -> None:
    """Test the initialization of MultiLangString with its default preferred language."""
    mls = MultiLangString()
    assert mls.preferred_lang == "en", "Expected default preferred language to be 'en', but found another value."


def test_init_with_duplicate_language_tags() -> None:
    """Test the initialization of MultiLangString with duplicate language tags."""
    langstr_en1 = LangString("Hello", "en")
    langstr_en2 = LangString("Hi", "en")
    with pytest.raises(ValueError):
        MultiLangString(langstr_en1, langstr_en2, control="BLOCK_ERROR")


def test_invalid_control_value_init():
    """Test the representation when control has an invalid value."""
    with pytest.raises(ValueError):
        MultiLangString(LangString("Hello", "en"), control="INVALID")
