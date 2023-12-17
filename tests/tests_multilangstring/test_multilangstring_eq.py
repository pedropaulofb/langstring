import pytest

from langstring import LangString
from langstring import MultiLangString


@pytest.fixture
def sample_langstrings_eq() -> list[LangString]:
    """Fixture to provide sample LangString objects for testing."""
    return [LangString("Hello", "en"), LangString("Hola", "es"), LangString("Bonjour", "fr")]


def test_equality_with_identical_multilangstrings(sample_langstrings_eq) -> None:
    """Test equality of two MultiLangString objects with identical langstrings and preferred_lang.

    :param sample_langstrings: Fixture providing sample LangString objects.
    :return: Asserts that two identical MultiLangString objects are equal.
    """
    mls1 = MultiLangString(*sample_langstrings_eq, preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings_eq, preferred_lang="en")
    assert mls1 == mls2, "MultiLangString objects with identical langstrings and preferred_lang should be equal."


def test_inequality_with_different_langstrings(sample_langstrings_eq) -> None:
    """Test inequality of two MultiLangString objects with different langstrings.

    :param sample_langstrings: Fixture providing sample LangString objects.
    :return: Asserts that MultiLangString objects with different langstrings are not equal.
    """
    mls1 = MultiLangString(sample_langstrings_eq[0], preferred_lang="en")
    mls2 = MultiLangString(sample_langstrings_eq[1], preferred_lang="en")
    assert mls1 != mls2, "MultiLangString objects with different langstrings should not be equal."


def test_equality_with_different_preferred_lang(sample_langstrings_eq) -> None:
    """Test equality of two MultiLangString objects with different preferred_lang.

    With the updated logic, different preferred_lang values do not affect equality.
    This test checks that two MultiLangString objects with the same langstrings but different preferred_lang
    are considered equal.

    :param sample_langstrings: Fixture providing sample LangString objects.
    :return: Asserts that MultiLangString objects with different preferred_lang are equal.
    """
    mls1 = MultiLangString(sample_langstrings_eq[0], preferred_lang="en")
    mls2 = MultiLangString(sample_langstrings_eq[0], preferred_lang="es")
    assert mls1 == mls2, "MultiLangString objects with different preferred_lang should be equal."


def test_inequality_with_non_multilangstring_object(sample_langstrings_eq) -> None:
    """Test inequality of a MultiLangString object compared with a non-MultiLangString object.

    :param sample_langstrings: Fixture providing sample LangString objects.
    :return: Asserts that a MultiLangString object is not equal to a non-MultiLangString object.
    """
    mls = MultiLangString(sample_langstrings_eq[0], preferred_lang="en")
    non_mls = "Hello"
    assert mls != non_mls, "MultiLangString object should not be equal to a non-MultiLangString object."


def test_equality_with_different_control_values(sample_langstrings_eq) -> None:
    """Test equality of two MultiLangString objects with different control values but identical langstrings and \
    preferred_lang.

    :param sample_langstrings: Fixture providing sample LangString objects.
    :return: Asserts that MultiLangString objects with different control values but identical langstrings and \
    preferred_lang are equal.
    """
    mls1 = MultiLangString(*sample_langstrings_eq, control="ALLOW", preferred_lang="en")
    mls2 = MultiLangString(*sample_langstrings_eq, control="OVERWRITE", preferred_lang="en")
    assert mls1 == mls2, (
        "MultiLangString objects with different control values but identical langstrings and preferred_lang should "
        "be equal."
    )


def test_equality_with_empty_multilangstrings() -> None:
    """Test equality of two empty MultiLangString objects."""
    mls1 = MultiLangString()
    mls2 = MultiLangString()
    assert mls1 == mls2, "Empty MultiLangString objects should be equal."


def test_equality_with_partial_overlap_in_langstrings(sample_langstrings_eq) -> None:
    """Test equality of two MultiLangString objects with partial overlap in langstrings."""
    mls1 = MultiLangString(*sample_langstrings_eq[:2], preferred_lang="en")  # First two langstrings
    mls2 = MultiLangString(*sample_langstrings_eq[1:], preferred_lang="en")  # Last two langstrings
    assert mls1 != mls2, "MultiLangString objects with partial overlap in langstrings should not be equal."


def test_equality_with_different_order_of_addition(sample_langstrings_eq) -> None:
    """Test equality of two MultiLangString objects with langstrings added in different order."""
    mls1 = MultiLangString(*sample_langstrings_eq, preferred_lang="en")
    mls2 = MultiLangString(*reversed(sample_langstrings_eq), preferred_lang="en")
    assert mls1 == mls2, "MultiLangString objects with same langstrings in different order should be equal."


def test_equality_with_null_or_invalid_inputs() -> None:
    """Test equality of MultiLangString objects when null or invalid inputs are provided."""
    mls1 = MultiLangString(LangString("", "en"), LangString("Hello", None))
    mls2 = MultiLangString(LangString("", "en"), LangString("Hello", None))
    assert mls1 == mls2, "MultiLangString objects with null or invalid inputs should be equal."

    # Testing with invalid language tag
    mls3 = MultiLangString(LangString("Hello", "invalid-lang-tag"))
    mls4 = MultiLangString(LangString("Hello", "invalid-lang-tag"))
    assert mls3 == mls4, "MultiLangString objects with invalid language tags should be equal."
