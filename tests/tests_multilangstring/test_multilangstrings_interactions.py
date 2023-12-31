import pytest

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag
from langstring import MultiLangString
from langstring import MultiLangStringControl
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "flag, flag_state",
    [
        (MultiLangStringFlag.ENSURE_TEXT, False),
        (MultiLangStringFlag.ENSURE_ANY_LANG, True),
        (MultiLangStringFlag.ENSURE_VALID_LANG, True),
    ],
)
def test_flag_setting_impact_on_multilangstring_methods(flag, flag_state):
    """
    Test the impact of changing flag settings on MultiLangString methods.

    :param flag: The flag to be tested.
    :param flag_state: The state to set for the flag.
    """
    MultiLangStringControl.set_flag(flag, flag_state)
    mls = MultiLangString()

    # Test the impact on add_entry method
    if flag == MultiLangStringFlag.ENSURE_TEXT and not flag_state:
        mls.add_entry("", "en")  # Should not raise an exception
    else:
        with pytest.raises(ValueError):
            mls.add_entry("", "en")

    # Test the impact on add_langstring method
    langstring = LangString(
        text="Hello", lang="invalid-lang" if flag == MultiLangStringFlag.ENSURE_VALID_LANG else "en"
    )
    if flag == MultiLangStringFlag.ENSURE_VALID_LANG and flag_state:
        with pytest.raises(ValueError):
            mls.add_langstring(langstring)
    else:
        mls.add_langstring(langstring)  # Should not raise an exception


def test_add_entry_and_add_langstring_with_validations():
    """
    Test the add_entry and add_langstring methods with different validation scenarios.
    """
    mls = MultiLangString()
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, True)
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, True)
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, True)

    # Test add_entry with invalid data
    with pytest.raises(ValueError):
        mls.add_entry("", "invalid-lang")

    # Temporarily disable ENSURE_TEXT for creating LangString with empty text
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    langstring = LangString(text="", lang="invalid-lang")

    # Test add_langstring with invalid data
    with pytest.raises(ValueError):
        mls.add_langstring(langstring)

    # Reset flags and test with valid data
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, False)
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, False)
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, False)
    mls.add_entry("Hello", "en")  # Should not raise an exception
    assert "Hello" in mls.get_strings_lang("en"), "Entry 'Hello' should be added under 'en'"

    langstring = LangString(text="Hello", lang="en")
    mls.add_langstring(langstring)  # Should not raise an exception
    assert "Hello" in mls.get_strings_lang("en"), "LangString 'Hello' should be added under 'en'"


def test_removal_methods_impact_on_retrieval_methods():
    """
    Test the impact of remove_entry and remove_lang on retrieval methods.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello", "Hi"}, "fr": {"Bonjour"}})

    # Remove an entry and test retrieval
    mls.remove_entry("Hello", "en")
    assert "Hello" not in mls.get_strings_lang("en"), "Removed entry should not be in the retrieved data"

    # Remove a language and test retrieval
    mls.remove_lang("fr")
    assert "fr" not in mls.get_langstrings_all(), "Removed language should not be in the retrieved data"
