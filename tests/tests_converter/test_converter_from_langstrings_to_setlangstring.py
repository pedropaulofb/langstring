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

