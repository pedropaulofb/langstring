from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString


def test_basic_functionality() -> None:
    """Ensure to_string_list converts a MultiLangString to a list of strings."""
    mls = MultiLangString(LangString("Hello", "en"), LangString("Bonjour", "fr"))
    result = mls.to_string_list()
    expected = ["'Hello'@en", "'Bonjour'@fr"]
    assert set(result) == set(expected), f"Expected {expected} but got {result}"


def test_empty_multilangstring() -> None:
    """Ensure an empty MultiLangString converts to an empty list."""
    mls = MultiLangString()
    result = mls.to_string_list()
    assert result == [], f"Expected an empty list but got {result}"


def test_multiple_entries_for_language() -> None:
    """Ensure multiple entries for a single language are correctly converted."""
    mls = MultiLangString(LangString("Hello", "en"), LangString("Hi", "en"))
    result = mls.to_string_list()
    expected = ["'Hello'@en", "'Hi'@en"]
    assert set(result) == set(expected), f"Expected {expected} but got {result}"


def test_special_characters() -> None:
    """Ensure special characters in LangString are correctly converted."""
    mls = MultiLangString(LangString('Hel"lo', "en"), LangString("Bonjour!", "fr"))
    result = mls.to_string_list()
    expected = ["'Hel\"lo'@en", "'Bonjour!'@fr"]
    assert set(result) == set(expected), f"Expected {expected} but got {result}"


def test_empty_initialization() -> None:
    """Ensure correct handling of empty initialization."""
    mls: MultiLangString = MultiLangString()
    result: list[str] = mls.to_string_list()
    assert result == [], "Expected an empty list for an empty MultiLangString initialization"


def test_duplicate_langstring_same_text() -> None:
    """Ensure duplicate LangStrings with the same text are stored correctly based on the control setting."""
    # Using control "ALLOW"
    mls_allow: MultiLangString = MultiLangString(LangString("Hello", "en"), LangString("Hello", "en"), control="ALLOW")
    result_allow: list[str] = mls_allow.to_string_list()
    assert result_allow == ["'Hello'@en"], f"Expected no duplicate entries for control ALLOW, but got {result_allow}"

    # Using control "OVERWRITE"
    mls_overwrite: MultiLangString = MultiLangString(
        LangString("Hello", "en"), LangString("Hello", "en"), control="OVERWRITE"
    )
    result_overwrite: list[str] = mls_overwrite.to_string_list()
    assert result_overwrite == [
        "'Hello'@en"
    ], f"Expected a single entry for control OVERWRITE, but got {result_overwrite}"


def test_duplicate_langstring_different_text() -> None:
    """Ensure duplicate LangStrings with different texts are stored correctly based on the control setting."""
    # Using control "ALLOW"
    mls_allow: MultiLangString = MultiLangString(LangString("Hello", "en"), LangString("Hi", "en"), control="ALLOW")
    result_allow: list[str] = mls_allow.to_string_list()
    assert set(result_allow) == {
        "'Hello'@en",
        "'Hi'@en",
    }, f"Expected different texts for control ALLOW, but got {result_allow}"


def test_extremely_long_text() -> None:
    """Test extremely long text input."""
    long_text: str = "a" * 10000
    mls: MultiLangString = MultiLangString(LangString(long_text, "en"))
    result: list[str] = mls.to_string_list()
    assert result == [f"'{long_text}'@en"], "Expected the long text to be stored correctly, but got a different result"


def test_empty_text() -> None:
    """Test empty text with a valid language tag."""
    mls: MultiLangString = MultiLangString(LangString("", "en"))
    result: list[str] = mls.to_string_list()
    assert result == ["''@en"], f"Expected an empty text entry, but got {result}"
