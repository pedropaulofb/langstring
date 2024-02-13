from langstring import MultiLangString


def test_multilangstring_eq_with_identical_objects():
    """
    Test if two MultiLangString objects with identical content are considered equal.
    """
    mls1 = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    mls2 = MultiLangString(mls_dict={"en": {"Hello"}, "fr": {"Bonjour"}})
    assert mls1 == mls2, "Two MultiLangString objects with identical content should be equal"


def test_multilangstring_eq_with_different_objects():
    """
    Test if two MultiLangString objects with different content are not considered equal.
    """
    mls1 = MultiLangString(mls_dict={"en": {"Hello"}})
    mls2 = MultiLangString(mls_dict={"fr": {"Bonjour"}})
    assert mls1 != mls2, "Two MultiLangString objects with different content should not be equal"


def test_multilangstring_eq_with_different_types():
    """
    Test if a MultiLangString object is not considered equal to an object of a different type.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    other = "Not a MultiLangString"
    assert mls != other, "A MultiLangString object should not be equal to an object of a different type"


def test_multilangstring_eq_with_self():
    """
    Test if a MultiLangString object is considered equal to itself.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert mls == mls, "A MultiLangString object should be equal to itself"


def test_multilangstring_eq_with_none():
    """
    Test if a MultiLangString object is not considered equal to None.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello"}})
    assert mls != None, "A MultiLangString object should not be equal to None"
