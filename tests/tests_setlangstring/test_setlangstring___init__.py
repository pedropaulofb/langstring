import pytest

from langstring import SetLangString


# Test cases for valid initialization
@pytest.mark.parametrize(
    "texts, lang",
    [
        ({"hello", "world"}, "en"),
        (set(), ""),
        (None, "fr"),
        ({"こんにちは", "世界"}, "jp"),
        ({"😊", "😂"}, "en"),
        ({"1", "2", "3"}, "en"),
    ],
)
def test_setlangstring_init_valid(texts, lang) -> None:
    """
    Test valid initializations of SetLangString.

    :param texts: A set of strings or None.
    :param lang: A language string.
    :return: None. Asserts if SetLangString is initialized correctly.
    """
    set_lang_string = SetLangString(texts, lang)
    expected_texts = texts if texts is not None else set()
    assert (
        set_lang_string.texts == expected_texts and set_lang_string.lang == lang
    ), f"Initialization failed for texts={texts} and lang={lang}"


# Test cases for invalid 'texts' input
@pytest.mark.parametrize(
    "invalid_texts",
    [
        ["hello", "world"],  # List instead of set
        "hello",  # String instead of set
        123,  # Integer instead of set
        {"hello", 123},  # Set with invalid element type
    ],
)
def test_setlangstring_init_invalid_texts(invalid_texts) -> None:
    """
    Test invalid 'texts' input during initialization of SetLangString.

    :param invalid_texts: Invalid 'texts' input.
    :return: None. Asserts if TypeError is raised for invalid 'texts' input.
    """
    with pytest.raises(TypeError, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString(invalid_texts, "en")


# Test cases for invalid 'lang' input
@pytest.mark.parametrize(
    "invalid_lang",
    [123, ["en"], {"lang": "en"}],  # Integer instead of string  # List instead of string  # Dict instead of string
)
def test_setlangstring_init_invalid_lang(invalid_lang) -> None:
    """
    Test invalid 'lang' input during initialization of SetLangString.

    :param invalid_lang: Invalid 'lang' input.
    :return: None. Asserts if TypeError is raised for invalid 'lang' input.
    """
    with pytest.raises(TypeError, match=r"Invalid argument with value '.+?'. Expected '.+?', but got '.+?'\."):
        SetLangString({"hello", "world"}, invalid_lang)


# Additional test cases for unusual but valid scenarios
@pytest.mark.parametrize(
    "texts, lang",
    [
        ({"hello", "こんにちは", "😊"}, "en123"),  # Mixed language and emoji texts with numeric lang
        (
            {"long_text_" * 100, "another_long_text_" * 100},
            "special_@_lang",
        ),  # Extremely long texts and special character lang
    ],
)
def test_setlangstring_init_unusual_valid(texts, lang) -> None:
    """
    Test unusual but valid initializations of SetLangString.

    :param texts: A set of strings with mixed types.
    :param lang: A language string with non-standard characters.
    :return: None. Asserts if SetLangString is initialized correctly with unusual inputs.
    """
    set_lang_string = SetLangString(texts, lang)
    assert (
        set_lang_string.texts == texts and set_lang_string.lang == lang
    ), f"Initialization failed for unusual but valid inputs: texts={texts}, lang={lang}"
