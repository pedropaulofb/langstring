import pytest

from langstring import LangString


@pytest.fixture
def langstring_en_hello():
    """Fixture for a LangString object with text 'Hello' and language 'en'."""
    return LangString("Hello", "en")


@pytest.fixture
def langstring_es_hello():
    """Fixture for a LangString object with text 'Hello' and language 'es'."""
    return LangString("Hello", "es")


@pytest.fixture
def langstring_en_hi():
    """Fixture for a LangString object with text 'Hi' and language 'en'."""
    return LangString("Hi", "en")


def test_hash_consistency(langstring_en_hello):
    """Test that the hash of a LangString object is consistent."""
    hash1 = hash(langstring_en_hello)
    hash2 = hash(langstring_en_hello)
    assert hash1 == hash2, "Hashes of the same LangString object should be consistent"


def test_hash_difference_for_different_texts(langstring_en_hello, langstring_en_hi):
    """Test that LangString objects with different texts have different hashes."""
    assert hash(langstring_en_hello) != hash(
        langstring_en_hi
    ), "LangString objects with different texts should have different hashes"


def test_hash_difference_for_different_languages(langstring_en_hello, langstring_es_hello):
    """Test that LangString objects with different languages have different hashes."""
    assert hash(langstring_en_hello) != hash(
        langstring_es_hello
    ), "LangString objects with different languages should have different hashes"


def test_hash_equality_for_identical_objects(langstring_en_hello):
    """Test that two identical LangString objects have the same hash."""
    langstring_duplicate = LangString("Hello", "en")
    assert hash(langstring_en_hello) == hash(
        langstring_duplicate
    ), "Identical LangString objects should have the same hash"
