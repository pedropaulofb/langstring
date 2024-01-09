import pytest

from langstring import Controller
from langstring import MultiLangString
from langstring import MultiLangStringFlag


def test_multilangstring_init_with_default_parameters():
    """
    Test if MultiLangString initializes correctly with default parameters.
    """
    mls = MultiLangString()
    assert mls.mls_dict == {}, "MultiLangString initialized with default parameters should have an empty mls_dict"
    assert mls.preferred_lang == "en", "Default preferred language should be 'en'"


def test_multilangstring_init_with_custom_parameters():
    """
    Test if MultiLangString initializes correctly with custom parameters.
    """
    custom_dict = {"en": {"Hello"}, "fr": {"Bonjour"}}
    mls = MultiLangString(mls_dict=custom_dict, pref_lang="fr")
    assert mls.mls_dict == custom_dict, "MultiLangString should initialize with the provided mls_dict"
    assert mls.preferred_lang == "fr", "Preferred language should be set to the provided value"


def test_multilangstring_init_with_invalid_mls_dict_type():
    """
    Test if initializing MultiLangString with an invalid mls_dict type raises a TypeError.
    """
    with pytest.raises(TypeError, match="Invalid type for argument mls_dict."):
        MultiLangString(mls_dict="invalid")


def test_multilangstring_init_with_invalid_pref_lang_type():
    """
    Test if initializing MultiLangString with an invalid pref_lang type raises a TypeError.
    """
    with pytest.raises(TypeError, match="Invalid type for argument pref_lang."):
        MultiLangString(pref_lang=123)


@pytest.mark.parametrize("flag_state", [True, False])
def test_multilangstring_init_respects_ensure_valid_lang_flag(flag_state):
    """
    Test if MultiLangString initialization respects the ENSURE_VALID_LANG flag.

    :param flag_state: The state to set for the ENSURE_VALID_LANG flag.
    """
    Controller.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, flag_state)
    if flag_state:
        with pytest.raises(ValueError, match="field cannot be invalid"):
            MultiLangString(mls_dict={"invalid_lang": {"Hello"}})
    else:
        mls = MultiLangString(mls_dict={"invalid_lang": {"Hello"}})
        assert (
            "invalid_lang" in mls.mls_dict
        ), "MultiLangString should allow invalid language codes when ENSURE_VALID_LANG is False"


def test_multilangstring_init_with_non_string_texts():
    """
    Test if initializing MultiLangString with non-string texts in mls_dict raises a TypeError.
    """
    with pytest.raises(TypeError, match="Expected 'text' to be of type str"):
        MultiLangString(mls_dict={"en": {123}})


def test_multilangstring_init_with_empty_language_code():
    """
    Test if initializing MultiLangString with an empty language code and non-empty texts is handled correctly.
    """
    mls_dict = {"": {"Hello"}}
    mls = MultiLangString(mls_dict=mls_dict)
    assert (
        "" in mls.mls_dict and "Hello" in mls.mls_dict[""]
    ), "MultiLangString should allow empty language code with non-empty texts"


def test_multilangstring_init_with_mixed_valid_and_invalid_data():
    """
    Test if initializing MultiLangString with a mix of valid and invalid data in mls_dict is handled correctly.
    """
    mls_dict = {"en": {"Hello"}, "invalid_lang": {123}}
    with pytest.raises(TypeError, match="Expected 'text' to be of type str"):
        MultiLangString(mls_dict=mls_dict)


@pytest.mark.parametrize(
    "flag, flag_state", [(MultiLangStringFlag.ENSURE_TEXT, True)]
)
def test_multilangstring_init_respects_other_flags(flag, flag_state):
    """
    Test if MultiLangString initialization respects other flags like ENSURE_TEXT or ENSURE_ANY_LANG.

    :param flag: The flag to be tested.
    :param flag_state: The state to set for the flag.
    """
    Controller.set_flag(flag, flag_state)
    mls_dict = {"en": {""}}
    expected_error = "cannot receive empty string" if flag_state else None

    if expected_error:
        with pytest.raises(ValueError, match=expected_error):
            MultiLangString(mls_dict=mls_dict)
    else:
        mls = MultiLangString(mls_dict=mls_dict)
        assert mls.mls_dict == mls_dict, "MultiLangString should initialize correctly respecting the flag settings"
