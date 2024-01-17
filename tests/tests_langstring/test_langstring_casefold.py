import pytest

from langstring.langstring import LangString


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        ("Hello World", "en", "hello world"),
        ("Äpfel", "de", "äpfel"),
        ("ΑΘΗΝΑ", "el", "αθηνα"),
        ("", "en", ""),
    ],
)
def test_casefold_valid_input(text, lang, expected):
    """Test casefolding with valid inputs."""
    lang_str = LangString(text, lang)
    result = lang_str.casefold()
    assert result.text == expected and result.lang == lang


@pytest.mark.parametrize(
    "text, lang",
    [
        (None, "en"),
        (123, "en"),
        ([], "en"),
    ],
)
def test_casefold_invalid_text(text, lang):
    """Test casefolding with invalid text inputs."""
    with pytest.raises(TypeError, match="Expected 'str', got"):
        _ = LangString(text, lang).casefold()


@pytest.mark.parametrize(
    "text, lang",
    [
        ("Hello World", None),
        ("Hello World", 123),
        ("Hello World", []),
    ],
)
def test_casefold_invalid_lang(text, lang):
    """Test casefolding with invalid language inputs."""
    with pytest.raises(TypeError, match="Expected 'str', got"):
        _ = LangString(text, lang).casefold()


def test_casefold_does_not_modify_original():
    """Test that casefold does not modify the original LangString."""
    original = LangString("Hello World", "en")
    _ = original.casefold()
    assert original.text == "Hello World" and original.lang == "en"
