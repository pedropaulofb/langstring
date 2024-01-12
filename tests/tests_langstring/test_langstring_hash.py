import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


@pytest.fixture
def langstring_en_hello() -> LangString:
    """Fixture for a LangString object with text 'Hello' and language 'en'."""
    return LangString("Hello", "en")


@pytest.fixture
def langstring_es_hello() -> LangString:
    """Fixture for a LangString object with text 'Hello' and language 'es'."""
    return LangString("Hello", "es")


@pytest.fixture
def langstring_en_hi() -> LangString:
    """Fixture for a LangString object with text 'Hi' and language 'en'."""
    return LangString("Hi", "en")


@pytest.mark.parametrize(
    "text, lang, other_text, other_lang, are_equal",
    [
        ("Hello", "en", "Hello", "en", True),
        ("Hello", "en", "Hello", None, False),
        ("Hello", "en", "Hi", "en", False),
        ("Hello", None, "Hello", None, True),
    ],
)
def test_langstring_hashing(text, lang, other_text, other_lang, are_equal) -> None:
    """Test LangString equality and hashing.

    :param text: Text for the first LangString.
    :param lang: Language tag for the first LangString.
    :param other_text: Text for the second LangString.
    :param other_lang: Language tag for the second LangString.
    :param are_equal: Expected equality result.
    """
    lang_str1 = LangString(text, lang)
    lang_str2 = LangString(other_text, other_lang)
    if are_equal:
        assert hash(lang_str1) == hash(lang_str2), "Equal LangStrings should have the same hash"


def test_hash_consistency(langstring_en_hello) -> None:
    """Test that the hash of a LangString object is consistent."""
    hash1 = hash(langstring_en_hello)
    hash2 = hash(langstring_en_hello)
    assert hash1 == hash2, "Hashes of the same LangString object should be consistent"


def test_hash_difference_for_different_texts(langstring_en_hello, langstring_en_hi) -> None:
    """Test that LangString objects with different texts have different hashes."""
    assert hash(langstring_en_hello) != hash(
        langstring_en_hi
    ), "LangString objects with different texts should have different hashes"


def test_hash_difference_for_different_languages(langstring_en_hello, langstring_es_hello) -> None:
    """Test that LangString objects with different languages have different hashes."""
    assert hash(langstring_en_hello) != hash(
        langstring_es_hello
    ), "LangString objects with different languages should have different hashes"


def test_hash_equality_for_identical_objects(langstring_en_hello) -> None:
    """Test that two identical LangString objects have the same hash."""
    langstring_duplicate = LangString("Hello", "en")
    assert hash(langstring_en_hello) == hash(
        langstring_duplicate
    ), "Identical LangString objects should have the same hash"


def test_langstring_hash() -> None:
    """Test the hash functionality of LangString."""
    lang_str1 = LangString("Hello", "en")
    lang_str2 = LangString("Hello", "en")
    assert hash(lang_str1) == hash(lang_str2), "Hash values should be the same for identical LangString instances"


def test_hash_consistency_with_flag_changes() -> None:
    """
    Test the consistency of the __hash__ method of LangString with changes in control flags.

    :raises AssertionError: If the hash value changes with control flag settings.
    """
    lang_str = LangString("Hello", "en")
    initial_hash = hash(lang_str)

    Controller.set_flag(LangStringFlag.DEFINED_TEXT, not Controller.get_flag(LangStringFlag.DEFINED_TEXT))
    assert hash(lang_str) == initial_hash, "Hash value should remain consistent despite changes in control flags"
