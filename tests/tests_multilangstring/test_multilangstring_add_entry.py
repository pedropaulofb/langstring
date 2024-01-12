import pytest

from langstring import Controller
from langstring import MultiLangString
from langstring import MultiLangStringFlag


def test_add_entry_to_empty_multilangstring():
    """
    Test adding an entry to an empty MultiLangString.
    """
    mls = MultiLangString()
    mls.add_entry("Hello", "en")
    assert mls.mls_dict == {"en": {"Hello"}}, "Entry should be added correctly to an empty MultiLangString"


def test_add_entry_to_existing_language():
    """
    Test adding an entry to an existing language in MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    mls.add_entry("Hi", "en")
    assert mls.mls_dict["en"] == {"Hello", "Hi"}, "New entry should be added to the existing set of texts"


def test_add_entry_with_new_language():
    """
    Test adding an entry with a new language to MultiLangString.
    """
    mls = MultiLangString()
    mls.add_entry("Bonjour", "fr")
    assert mls.mls_dict == {"fr": {"Bonjour"}}, "Entry with a new language should be added correctly"


@pytest.mark.parametrize(
    "text, lang, expected_error",
    [
        (123, "en", "Expected 'text' to be of type str"),
        ("Hello", 123, "Expected 'lang' to be of type str"),
        (None, "en", "Expected 'text' to be of type str"),
        ("", "en", "cannot receive empty string"),  # Assuming DEFINED_TEXT flag is True
    ],
)
def test_add_entry_invalid_arguments(text, lang, expected_error):
    """
    Test adding entries with invalid arguments to MultiLangString.

    :param text: The text to be added.
    :param lang: The language of the text.
    :param expected_error: The expected error message.
    """
    mls = MultiLangString()
    with pytest.raises((TypeError, ValueError), match=expected_error):
        mls.add_entry(text, lang)


@pytest.mark.parametrize(
    "flag, flag_state, text, lang, expected_error",
    [
        (MultiLangStringFlag.DEFINED_TEXT, True, "", "en", "cannot receive empty string"),
        (MultiLangStringFlag.VALID_LANG, True, "Hello", "invalid_lang", "cannot be invalid"),
    ],
)
def test_add_entry_respects_flags(flag, flag_state, text, lang, expected_error):
    """
    Test if add_entry method respects the control flags.

    :param flag: The flag to be tested.
    :param flag_state: The state to set for the flag.
    :param text: The text to be added.
    :param lang: The language of the text.
    :param expected_error: The expected error message.
    """
    Controller.set_flag(flag, flag_state)
    mls = MultiLangString()
    with pytest.raises(ValueError, match=expected_error):
        mls.add_entry(text, lang)


def test_add_duplicate_entry():
    """
    Test adding a duplicate entry to a language in MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    mls.add_entry("Hello", "en")
    assert mls.mls_dict["en"] == {"Hello"}, "Duplicate entries should not be added or should be handled appropriately"
