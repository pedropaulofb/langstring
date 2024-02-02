from unittest.mock import patch

import pytest

from langstring import SetLangString
from langstring.converter import Converter
from langstring.langstring import LangString


@pytest.fixture
def langstrings():
    return [LangString(text="Hello", lang="en"), LangString(text="World", lang="en")]

def test_from_langstrings_to_setlangstring(langstrings):
    expected_setlangstring = SetLangString(texts={"Hello", "World"}, lang="en")
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', return_value=expected_setlangstring):
        result = Converter.from_langstrings_to_setlangstring(langstrings)
        assert result == expected_setlangstring


@pytest.fixture
def mixed_lang_langstrings():
    return [
        LangString(text="Hello", lang="en"),
        LangString(text="Bonjour", lang="fr")
    ]

def test_valid_conversion(langstrings):
    expected = SetLangString(texts={"Hello", "World"}, lang="en")
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', return_value=expected) as mock_method:
        result = Converter.from_langstrings_to_setlangstring(langstrings)
        mock_method.assert_called_once_with(langstrings)
        assert result == expected, "The conversion did not produce the expected SetLangString."

def test_mixed_language_error(mixed_lang_langstrings):
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', side_effect=ValueError("Mixed languages")) as mock_method:
        with pytest.raises(ValueError, match="Mixed languages"):
            Converter.from_langstrings_to_setlangstring(mixed_lang_langstrings)
        mock_method.assert_called_once_with(mixed_lang_langstrings)

def test_empty_list():
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', side_effect=ValueError("Empty list")) as mock_method:
        with pytest.raises(ValueError, match="Empty list"):
            Converter.from_langstrings_to_setlangstring([])
        mock_method.assert_called_once_with([])


def test_duplicate_texts_same_language():
    # Setup: LangStrings with duplicate texts
    duplicate_langstrings = [
        LangString(text="Duplicate", lang="en"),
        LangString(text="Duplicate", lang="en")
    ]
    # Expected behavior: Only one instance of the text in the SetLangString
    expected = SetLangString(texts={"Duplicate"}, lang="en")

    # Assuming direct call without error for demonstration
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', return_value=expected) as mock_method:
        result = Converter.from_langstrings_to_setlangstring(duplicate_langstrings)
        mock_method.assert_called_once_with(duplicate_langstrings)
        assert result == expected, "Duplicate texts with the same language should result in unique texts in SetLangString."


def test_different_cases_unique_texts():
    # Setup: LangStrings with the same text in different cases
    case_langstrings = [
        LangString(text="hello", lang="en"),
        LangString(text="Hello", lang="en")
    ]
    # Expected behavior: Both texts are treated as unique in the SetLangString
    expected = SetLangString(texts={"hello", "Hello"}, lang="en")

    # Assuming direct call without error for demonstration
    with patch('langstring.converter.Converter.from_langstrings_to_setlangstring', return_value=expected) as mock_method:
        result = Converter.from_langstrings_to_setlangstring(case_langstrings)
        mock_method.assert_called_once_with(case_langstrings)
        assert result == expected, "Texts with different cases should be treated as unique in SetLangString."
