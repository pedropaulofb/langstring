import pytest

from langstring.controller import Controller
from langstring.langstring import LangStringFlag
from langstring.utils.validator import Validator
from tests.conftest import TYPEERROR_MSG_SINGULAR


# Test cases for valid text input
@pytest.mark.parametrize("text, expected", [("Hello", "Hello"), ("  Hello  ", "Hello"), ("", "")])
def test_validate_text_valid(text, expected):
    """Test validate_text with valid inputs."""
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.set_flag(LangStringFlag.STRIP_TEXT, True)
    assert Validator.validate_flags_text(LangStringFlag, text) == expected, "Valid text should be validated correctly."


# Test cases for invalid text input
@pytest.mark.parametrize("invalid_text", [123, None, 5.5, [], {}])
def test_validate_text_invalid_type(invalid_text):
    """Test validate_text with invalid input types."""
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        Validator.validate_flags_text(LangStringFlag, invalid_text)


# Test cases for empty text with DEFINED_TEXT flag enabled
def test_validate_text_empty_with_defined_text_flag():
    """Test validate_text with empty string and DEFINED_TEXT flag enabled."""
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    with pytest.raises(ValueError, match="Invalid 'text' value received"):
        Validator.validate_flags_text(LangStringFlag, "")


# Test cases for non-empty text with DEFINED_TEXT flag enabled
def test_validate_text_non_empty_with_defined_text_flag():
    """Test validate_text with non-empty string and DEFINED_TEXT flag enabled."""
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    assert (
        Validator.validate_flags_text(LangStringFlag, "Hello") == "Hello"
    ), "Non-empty text should be validated correctly."


# Test cases for stripping text
@pytest.mark.parametrize("text, expected", [(" Hello ", "Hello"), ("Hello", "Hello")])
def test_validate_text_strip_text(text, expected):
    """Test validate_text with STRIP_TEXT flag enabled."""
    Controller.set_flag(LangStringFlag.STRIP_TEXT, True)
    assert Validator.validate_flags_text(LangStringFlag, text) == expected, "Text should be stripped correctly."


# Test cases for not stripping text
@pytest.mark.parametrize("text, expected", [(" Hello ", " Hello "), ("Hello", "Hello")])
def test_validate_text_no_strip_text(text, expected):
    """Test validate_text with STRIP_TEXT flag disabled."""
    Controller.set_flag(LangStringFlag.STRIP_TEXT, False)
    assert Validator.validate_flags_text(LangStringFlag, text) == expected, "Text should not be stripped."


# Test cases for strings with only whitespace
@pytest.mark.parametrize("whitespace_text", [" ", "   ", "\t", "\n"])
def test_validate_text_whitespace_only(whitespace_text):
    """Test validate_text with strings containing only whitespace."""
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.set_flag(LangStringFlag.STRIP_TEXT, True)
    assert (
        Validator.validate_flags_text(LangStringFlag, whitespace_text) == ""
    ), "Whitespace-only text should be handled correctly."


# Test cases for unusual but valid strings
@pytest.mark.parametrize("unusual_text", ["特殊字符", "1234567890" * 100, "!@#$%^&*()"])
def test_validate_text_unusual_valid_strings(unusual_text):
    """Test validate_text with unusual but valid strings."""
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    Controller.set_flag(LangStringFlag.STRIP_TEXT, False)
    assert (
        Validator.validate_flags_text(LangStringFlag, unusual_text) == unusual_text
    ), "Unusual but valid text should be validated correctly."
