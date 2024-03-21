import pytest

from langstring import LangStringFlag
from langstring.controller import Controller
from langstring.utils.validator import Validator
from tests.conftest import TYPEERROR_MSG_SINGULAR


# Test valid language codes
@pytest.mark.parametrize("lang", ["en", "fr", "es"])
def test_validate_lang_valid_codes(lang):
    """Test validate_lang with valid language codes."""
    Controller.set_flag(LangStringFlag.VALID_LANG, True)
    assert (
        Validator.validate_flags_lang(LangStringFlag, lang) == lang
    ), f"Valid language code '{lang}' should be accepted."


# Test invalid language codes
@pytest.mark.parametrize("invalid_lang", ["invalid-lang", "123", ""])
def test_validate_lang_invalid_codes(invalid_lang):
    """Test validate_lang with invalid language codes."""
    Controller.set_flag(LangStringFlag.VALID_LANG, True)
    with pytest.raises(ValueError, match="Expected valid language code."):
        Validator.validate_flags_lang(LangStringFlag, invalid_lang)


# Test non-string inputs
@pytest.mark.parametrize("non_string", [123, 5.5, True, None, [], {}])
def test_validate_lang_non_string_input(non_string):
    """Test validate_lang with non-string inputs."""
    with pytest.raises(TypeError, match=TYPEERROR_MSG_SINGULAR):
        Validator.validate_flags_lang(LangStringFlag, non_string)


# Test empty string with DEFINED_LANG flag
def test_validate_lang_empty_string_defined_lang():
    """Test validate_lang with empty string when DEFINED_LANG flag is enabled."""
    Controller.set_flag(LangStringFlag.DEFINED_LANG, True)
    with pytest.raises(ValueError, match="Expected non-empty 'str'."):
        Validator.validate_flags_lang(LangStringFlag, "")


# Test stripping whitespace
@pytest.mark.parametrize("lang_with_space", [" en ", "fr ", " es"])
def test_validate_lang_invalid_whitespace(lang_with_space):
    """Test validate_lang with language codes having leading/trailing spaces should be considered invalid."""
    Controller.set_flag(LangStringFlag.STRIP_LANG, False)
    Controller.set_flag(LangStringFlag.VALID_LANG, True)
    with pytest.raises(ValueError, match="Expected valid language code."):
        Validator.validate_flags_lang(LangStringFlag, lang_with_space)


# Test lowercase conversion
@pytest.mark.parametrize("uppercase_lang", ["EN", "FR", "ES"])
def test_validate_lang_lowercase_conversion(uppercase_lang):
    """Test validate_lang with uppercase language codes."""
    Controller.set_flag(LangStringFlag.LOWERCASE_LANG, True)
    assert (
        Validator.validate_flags_lang(LangStringFlag, uppercase_lang) == uppercase_lang.lower()
    ), "Language code should be converted to lowercase."


# Test without VALID_LANG flag
@pytest.mark.parametrize("lang", ["en", "invalid-lang"])
def test_validate_lang_without_valid_lang_flag(lang):
    """Test validate_lang without VALID_LANG flag."""
    Controller.set_flag(LangStringFlag.VALID_LANG, False)
    assert (
        Validator.validate_flags_lang(LangStringFlag, lang) == lang
    ), "Language code should be accepted without VALID_LANG flag."


@pytest.mark.parametrize("lang_with_space", [" en ", "fr ", " es"])
def test_validate_lang_whitespace_invalid(lang_with_space):
    """Test validate_lang with language codes having leading/trailing spaces should be valid."""
    Controller.set_flag(LangStringFlag.STRIP_LANG, True)
    assert Validator.validate_flags_lang(LangStringFlag, lang_with_space)
