import pytest

from langstring import MultiLangString


@pytest.mark.parametrize(
    "lang, expected_keys",
    [
        ("en", ["es"]),  # Deleting existing language
        ("eN", ["es"]),  # Deleting existing language
        ("EN", ["es"]),  # Deleting existing language
        ("es-ES", ["en"]),  # Deleting language with region
    ],
)
def test_multilangstring_delitem_valid(lang: str, expected_keys: list):
    """
    Test the __delitem__ method for valid language deletion scenarios.

    :param lang: The language code to be deleted from the MultiLangString instance.
    :param expected_keys: The expected remaining language codes in the instance after deletion.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}, "es-ES": {"Hola Mundo Español"}})
    del mls[lang]
    assert (
        all(key in mls.mls_dict for key in expected_keys) and lang not in mls.mls_dict
    ), f"After deleting '{lang}', expected remaining keys are {expected_keys}."


@pytest.mark.parametrize(
    "lang, match_msg",
    [
        ("fr", "fr"),  # Attempt to delete non-existent language
        (" en", " en"),  # Non-existent language with trailing space
        ("EN ", "EN "),  # Non-existent language with trailing space
        ("", ""),  # Attempt to delete an empty string language code
        ("Ελ", "Ελ"),  # Attempt to delete a language with Greek characters
        ("Привет", "Привет"),  # Attempt to delete a language with Cyrillic characters
        ("🚀", "🚀"),  # Attempt to delete a language with emoji
        ("special-char#", "special-char#"),  # Attempt to delete a language with special characters
    ],
)
def test_multilangstring_delitem_key_error(lang: str, match_msg: str):
    """
    Test the __delitem__ method for scenarios where deletion should raise KeyError.

    :param lang: The language code attempted to be deleted, expected to not exist in the instance.

    :raises KeyError: If the language code does not exist in the MultiLangString instance.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    with pytest.raises(KeyError, match=match_msg):
        del mls[lang]


@pytest.mark.parametrize(
    "lang, match_msg",
    [
        (123, "Argument .+ must be of type 'str', but got"),  # Non-string input: integer
        ([], "Argument .+ must be of type 'str', but got"),  # Non-string input: list
        ({}, "Argument .+ must be of type 'str', but got"),  # Non-string input: dictionary
    ],
)
def test_multilangstring_delitem_type_error(lang: str, match_msg: str):
    """Test the delitem method for type validation, expecting TypeError for invalid input types.
    :param lang: The invalid language code input, not of type str, to be tested for deletion.
    :raises TypeError: If the input is not of type str.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    with pytest.raises(TypeError, match=match_msg):
        del mls[lang]


def test_multilangstring_delitem_none_value():
    """
    Test the __delitem__ method for invalid values like null and empty strings, expecting TypeError.
    :param lang: The invalid language code input to be tested for deletion.
    :raises TypeError: If the input is null or an empty string.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}})
    with pytest.raises(TypeError, match="Argument .+ must be of type 'str', but got"):
        del mls[None]


@pytest.mark.parametrize(
    "lang, expected_exception, match_msg",
    [
        ("  es  ", KeyError, "  es  "),  # Valid language with extra spaces around
        ("en-US", KeyError, "en-US"),  # Attempting a locale-specific deletion that doesn't exist
    ],
)
def test_multilangstring_delitem_edge_cases(lang: str, expected_exception: type, match_msg: str):
    """
    Test the __delitem__ method for edge cases including unusual but potentially valid inputs.
    :param lang: The language code being tested for deletion.
    :param expected_exception: The type of exception expected to be raised.
    :param match_msg: The expected message in the exception.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    with pytest.raises(expected_exception, match=match_msg):
        del mls[lang]
