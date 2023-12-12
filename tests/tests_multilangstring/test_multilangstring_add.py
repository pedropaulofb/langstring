"""Tests for the MultiLangString class's method add."""
import pytest

from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def test_add_overwrite() -> None:
    """Test the OVERWRITE control strategy."""
    ls1 = LangString("hello", "en")
    ls2 = LangString("goodbye", "en")

    mls = MultiLangString(ls1, control="OVERWRITE")
    mls.add_langstring(ls2)

    assert mls.langstrings["en"] == ["goodbye"], f"Expected 'goodbye', but got {mls.langstrings['en']}"


def test_add_allow() -> None:
    """Test the ALLOW control strategy."""
    ls1 = LangString("hello", "en")
    ls2 = LangString("goodbye", "en")

    mls = MultiLangString(ls1, control="ALLOW")
    mls.add_langstring(ls2)

    assert mls.langstrings["en"] == [
        "hello",
        "goodbye",
    ], f"Expected ['hello', 'goodbye'], but got {mls.langstrings['en']}"


def test_add_block_warn() -> None:
    """Test the BLOCK_WARN control strategy with a warning."""
    ls1 = LangString("hello", "en")
    ls2 = LangString("hello", "en")

    mls = MultiLangString(ls1, control="BLOCK_WARN")
    with pytest.warns(UserWarning, match=r"Operation not possible, a LangString with language tag en already exists."):
        mls.add_langstring(ls2)

    assert mls.langstrings["en"] == ["hello"], f"Expected 'hello', but got {mls.langstrings['en']}"


def test_add_block_error() -> None:
    """Test the BLOCK_ERROR control strategy with an error."""
    ls1 = LangString("hello", "en")
    ls2 = LangString("hello", "en")

    mls = MultiLangString(ls1, control="BLOCK_ERROR")
    with pytest.raises(ValueError, match=r"Operation not possible, a LangString with language tag en already exists."):
        mls.add_langstring(ls2)


def test_add_new_language() -> None:
    """Test adding a LangString with a new language."""
    ls1 = LangString("hello", "en")
    ls2 = LangString("hola", "es")

    mls = MultiLangString(ls1)
    mls.add_langstring(ls2)

    assert mls.langstrings["en"] == ["hello"], f"Expected 'hello', but got {mls.langstrings['en']}"
    assert mls.langstrings["es"] == ["hola"], f"Expected 'hola', but got {mls.langstrings['es']}"


def test_add_wrong_type() -> None:
    """Test adding a non-LangString type."""
    mls = MultiLangString(control="ALLOW")
    with pytest.raises(TypeError):
        mls.add_langstring("hello")


def test_add_empty_value() -> None:
    """Test adding a LangString with an empty string value."""
    ls_empty = LangString("", "en")

    mls = MultiLangString(control="ALLOW")
    mls.add_langstring(ls_empty)

    assert mls.langstrings["en"] == [""], f"Expected an empty string, but got {mls.langstrings['en']}"


def test_add_empty_value_overwrite() -> None:
    """Test the OVERWRITE control strategy with an empty string value."""
    ls1 = LangString("hello", "en")
    ls_empty = LangString("", "en")

    mls = MultiLangString(ls1, control="OVERWRITE")
    mls.add_langstring(ls_empty)

    assert mls.langstrings["en"] == [""], f"Expected an empty string, but got {mls.langstrings['en']}"


def test_add_empty_value_block_warn() -> None:
    """Test the BLOCK_WARN control strategy with an empty string value."""
    ls_empty1 = LangString("", "en")
    ls_empty2 = LangString("", "en")

    mls = MultiLangString(ls_empty1, control="BLOCK_WARN")
    with pytest.warns(UserWarning, match=r"Operation not possible, a LangString with language tag en already exists."):
        mls.add_langstring(ls_empty2)

    assert mls.langstrings["en"] == [""], f"Expected an empty string, but got {mls.langstrings['en']}"


def test_add_empty_value_block_error() -> None:
    """Test the BLOCK_ERROR control strategy with an empty string value."""
    ls_empty1 = LangString("", "en")
    ls_empty2 = LangString("", "en")

    mls = MultiLangString(ls_empty1, control="BLOCK_ERROR")
    with pytest.raises(ValueError, match=r"Operation not possible, a LangString with language tag en already exists."):
        mls.add_langstring(ls_empty2)
