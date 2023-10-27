import pytest

from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString
from langstring_lib.tests.tests_multilangstring.sample_multilangstring import create_sample_multilangstring


def test_remove_existing_langstring() -> None:
    """Test removing an existing LangString from a MultiLangString."""
    multi_lang_string = create_sample_multilangstring()
    langstring_to_remove = LangString("Bonjour", "fr")

    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove an existing LangString from MultiLangString."
    assert "fr" not in multi_lang_string.langstrings, "French LangString was not removed from MultiLangString."


def test_remove_non_existent_langstring() -> None:
    """Test attempting to remove a non-existent LangString from a MultiLangString."""
    multi_lang_string = create_sample_multilangstring()
    langstring_to_remove = LangString("Saluton", "eo")  # Esperanto greeting, not in sample MultiLangString

    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is False, "Unexpectedly reported success while trying to remove a non-existent LangString."
    assert "eo" not in multi_lang_string.langstrings, "Esperanto, a non-existent LangString, found in MultiLangString."


def test_remove_langstring_from_language_with_multiple_entries() -> None:
    """Test removing a LangString from a language with multiple LangString entries."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), LangString("Hi", "en"), control="ALLOW")

    langstring_to_remove = LangString("Hello", "en")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove a LangString from a language with multiple entries."
    assert (
            "Hello" not in multi_lang_string.langstrings["en"]
    ), "'Hello' was not removed from English LangStrings in MultiLangString."
    assert (
            "Hi" in multi_lang_string.langstrings["en"]
    ), "'Hi' was not found in English LangStrings in MultiLangString after removal attempt."


def test_remove_last_langstring_from_language() -> None:
    """Test removing the last LangString for a specific language."""
    multi_lang_string = create_sample_multilangstring()
    langstring_to_remove = LangString("Hallo", "de")

    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove the last LangString for a specific language."
    assert "de" not in multi_lang_string.langstrings, (
        "German LangString was not removed even though it was " "the last one."
    )


def test_remove_invalid_argument_type() -> None:
    """Test attempting to remove a LangString using an invalid argument type."""
    multi_lang_string = create_sample_multilangstring()

    # Using an integer instead of a LangString
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_langstring(123)

    assert str(excinfo.value) == "Expected a LangString but received 'int'."


def test_remove_none_argument() -> None:
    """Test attempting to remove a LangString using a None argument."""
    multi_lang_string = create_sample_multilangstring()

    # Using None instead of a LangString
    with pytest.raises(TypeError) as excinfo:
        multi_lang_string.remove_langstring(None)

    assert str(excinfo.value) == "Expected a LangString but received 'NoneType'."


def test_remove_empty_langstring() -> None:
    """Test attempting to remove an empty LangString."""
    multi_lang_string = create_sample_multilangstring()
    empty_langstring = LangString("", "fr")

    result = multi_lang_string.remove_langstring(empty_langstring)

    assert result is False, "Expected to not find and remove an empty French string in MultiLangString."


def test_remove_duplicate_langstring_entries() -> None:
    """Test removing a duplicate LangString entry from a MultiLangString."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), LangString("Hello", "en"), control="ALLOW")

    langstring_to_remove = LangString("Hello", "en")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove a duplicate LangString."
    # Depending on behavior: Either all duplicates are removed, or just one.
    if "en" in multi_lang_string.langstrings:
        assert "Hello" not in multi_lang_string.langstrings["en"], "Not all duplicates of 'Hello' were removed."
    else:
        # If 'en' key doesn't exist, it implies all duplicates were removed.
        pass


def test_case_sensitive_removal() -> None:
    """Test the case sensitivity when removing a LangString."""
    multi_lang_string = create_sample_multilangstring()

    langstring_to_remove = LangString("HELLO", "en")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is False, "Unexpectedly removed a LangString with different casing."


def test_whitespace_handling() -> None:
    """Test the removal of a LangString with leading or trailing whitespaces."""
    multi_lang_string = MultiLangString(LangString(" Hello ", "en"), control="ALLOW")

    langstring_to_remove = LangString("Hello", "en")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is False, "Unexpectedly removed a LangString with differing whitespace."


def test_special_characters() -> None:
    """Test the removal of a LangString with special characters."""
    special_string = "!@#Hello$%^"
    multi_lang_string = MultiLangString(LangString(special_string, "en"), control="ALLOW")

    langstring_to_remove = LangString(special_string, "en")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove a LangString with special characters."
    assert "en" not in multi_lang_string.langstrings, "Failed to remove English LangString with special characters."


def test_remove_from_empty_multilangstring() -> None:
    """Test attempting to remove a LangString from an empty MultiLangString."""
    multi_lang_string = MultiLangString(control="ALLOW")
    langstring_to_remove = LangString("Hello", "en")

    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is False, "Reported success when trying to remove a LangString from an empty MultiLangString."


def test_remove_langstring_same_text_diff_lang() -> None:
    """Test removing a LangString with the same text but different language."""
    multi_lang_string = MultiLangString(LangString("Hello", "en"), LangString("Hello", "fr"), control="ALLOW")

    langstring_to_remove = LangString("Hello", "fr")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove the French LangString with text 'Hello'."
    assert "fr" not in multi_lang_string.langstrings, "Failed to remove French LangString with text 'Hello'."


def test_unicode_removal() -> None:
    """Test the removal of a LangString with non-ASCII characters."""
    multi_lang_string = MultiLangString(LangString("こんにちは", "jp"), control="ALLOW")

    langstring_to_remove = LangString("こんにちは", "jp")
    result = multi_lang_string.remove_langstring(langstring_to_remove)

    assert result is True, "Failed to remove the Japanese LangString."
    assert "jp" not in multi_lang_string.langstrings, "Failed to remove Japanese LangString."
