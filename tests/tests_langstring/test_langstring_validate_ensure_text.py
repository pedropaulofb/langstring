import pytest

from langstring import LangString
from langstring import LangStringControl
from langstring import LangStringFlag


def test_validate_ensure_text_with_non_empty_text() -> None:
    """Test _validate_ensure_text method with non-empty text."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    try:
        LangString("Hello", "en")
    except ValueError:
        pytest.fail("Unexpected ValueError with non-empty text when ENSURE_TEXT is enabled")


def test_validate_ensure_text_with_empty_text_flag_enabled() -> None:
    """Test _validate_ensure_text method with empty text and ENSURE_TEXT flag enabled."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    with pytest.raises(ValueError, match="ENSURE_TEXT enabled: LangString's 'text' field cannot receive empty string."):
        LangString("", "en")


def test_validate_ensure_text_with_empty_text_flag_disabled() -> None:
    """Test _validate_ensure_text method with empty text and ENSURE_TEXT flag disabled."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)
    try:
        lang_str = LangString("", "en")
        assert lang_str.text == "", "LangString should accept empty text when ENSURE_TEXT is disabled"
    except ValueError:
        pytest.fail("Unexpected ValueError with empty text when ENSURE_TEXT is disabled")


def test_validate_ensure_text_with_whitespace() -> None:
    """Test _validate_ensure_text method with whitespace as text."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    try:
        lang_str = LangString("   ", "en")
        assert lang_str.text == "   ", "LangString should accept whitespace as text when ENSURE_TEXT is enabled"
    except ValueError:
        pytest.fail("Unexpected ValueError with whitespace as text when ENSURE_TEXT is enabled")


def test_validate_ensure_text_with_none() -> None:
    """Test _validate_ensure_text method with None as text."""
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    with pytest.raises(TypeError, match="Expected 'text' to be of type str, but got NoneType."):
        LangString(None, "en")
