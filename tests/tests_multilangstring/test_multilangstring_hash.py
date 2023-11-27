from langstring import MultiLangString, LangString
from tests.tests_multilangstring.test_multilangstring_eq import sample_langstrings


def test_hash_consistency(sample_langstrings):
    """
    Test that the hash value of a MultiLangString object remains consistent.
    """
    mls = MultiLangString(*sample_langstrings, preferred_lang="en")
    hash1 = hash(mls)
    hash2 = hash(mls)
    assert hash1 == hash2, "Hash values of the same MultiLangString object should be consistent."


def test_hash_equality_for_identical_multilangstrings(sample_langstrings):
    """
    Test that identical MultiLangString objects have the same hash value.
    """
    mls1 = MultiLangString(*sample_langstrings, preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings, preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Identical MultiLangString objects should have the same hash value."


def test_hash_inequality_for_different_multilangstrings(sample_langstrings):
    """
    Test that different MultiLangString objects have different hash values.
    """
    mls1 = MultiLangString(*sample_langstrings[:2], preferred_lang="en")  # First two langstrings
    mls2 = MultiLangString(*sample_langstrings[1:], preferred_lang="en")  # Last two langstrings
    assert hash(mls1) != hash(mls2), "Different MultiLangString objects should have different hash values."


def test_hash_with_different_order_of_addition(sample_langstrings):
    """
    Test that the order of addition of langstrings does not affect the hash value.
    """
    mls1 = MultiLangString(*sample_langstrings, preferred_lang="en")
    mls2 = MultiLangString(*reversed(sample_langstrings), preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Order of addition of langstrings should not affect the hash value."


def test_hash_with_different_preferred_languages(sample_langstrings):
    """
    Test that different preferred languages do not affect the hash value.

    With the updated logic, different preferred_lang values do not affect the hash.
    This test checks that two MultiLangString objects with the same langstrings but different preferred_lang
    have the same hash value.

    :param sample_langstrings: Fixture providing sample LangString objects.
    """
    mls1 = MultiLangString(*sample_langstrings, preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings, preferred_lang="es")
    assert hash(mls1) == hash(mls2), "Different preferred languages should not affect the hash value."


def test_hash_with_different_control_strategies(sample_langstrings):
    """
    Test that different control strategies do not affect the hash value.
    """
    mls1 = MultiLangString(*sample_langstrings, control="ALLOW", preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings, control="OVERWRITE", preferred_lang="en")
    assert hash(mls1) == hash(mls2), "Different control strategies should not affect the hash value."


def test_hash_with_modified_langstrings(sample_langstrings):
    """
    Test that modifying the contents of a MultiLangString affects its hash value.
    """
    mls1 = MultiLangString(*sample_langstrings, preferred_lang="en")
    hash_before = hash(mls1)
    mls1.add(LangString("New text", "en"))
    hash_after = hash(mls1)
    assert hash_before != hash_after, "Modifying the contents of a MultiLangString should change its hash value."


def test_hash_with_empty_multilangstring():
    """
    Test the hash value of an empty MultiLangString.
    """
    mls = MultiLangString(preferred_lang="en")
    assert isinstance(hash(mls), int), "Hash of an empty MultiLangString should still be an integer."
