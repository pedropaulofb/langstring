import pytest
from langstring import LangString

def test_encode_default_parameters() -> None:
    """
    Test the `encode` method with default parameters.

    :return: None
    """
    lang_string = LangString("Hello, World!", "en")
    encoded = lang_string.encode()
    assert encoded == b"Hello, World!", "Encoding with default parameters should match expected bytes"

@pytest.mark.parametrize("text, lang, encoding, errors, expected", [
    ("Hello, World!", "en", "utf-8", "strict", b"Hello, World!"),
    ("Привет, мир!", "ru", "utf-8", "strict", b"\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!"),
    ("こんにちは", "ja", "utf-8", "strict", b"\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf"),
    ("Hello, World!", "en", "ascii", "ignore", b"Hello, World!"),
    ("こんにちは", "ja", "ascii", "ignore", b""),
])
def test_encode_valid_cases(text: str, lang: str, encoding: str, errors: str, expected: bytes) -> None:
    """
    Test the `encode` method for valid cases with different text, languages, encodings, and error handling strategies.

    :param text: The text to be encoded.
    :param lang: The language tag of the text.
    :param encoding: The encoding to be used.
    :param errors: The error handling strategy.
    :param expected: The expected encoded byte string.
    """
    lang_string = LangString(text, lang)
    result = lang_string.encode(encoding, errors)
    assert result == expected, f"Expected encoded result {expected}, got {result}"

