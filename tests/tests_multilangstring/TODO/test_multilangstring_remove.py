import pytest
from langstring import MultiLangString, LangString, SetLangString


@pytest.mark.parametrize(
    "text,lang,clean_empty,expected_result",
    [
        ("Hello", "en", False, {"en": set(), "fr": set()}),  # Adjusted to reflect the correct expected result
        ("Bonjour", "fr", True, {"en": {"Hello"}}),  # Adjusted because "Bonjour" does not exist, so no change
        (
            "Hello",
            "en",
            True,
            {"fr": set()},
        ),  # Correct, removes "Hello" and leaves "fr" since it's empty but clean_empty is True
        # Add these lines to your existing parametrization under `test_remove_valid_entry`
        ("Hello", "en", False, {"fr": set()}),  # Entry exists and is removed without cleaning empty languages
        ("Hello", "en", True, {"fr": set()}),  # Entry exists and is removed with cleaning empty languages
        ("  Hello  ", "en", False, {"en": {"Hello"}, "fr": set()}),  # With spaces around, entry not found
        ("HELLO", "en", False, {"en": {"Hello"}, "fr": set()}),  # Different case, entry not found
        ("Hello", "EN", False, {"en": {"Hello"}, "fr": set()}),  # Language case sensitivity, entry not found
        ("Hello", "en", False, {"en": set(), "fr": set()}),  # Reiteration to clarify removal without cleaning
    ],
)
def test_remove_valid_entry(text: str, lang: str, clean_empty: bool, expected_result: dict):
    mls = MultiLangString({"en": {"Hello"}, "fr": set()})
    mls.remove((text, lang), clean_empty)
    assert mls.mls_dict == expected_result, f"Expected mls_dict to be {expected_result}, got {mls.mls_dict}"


@pytest.mark.parametrize(
    "text,lang,clean_empty,expected_exception,match_message",
    [
        (("Hola", "es", False, ValueError, "Entry 'Hola@es' not found in the MultiLangString.")),
        ((LangString("Hello", "en"), None, False, TypeError, "Argument .* must be of type 'tuple.*")),
        ((SetLangString({"Hola"}, "es"), None, True, TypeError, "Argument .* must be of type 'tuple.*")),
        (("Guten Tag", "de", True, ValueError, "Entry 'Guten Tag@de' not found in the MultiLangString.")),
        ("", "en", False, ValueError, "Entry '@en' not found in the MultiLangString."),  # Empty string
        (
            " HELLO ",
            "en",
            True,
            ValueError,
            "Entry ' HELLO @en' not found in the MultiLangString.",
        ),  # With spaces around
        (
            "hello",
            "en",
            False,
            ValueError,
            "Entry 'hello@en' not found in the MultiLangString.",
        ),  # Lowercase, non-matching case
        ("Γειά", "gr", True, ValueError, "Entry 'Γειά@gr' not found in the MultiLangString."),  # Greek characters
        (
            "Привет",
            "ru",
            False,
            ValueError,
            "Entry 'Привет@ru' not found in the MultiLangString.",
        ),  # Cyrillic characters
        ("😊", "emoji", True, ValueError, "Entry '😊@emoji' not found in the MultiLangString."),  # Emoji as language
        ("Hello!", "en", True, ValueError, "Entry 'Hello!@en' not found in the MultiLangString."),  # Special character

(None, "en", False, TypeError, "must be str, not NoneType"),  # Null text
("Hello", None, False, TypeError, "language code must be str, not NoneType"),  # Null lang
("Hello", "en", None, TypeError, "clean_empty must be bool, not NoneType"),  # Null clean_empty
({}, "en", False, TypeError, "text must be str, not dict"),  # Invalid text type
("Hello", 123, False, TypeError, "language code must be str, not int"),  # Invalid lang type
("Hello", "en", "yes", TypeError, "clean_empty must be bool, not str"),  # Invalid clean_empty type
    ],
)
def test_remove_invalid_entry(text, lang, clean_empty, expected_exception, match_message):
    """Test the remove method with invalid inputs or scenarios.

    :param text: The text entry or the object to be removed.
    :param lang: The language of the text entry.
    :param clean_empty: Whether to clean empty language sets after removal.
    :param expected_exception: Expected exception type if the operation is supposed to fail.
    :param match_message: The message expected to be part of the exception, if any.
    """
    mls = MultiLangString({"en": {"Hello"}, "fr": set()})
    with pytest.raises(expected_exception, match=match_message):
        mls.remove((text, lang) if not isinstance(text, (LangString, SetLangString)) else text, clean_empty)
