from langstring import MultiLangString


def test_hash_equality_for_identical_multilangstrings():
    """
    Test if two MultiLangString objects with identical content have the same hash new_text.
    """
    mls1 = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    mls2 = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    assert hash(mls1) == hash(mls2), "Identical MultiLangString objects should have the same hash new_text"


def test_hash_inequality_for_different_multilangstrings():
    """
    Test if two MultiLangString objects with different content have different hash values.
    """
    mls1 = MultiLangString(mls_dict={"en": {"Hello"}})
    mls2 = MultiLangString(mls_dict={"fr": {"Bonjour"}})
    assert hash(mls1) != hash(mls2), "Different MultiLangString objects should have different hash values"


def test_hash_consistency_for_same_multilangstring():
    """
    Test if the hash new_text of a MultiLangString object remains consistent across calls.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    hash1 = hash(mls)
    hash2 = hash(mls)
    assert hash1 == hash2, "The hash new_text of a MultiLangString object should remain consistent across calls"
