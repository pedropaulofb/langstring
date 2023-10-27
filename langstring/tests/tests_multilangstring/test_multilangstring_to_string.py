from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString
from langstring.tests.tests_multilangstring.sample_multilangstring import create_sample_multilangstring


def test_to_string_matches_str_representation():
    """Verify that to_string() provides the same output as __str__()."""
    multi_lang_string = create_sample_multilangstring()

    assert multi_lang_string.to_string() == str(
        multi_lang_string
    ), "The output of to_string() should match the output of __str__()."


def test_string_representation_single_entry():
    """Check the string representation for a MultiLangString with a single LangString."""
    lang_string = LangString("Hello", "en")
    multi_lang_string = MultiLangString(lang_string)

    expected_output = "'Hello'@en"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected string representation to be {expected_output} but got {str(multi_lang_string)}."


def test_string_representation_multiple_entries_single_language():
    """Verify string representation for MultiLangString with multiple LangStrings for a single language."""
    lang_string1 = LangString("Hello", "en")
    lang_string2 = LangString("Hi", "en")
    multi_lang_string = MultiLangString(lang_string1, lang_string2)

    expected_output = "'Hello'@en, 'Hi'@en"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected string representation to be {expected_output} but got {str(multi_lang_string)}."


def test_string_representation_multiple_entries_multiple_languages():
    """Confirm string representation for a MultiLangString with multiple LangStrings for multiple languages."""
    lang_string1 = LangString("Hello", "en")
    lang_string2 = LangString("Hi", "en")
    lang_string3 = LangString("Bonjour", "fr")
    multi_lang_string = MultiLangString(lang_string1, lang_string2, lang_string3)

    expected_output = "'Hello'@en, 'Hi'@en, 'Bonjour'@fr"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected string representation to be {expected_output} but got {str(multi_lang_string)}."


def test_string_representation_empty_multilangstring():
    """Check the string representation for an empty MultiLangString."""
    multi_lang_string = MultiLangString()

    expected_output = ""
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected string representation to be an empty string but got {str(multi_lang_string)}."


def test_string_representation_invalid_langstring():
    """Check the string representation with an improperly initialized LangString (e.g., no language)."""
    lang_string = LangString("Hello", "")  # Empty language code
    multi_lang_string = MultiLangString(lang_string)

    expected_output = "'Hello'@"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected string representation to be {expected_output} but got {str(multi_lang_string)}."


def test_string_representation_multiple_same_language():
    """Check the string representation when there are multiple LangStrings for the same language."""
    langstring1 = LangString("Hello", "en")
    langstring2 = LangString("Hi", "en")
    multi_lang_string = MultiLangString(langstring1, langstring2)

    expected_output = "'Hello'@en, 'Hi'@en"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected '{expected_output}' but got '{str(multi_lang_string)}'."


def test_string_representation_special_characters():
    """Check the string representation handles special characters."""
    special_value = "Hello\nWorld\"!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    langstring = LangString(special_value, "en")
    multi_lang_string = MultiLangString(langstring)

    # Adjusting the expected_output to match the repr representation
    expected_output = f"{repr(special_value)}@en"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected '{expected_output}' but got '{str(multi_lang_string)}'."


def test_string_representation_long_value():
    """Test the string representation with a very long LangString value."""
    long_value = "A" * 5000  # Creating a very long string
    langstring = LangString(long_value, "en")
    multi_lang_string = MultiLangString(langstring)

    expected_output = f"'{long_value}'@en"
    assert str(multi_lang_string) == expected_output, (
        f"Expected the first 120 characters to be '{expected_output[:120]}...' but "
        f"got '{str(multi_lang_string)[:120]}...'."
    )


def test_string_representation_multiple_languages():
    """Test the string representation with multiple LangStrings of different languages."""
    langstring_en = LangString("Hello", "en")
    langstring_fr = LangString("Bonjour", "fr")
    multi_lang_string = MultiLangString(langstring_en, langstring_fr)

    expected_output = "'Hello'@en, 'Bonjour'@fr"
    assert (
        str(multi_lang_string) == expected_output
    ), f"Expected '{expected_output}' but got '{str(multi_lang_string)}'."
