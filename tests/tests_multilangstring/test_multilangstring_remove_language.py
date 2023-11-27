import pytest

from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString
from tests.tests_multilangstring.sample_multilangstring import create_sample_multilangstring


def test_remove_existing_language() -> None:
    """Test removing all LangStrings of an existing language from a MultiLangString."""
    multi_lang_string = create_sample_multilangstring()

    result = multi_lang_string.remove_language("fr")

    assert result is True, "Failed to remove an existing language from MultiLangString."
    assert "fr" not in multi_lang_string.langstrings, "French LangStrings were not removed from MultiLangString."


def test_remove_non_existent_language() -> None:
    """Test attempting to remove LangStrings of a non-existent language from a MultiLangString."""
    multi_lang_string = create_sample_multilangstring()

    result = multi_lang_string.remove_language("eo")

    assert result is False, "Unexpectedly reported success while trying to remove a non-existent language."
    assert "eo" not in multi_lang_string.langstrings, "Esperanto, a non-existent language, found in MultiLangString."


def test_remove_language_with_multiple_entries() -> None:
    """Test removing a language with multiple associated LangString entries."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), LangString("Hi", "en"), control="ALLOW")

    result = multi_lang_string.remove_language("en")

    assert result is True, "Failed to remove a language with multiple LangString entries."
    assert "en" not in multi_lang_string.langstrings, "English LangStrings were not removed from MultiLangString."


def test_remove_invalid_language_format() -> None:
    """Test attempting to remove LangStrings using an invalid language format."""
    multi_lang_string = create_sample_multilangstring()
    invalid_language = "123"
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(invalid_language)
    assert (
        str(excinfo.value) == f"Invalid language format. Expected alphabetic string and received '{invalid_language}'."
    )


def test_language_case_sensitivity() -> None:
    """Test if the removal of LangStrings by language is case-sensitive."""
    multi_lang_string = create_sample_multilangstring()

    # Using uppercase instead of lowercase
    result = multi_lang_string.remove_language("FR")

    assert result is True, "Failed to remove a language due to case sensitivity."
    assert "FR" not in multi_lang_string.langstrings, "Uppercase language was not removed from MultiLangString."


def test_remove_from_empty_multilangstring() -> None:
    """Test attempting to remove a language from an empty MultiLangString."""
    multi_lang_string = MultiLangString(control="ALLOW")

    result = multi_lang_string.remove_language("en")

    assert result is False, (
        "Unexpectedly reported success while trying to remove a language from an empty " "MultiLangString."
    )


def test_remove_empty_language_code() -> None:
    """Test removing LangStrings with an empty language code."""
    multi_lang_string = create_sample_multilangstring()
    empty_language = ""
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(empty_language)
    assert (
        str(excinfo.value)
        == "Invalid language format. Expected non-empty alphabetic string and received an empty string."
    )


def test_remove_language_non_string() -> None:
    """Test attempting to remove LangStrings with a non-string language code."""
    multi_lang_string = create_sample_multilangstring()

    non_string_language = 123  # Using a number
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(non_string_language)

    assert (
        str(excinfo.value)
        == f"Invalid language format. Expected alphabetic string and received '{non_string_language}'."
    )


def test_remove_language_with_special_characters() -> None:
    """Test attempting to remove LangStrings with a language code that contains special characters."""
    multi_lang_string = create_sample_multilangstring()
    special_char_language = "en-US"  # Using a regional code
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(special_char_language)
    assert (
        str(excinfo.value)
        == f"Invalid language format. Expected alphabetic string and received '{special_char_language}'."
    )


def test_remove_language_with_spaces() -> None:
    """Test attempting to remove LangStrings with a language code that contains spaces."""
    multi_lang_string = create_sample_multilangstring()
    spaced_language = "en us"  # Using spaces
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(spaced_language)
    assert (
        str(excinfo.value) == f"Invalid language format. Expected alphabetic string and received '{spaced_language}'."
    )


def test_remove_language_with_mixed_characters() -> None:
    """Test attempting to remove LangStrings with a mixed character set in the language code."""
    multi_lang_string = create_sample_multilangstring()
    mixed_language = "3n"  # Using alphanumeric characters
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_language(mixed_language)
    assert str(excinfo.value) == f"Invalid language format. Expected alphabetic string and received '{mixed_language}'."
