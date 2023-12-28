import pytest

from langstring import LangString
from langstring import MultiLangString


@pytest.fixture
def sample_langstrings_hash() -> list[LangString]:
    """Fixture to provide sample LangString objects for testing.

    :return: A list of LangString objects with different texts and languages.
    :rtype: list[LangString]
    """
    return [LangString("Hello", "en"), LangString("Hola", "es"), LangString("Bonjour", "fr")]


def test_hash_consistency(sample_langstrings_hash: list[LangString]) -> None:
    """Test that the hash value of a MultiLangString object remains consistent.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    hash1 = hash(mls)
    hash2 = hash(mls)
    assert hash1 == hash2, "Hash values of the same MultiLangString object should be consistent."


def test_hash_equality_for_identical_multilangstrings(sample_langstrings_hash: list[LangString]) -> None:
    """Test that identical MultiLangString objects have the same hash value.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Identical MultiLangString objects should have the same hash value."


def test_hash_inequality_for_different_multilangstrings(sample_langstrings_hash: list[LangString]) -> None:
    """Test that different MultiLangString objects have different hash values.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash[:2], preferred_lang="en")  # First two mls_dict
    mls2 = MultiLangString(*sample_langstrings_hash[1:], preferred_lang="en")  # Last two mls_dict
    assert hash(mls1) != hash(mls2), "Different MultiLangString objects should have different hash values."


def test_hash_with_different_order_of_addition(sample_langstrings_hash: list[LangString]) -> None:
    """Test that the order of addition of mls_dict does not affect the hash value.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    mls2 = MultiLangString(*reversed(sample_langstrings_hash), preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Order of addition of mls_dict should not affect the hash value."


def test_hash_with_different_preferred_languages(sample_langstrings_hash: list[LangString]) -> None:
    """Test that different preferred languages do not affect the hash value.

    With the updated logic, different preferred_lang values do not affect the hash.
    This test checks that two MultiLangString objects with the same mls_dict but different preferred_lang
    have the same hash value.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings_hash, preferred_lang="es")
    assert hash(mls1) == hash(mls2), "Different preferred languages should not affect the hash value."


def test_hash_with_different_control_strategies(sample_langstrings_hash: list[LangString]) -> None:
    """Test that different control strategies do not affect the hash value.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash, control="ALLOW", preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings_hash, control="OVERWRITE", preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Different control strategies should not affect the hash value."


def test_hash_with_modified_langstrings(sample_langstrings_hash: list[LangString]) -> None:
    """Test that modifying the contents of a MultiLangString affects its hash value.

    :param sample_langstrings_hash: Fixture providing sample LangString objects.
    :type sample_langstrings_hash: list[LangString]
    """
    mls1 = MultiLangString(*sample_langstrings_hash, preferred_lang="en")
    hash_before = hash(mls1)
    mls1.add_langstring(LangString("New text", "en"))
    hash_after = hash(mls1)
    assert hash_before != hash_after, "Modifying the contents of a MultiLangString should change its hash value."


def test_hash_with_empty_multilangstring() -> None:
    """Test the hash value of an empty MultiLangString."""
    mls = MultiLangString(preferred_lang="en")
    assert isinstance(hash(mls), int), "Hash of an empty MultiLangString should still be an integer."
