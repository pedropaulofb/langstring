import pytest
from langstring import MultiLangString, Controller, MultiLangStringFlag


@pytest.mark.parametrize("print_with_lang, expected_output", [(True, "{}"), (False, "{}")])
def test_multi_lang_string_str_empty(print_with_lang: bool, expected_output: str):
    """Test __str__ method with an empty MultiLangString.

    :param print_with_lang: Flag to indicate if language tags should be included in the output.
    :param expected_output: Expected string representation of an empty MultiLangString.
    """
    Controller.set_flag(MultiLangStringFlag.PRINT_WITH_LANG, print_with_lang)
    mls = MultiLangString()
    assert str(mls) == expected_output, (
        f"Empty MultiLangString should return '{expected_output}' when "
        f"PRINT_WITH_LANG is {'enabled' if print_with_lang else 'disabled'}."
    )


@pytest.mark.parametrize(
    "texts, expected_with_lang, expected_without_lang",
    [
        ([("", "")], "{''}@\"\"", "{''}"),
        ([("Hello", "en")], "{'Hello'}@en", "{'Hello'}"),
        ([("Hola", "es"), ("Hello", "en")], "{'Hola'}@es, {'Hello'}@en", "{'Hola'}, {'Hello'}"),
        ([(" Привет", "ru"), (" Γειά", "gr")], "{' Привет'}@ru, {' Γειά'}@gr", "{' Привет'}, {' Γειά'}"),  # Leading spaces in text, Cyrillic and Greek.
        ([("Hello ", "en"), ("Hola", "es ")], "{'Hello '}@en, {'Hola'}@es ", "{'Hello '}, {'Hola'}"),  # Trailing spaces in text and language.
        ([("Καλημέρα", "GR"), ("Hello", "EN")], "{'Καλημέρα'}@GR, {'Hello'}@EN", "{'Καλημέρα'}, {'Hello'}"),  # Mixed case languages.
        ([("Hello😊", "en"), ("😢", "emoji")], "{'Hello😊'}@en, {'😢'}@emoji", "{'Hello😊'}, {'😢'}"),  # Emojis in text and as a language.
        ([("Hello\nWorld", "en"), ("Line\nBreak", "mult")], "{'Hello\nWorld'}@en, {'Line\nBreak'}@mult", "{'Hello\nWorld'}, {'Line\nBreak'}"),  # Newline characters in text.
        ([("Speci@l Ch@racters", "en"), ("<XML>", "markup")], "{'Speci@l Ch@racters'}@en, {'<XML>'}@markup", "{'Speci@l Ch@racters'}, {'<XML>'}"),  # Special characters.
        ([("Hello", "en"), ("hello", "en")], "{'Hello', 'hello'}@en", "{'Hello', 'hello'}"),
        ([("你好", "zh-Hant"), ("こんにちは", "ja")], "{'你好'}@zh-Hant, {'こんにちは'}@ja", "{'你好'}, {'こんにちは'}"),
        ([("", "en")], "{''}@en", "{''}"),
        ([(" ", "en")], "{' '}@en", "{' '}"),
        ([("مرحبا", "ar"), ("שלום", "he")], "{'مرحبا'}@ar, {'שלום'}@he", "{'مرحبا'}, {'שלום'}"),
        ([("Line1\\nLine2", "en")], "{'Line1\\nLine2'}@en", "{'Line1\\nLine2'}"),
    ],
)
def test_multi_lang_string_str_various_texts(
    texts: list[tuple[str, str]], expected_with_lang: str, expected_without_lang: str):
    """Test __str__ method with various texts and languages.

    :param texts: List of text and language pairs to add to the MultiLangString.
    :param expected_with_lang: Expected string representation with language tags included.
    :param expected_without_lang: Expected string representation without language tags.
    :param reset_controller_flags: Pytest fixture to reset Controller flags before each test.
    """
    mls = MultiLangString()
    for text, lang in texts:
        mls.add_entry(text, lang)

    Controller.set_flag(MultiLangStringFlag.PRINT_WITH_LANG, True)
    assert str(mls) == expected_with_lang, "String representation with languages included does not match expected."

    Controller.set_flag(MultiLangStringFlag.PRINT_WITH_LANG, False)
    assert str(mls) == expected_without_lang, "String representation without languages does not match expected."

@pytest.mark.parametrize(
    "texts, expected_output",
    [
        ([("Hello", "en"), ("Hello", "en")], "{'Hello'}@en"),
        ([("Hello", "en"), ("Hello", "es")], "{'Hello'}@en, {'Hello'}@es"),
        ([("Hello" * 100, "en")], f"{{'{'Hello' * 100}'}}@en"),
    ],
)
def test_multi_lang_string_str_edge_and_unusual_cases(texts: list[tuple[str, str]], expected_output: str):
    """Test __str__ method for edge and unusual but valid cases.

    :param texts: List of text and language pairs to add to the MultiLangString.
    :param expected_output: Expected string representation.
    """
    Controller.set_flag(MultiLangStringFlag.PRINT_WITH_LANG, True)
    mls = MultiLangString()
    for text, lang in texts:
        mls.add_entry(text, lang)
    assert str(mls) == expected_output, "String representation does not match expected for edge or unusual cases."
