import pytest

from langstring import MultiLangString


@pytest.mark.parametrize(
    "mls_data, pref_lang, expected_result",
    [
        ({"en": {"Hello", "World"}}, "en", True),  # Entries present in the preferred language
        ({"en": set()}, "en", False),  # No entries in the preferred language
        ({"en": {"Hello"}, "es": {"Hola", "Mundo"}}, "es", True),  # Entries present in a non-English preferred language
        ({"fr": set(), "de": set()}, "fr", False),  # Preferred language empty, others also empty
        ({"fr": {"Bonjour"}, "de": {"Guten Tag"}}, "it", False),  # Preferred language not present
        ({"en": {" "}}, "en", True),  # Spaces only in English entries
        ({"EN": {" "}}, "en", True),  # Case insensivity in mls_dict
        ({"en": {" "}}, "EN", True),  # Case insensivity in pref_lang
        ({" en": {" "}}, "en", False),
        ({"ru": {"Привет", "Мир"}}, "ru", True),  # Cyrillic characters in Russian entries
        ({"gr": {"Γειά σου", "Κόσμος"}}, "gr", True),  # Greek characters in Greek entries
        ({"emoji": {"😊", "🌍"}}, "emoji", True),  # Emojis as entries
        ({"mixed": {"Hello", "世界", "123"}}, "mixed", True),  # Mixed charset and numbers
        ({"special": {"@Hello#", "$World&"}}, "special", True),  # Special characters in entries
        ({"spaces": {" Hello", "World "}}, "spaces", True),  # Leading and trailing spaces in entries
        ({"empty_strings": {""}}, "empty_strings", True),  # Empty string as an entry
        ({"multiple_spaces": {"   "}}, "multiple_spaces", True),  # Multiple spaces as an entry
        ({"upper_case": {"HELLO", "WORLD"}}, "en", False),  # Upper case preferred language code with no match
    ],
)
def test_has_pref_lang_entries_parametrized(mls_data, pref_lang, expected_result):
    """Test has_pref_lang_entries with various configurations to ensure it correctly identifies presence or absence of preferred language entries."""
    mls = MultiLangString(mls_data, pref_lang=pref_lang)
    assert (
        mls.has_pref_lang_entries() == expected_result
    ), f"Expected {expected_result} for preferred language '{pref_lang}' with data {mls_data}"
