import pytest

from langstring.converter import Converter
from langstring.langstring import LangString
from tests.conftest import TYPEERROR_MSG_SINGULAR


@pytest.mark.parametrize(
    "input_string,ignore_at_sign,expected_result",
    [
        ("Hello@en", False, LangString("Hello", "en")),
        ("Hello@en", True, LangString("Hello@en", "")),
        ("Hello", False, LangString("Hello", "")),
        ("@en", False, LangString("", "en")),
        ("@", False, LangString("", "")),
        ("", False, LangString("", "")),
    ],
)
def test_from_string_to_langstring(input_string: str, ignore_at_sign: bool, expected_result: LangString):
    """
    Test the `from_string_to_langstring` method for various input scenarios.

    :param input_string: The input string to be converted to a LangString.
    :param ignore_at_sign: Flag to ignore or consider '@' in the input string for splitting text and lang.
    :param expected_result: The expected LangString result.
    :return: Asserts if the conversion results match the expected LangString object.
    """
    result = Converter.from_string_to_langstring(input_string, ignore_at_sign)
    assert result == expected_result, (
        f"Expected LangString with text '{expected_result.text}' and lang "
        f"'{expected_result.lang}', but got text '{result.text}' and lang "
        f"'{result.lang}'."
    )


@pytest.mark.parametrize(
    "input_string,expected_error",
    [
        (123, TypeError),
        (None, TypeError),
    ],
)
def test_from_string_to_langstring_type_errors(input_string, expected_error):
    """
    Test the `from_string_to_langstring` method with inputs of incorrect type.

    :param input_string: The input string, intentionally of the wrong type, to trigger a TypeError.
    :param expected_error: The expected error type.
    :param match_text: Regex pattern to match the error message.
    :return: Asserts if TypeError is raised with the expected message.
    """
    with pytest.raises(expected_error, match=TYPEERROR_MSG_SINGULAR):
        Converter.from_string_to_langstring(input_string)


@pytest.mark.parametrize(
    "input_string,expected_error",
    [
        (None, TypeError),
        ([], TypeError),
        (True, TypeError),
    ],
)
def test_from_string_to_langstring_invalid_type(input_string, expected_error):
    """Test conversion with invalid input types."""
    with pytest.raises(expected_error):
        Converter.from_string_to_langstring(input_string)


@pytest.mark.parametrize(
    "input_string,ignore_at_sign,expected_text,expected_lang",
    [
        ("NoLangInfo", False, "NoLangInfo", ""),
        ("NoLangInfo", True, "NoLangInfo", ""),
        ("NoLangInfo@", False, "NoLangInfo", ""),
        ("NoLangInfo@", True, "NoLangInfo@", ""),
        ("@NoText", False, "", "NoText"),
        ("@NoText", True, "@NoText", ""),
        ("@@@", False, "@@", ""),
        ("@@@", True, "@@@", ""),
        ("With@@Sign", False, "With@", "Sign"),
        ("With@@Sign", True, "With@@Sign", ""),
        ("Multiple@Signs@In@String", False, "Multiple@Signs@In", "String"),
        ("Multiple@Signs@In@String", True, "Multiple@Signs@In@String", ""),
        ("CapsLOCK@EN", False, "CapsLOCK", "EN"),
        ("CapsLOCK@EN", True, "CapsLOCK@EN", ""),
        (" @LeadingSpace", False, " ", "LeadingSpace"),
        (" @LeadingSpace", True, " @LeadingSpace", ""),
        ("TrailingSpace@ ", False, "TrailingSpace", " "),
        ("TrailingSpace@ ", True, "TrailingSpace@ ", ""),
        ("@@", False, "@", ""),
        ("@@", True, "@@", ""),
        ("@StartAndEnd@", False, "@StartAndEnd", ""),
        ("@StartAndEnd@", True, "@StartAndEnd@", ""),
        (" @StartAndEnd@ ", False, " @StartAndEnd", " "),
        (" @StartAndEnd@ ", True, " @StartAndEnd@ ", ""),
        ("@", False, "", ""),
        ("@", True, "@", ""),
        ("  @  ", False, "  ", "  "),
        ("  @  ", True, "  @  ", ""),
    ],
)
def test_from_string_to_langstring_edge_cases(input_string, ignore_at_sign, expected_text, expected_lang):
    """Test edge cases and unusual but valid usages."""
    result = Converter.from_string_to_langstring(input_string, ignore_at_sign)
    assert (
        result.text == expected_text and result.lang == expected_lang
    ), "Conversion did not handle edge cases or unusual usage as expected."


@pytest.mark.parametrize(
    "input_string,expected_output",
    [
        ("simpletext", LangString("simpletext", "")),
        ("    ", LangString("    ", "")),
        ("\n@en", LangString("\n", "en")),
        ("text with spaces@en", LangString("text with spaces", "en")),
        ("text with multiple @@@", LangString("text with multiple @@", "")),
    ],
)
def test_from_string_to_langstring_unusual_valid_usage(input_string, expected_output):
    """Test unusual but valid input strings."""
    result = Converter.from_string_to_langstring(input_string)
    assert result == expected_output, "Unusual but valid input was not handled correctly."


@pytest.mark.parametrize(
    "input_string,ignore_at_sign,expected_text,expected_lang",
    [
        # Testing inputs with unusual characters
        ("Special&Char@es", False, "Special&Char", "es"),
        ("Numbers123@num", False, "Numbers123", "num"),
        # Testing inputs with multiple '@' but considering only the last one for lang separation
        ("part1@part2@part3", False, "part1@part2", "part3"),
        # Testing inputs with spaces and '@' in various positions
        (" LeadingSpace@en", False, " LeadingSpace", "en"),
        ("TrailingSpace @en", False, "TrailingSpace ", "en"),
        (" SurroundingSpaces @ en ", False, " SurroundingSpaces ", " en "),
        # Testing ignore_at_sign with complex strings
        ("Complex@String@With@Multiple@At@en", True, "Complex@String@With@Multiple@At@en", ""),
        # Testing non-ASCII characters
        ("こんにちは@ja", False, "こんにちは", "ja"),
        ("Привет@ru", False, "Привет", "ru"),
        # Testing mixed language codes and unusual text patterns
        ("Text@EN-us", False, "Text", "EN-us"),
        ("emoji😊@emoji", False, "emoji😊", "emoji"),
        # Testing edge case with only spaces and '@'
        ("   @   ", False, "   ", "   "),
        # Testing complete absence of text or language
        ("@", True, "@", ""),
        ("@", False, "", ""),
        # Ensure empty string is handled correctly
        ("", True, "", ""),
        ("", False, "", ""),
        # Test with only spaces
        ("   ", True, "   ", ""),
        ("   ", False, "   ", ""),
        # Test strings that look like email addresses
        ("example@example.com", False, "example", "example.com"),
        ("example@example.com", True, "example@example.com", ""),
    ],
)
def test_from_string_to_langstring_comprehensive(input_string, ignore_at_sign, expected_text, expected_lang):
    """Comprehensive tests to ensure all relevant scenarios are covered for the method from_string_to_langstring."""
    result = Converter.from_string_to_langstring(input_string, ignore_at_sign)
    assert result.text == expected_text and result.lang == expected_lang, (
        f"Conversion of '{input_string}' with ignore_at_sign={ignore_at_sign} "
        f"did not yield expected text '{expected_text}' and lang '{expected_lang}'."
    )
