import pytest

from langstring import LangString
from langstring import MultiLangString
from langstring import MultiLangStringControl
from langstring import MultiLangStringFlag


def test_add_langstring_to_empty_multilangstring():
    """
    Test adding a LangString to an empty MultiLangString.
    """
    mls = MultiLangString()
    langstring = LangString(text="Hello", lang="en")
    mls.add_langstring(langstring)
    assert mls.mls_dict == {"en": {"Hello"}}, "LangString should be added correctly to an empty MultiLangString"


def test_add_langstring_to_existing_language():
    """
    Test adding a LangString to an existing language in MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    langstring = LangString(text="Hi", lang="en")
    mls.add_langstring(langstring)
    assert mls.mls_dict["en"] == {"Hello", "Hi"}, "LangString should be added to the existing set of texts"


def test_add_langstring_with_new_language():
    """
    Test adding a LangString with a new language to MultiLangString.
    """
    mls = MultiLangString()
    langstring = LangString(text="Bonjour", lang="fr")
    mls.add_langstring(langstring)
    assert mls.mls_dict == {"fr": {"Bonjour"}}, "LangString with a new language should be added correctly"


def test_add_langstring_invalid_type():
    """
    Test adding an invalid type (not LangString) to MultiLangString raises a TypeError.
    """
    mls = MultiLangString()
    with pytest.raises(TypeError, match="Expected a LangString"):
        mls.add_langstring("not a LangString")


@pytest.mark.parametrize(
    "flag, flag_state, text, lang, expected_error",
    [
        (MultiLangStringFlag.ENSURE_TEXT, True, "", "en", "cannot receive empty string"),
        (MultiLangStringFlag.ENSURE_ANY_LANG, True, "Hello", "", "cannot receive empty string"),
        (MultiLangStringFlag.ENSURE_VALID_LANG, True, "Hello", "invalid_lang", "cannot be invalid"),
    ],
)
def test_add_langstring_respects_flags(flag, flag_state, text, lang, expected_error):
    """
    Test if add_langstring method respects the control flags.

    :param flag: The flag to be tested.
    :param flag_state: The state to set for the flag.
    :param text: The text of the LangString to be added.
    :param lang: The language of the LangString.
    :param expected_error: The expected error message.
    """
    MultiLangStringControl.set_flag(flag, flag_state)
    mls = MultiLangString()

    with pytest.raises(ValueError, match=expected_error):
        langstring = LangString(text=text, lang=lang)
        mls.add_langstring(langstring)


def test_add_duplicate_langstring():
    """
    Test adding a duplicate LangString to a language in MultiLangString.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    duplicate_langstring = LangString(text="Hello", lang="en")
    mls.add_langstring(duplicate_langstring)
    assert mls.mls_dict["en"] == {
        "Hello"
    }, "Duplicate LangStrings should not be added or should be handled appropriately"
