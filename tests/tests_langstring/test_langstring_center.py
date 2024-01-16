import pytest
from langstring.langstring import LangString

@pytest.mark.parametrize("text, width, fillchar, expected", [
    ("Hello", 10, " ", "  Hello   "),
    ("Hello", 10, "*", "**Hello***"),
    ("", 5, "-", "-----"),
    ("Python", 6, "*", "Python"),
    ("LangString", 20, " ", "     LangString     ")
])
def test_center_normal_cases(text, width, fillchar, expected):
    """Test centering of text with various widths and fill characters."""
    lang_str = LangString(text, "en")
    centered = lang_str.center(width, fillchar)
    assert centered.text == expected and centered.lang == lang_str.lang, \
        f"Expected centered text '{expected}', got '{centered.text}'"

@pytest.mark.parametrize("text, width", [
    ("Hello", -1),
    ("Hello", 0)
])
def test_center_invalid_width(text, width):
    """Test centering with invalid width values."""
    lang_str = LangString(text, "en")
    centered = lang_str.center(width)
    assert centered.text== text and centered.lang == lang_str.lang, f"Expected original text '{text}' for invalid width, got '{centered.text}'"

@pytest.mark.parametrize("width, fillchar, expected", [
    (10, " ", "          "),
    (5, "*", "*****"),
    (0, "-", "")
])
def test_center_with_empty_string(width, fillchar, expected):
    """Test centering an empty string with various widths and fill characters."""
    lang_str = LangString("", "en")
    centered = lang_str.center(width, fillchar)
    assert centered.text == expected and centered.lang == lang_str.lang, \
        f"Expected centered text '{expected}' for empty string, got '{centered.text}'"

@pytest.mark.parametrize("text, width, fillchar", [
    ("Hello", 10, 123),
    ("Hello", 10, None),
    ("Hello", 10, True)
])
def test_center_invalid_fillchar(text, width, fillchar):
    """Test centering with invalid fill character types."""
    lang_str = LangString(text, "en")
    with pytest.raises(TypeError, match="The fill character must be a unicode character, not"):
        _ = lang_str.center(width, fillchar)


def test_center_does_not_modify_original():
    """Ensure that centering does not modify the original LangString object."""
    original_text = "Hello"
    lang_str = LangString(original_text, "en")
    _ = lang_str.center(10, "*")
    assert lang_str.text == original_text, "Original LangString object should not be modified after centering"