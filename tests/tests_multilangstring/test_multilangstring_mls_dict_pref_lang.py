import pytest

from langstring import MultiLangString


# Test cases for mls_dict getter and setter
@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        ({"en": {"Hello"}, "fr": {"Bonjour"}}, {"en": {"Hello"}, "fr": {"Bonjour"}}),
        ({}, {}),
        ({"en": {"Hello"}, "fr": {"Bonjour"}, "es": {"Hola"}}, {"en": {"Hello"}, "fr": {"Bonjour"}, "es": {"Hola"}}),
        ({"en": set()}, {"en": set()}),  # Testing with an empty set for a language
    ],
)
def test_mls_dict_getter_setter(input_dict: dict, expected_output: dict):
    """Tests the getter and setter for mls_dict.

    :param input_dict: The input dictionary to set for mls_dict.
    :param expected_output: The expected dictionary to be retrieved from mls_dict.
    """
    mls = MultiLangString()
    mls.mls_dict = input_dict
    assert mls.mls_dict == expected_output, "mls_dict getter or setter does not work as expected"


# Test cases for pref_lang getter and setter
@pytest.mark.parametrize(
    "input_lang, expected_output",
    [
        ("en", "en"),
        ("fr", "fr"),
        (None, TypeError),
        ("es", "es"),
    ],
)
def test_pref_lang_getter_setter(input_lang: str, expected_output):
    """Tests the getter and setter for pref_lang.

    :param input_lang: The input language code to set for pref_lang.
    :param expected_output: The expected language code to be retrieved from pref_lang or the expected error.
    """
    mls = MultiLangString()
    if expected_output is TypeError:
        with pytest.raises(TypeError, match="Invalid 'lang' value received"):
            mls.pref_lang = input_lang
    else:
        mls.pref_lang = input_lang
        assert mls.pref_lang == expected_output, "pref_lang getter or setter does not work as expected"


# Testing for handling None as mls_dict
@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        (None, TypeError),  # Expect TypeError when setting mls_dict to None
    ],
)
def test_mls_dict_setter_none(input_dict, expected_output):
    """Tests setting mls_dict to None to ensure appropriate error is raised."""
    mls = MultiLangString()
    with pytest.raises(expected_output, match="Invalid type of 'mls_dict' received"):
        mls.mls_dict = input_dict


# Testing invalid types within mls_dict values
@pytest.mark.parametrize(
    "input_dict, expected_error",
    [
        ({"en": [123]}, TypeError),  # List instead of set
        ({"en": "Hello"}, TypeError),  # String instead of set
    ],
)
def test_mls_dict_setter_invalid_value_types(input_dict: dict, expected_error):
    """Tests setting mls_dict with invalid value types."""
    mls = MultiLangString()
    with pytest.raises(expected_error, match="Invalid 'texts' type in mls_dict init. Expected"):
        mls.mls_dict = input_dict
