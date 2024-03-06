import pytest
from langstring import MultiLangString


@pytest.fixture
def sample_mls():
    """Fixture to provide a MultiLangString instance with predefined languages and texts."""
    return MultiLangString(mls_dict={"en": {"Hello", "World"}, "fr": {"Bonjour", "Monde"}, "es": {"Hola", "Mundo"}})


@pytest.mark.parametrize(
    "lang_to_remove",
    [
        "es",
        "fr",
        "en",
        "En",
        "EN",
    ],
)
def test_remove_existing_language(sample_mls: MultiLangString, lang_to_remove: str):
    """Test removing languages that exist in the MultiLangString with different cases.

    :param sample_mls: A MultiLangString instance for testing.
    :param lang_to_remove: The language code to be removed from the MultiLangString.
    """
    sample_mls.remove_lang(lang_to_remove)
    assert lang_to_remove not in sample_mls.mls_dict, "Failed to remove existing language 'fr'."
    assert len(sample_mls.mls_dict) == 2, "Other two langs are not still in dictionary."


@pytest.mark.parametrize(
    "lang_to_remove",
    [
        "de",
        " en",
        "en ",
        " en ",
        "ru",
        "it",
        "DA",
        "",  # Empty string
        "   ",  # Spaces only
        "ελ",  # Greek
        "рус",  # Cyrillic
        "🚀",  # Emoji
        "<script>",
        "\n",  # Newline character
        "\t",  # Tab character
    ],
)
def test_remove_nonexistent_language(sample_mls: MultiLangString, lang_to_remove: str):
    """Test attempting to remove languages that do not exist in the MultiLangString with different cases.

    :param sample_mls: A MultiLangString instance for testing.
    :param lang_to_remove: The language code attempted to be removed from the MultiLangString.
    :param expected_error_message: The expected error message for the nonexistent language removal attempt.
    """
    with pytest.raises(ValueError, match=f"Lang '{lang_to_remove}' not found in the MultiLangString."):
        sample_mls.remove_lang(lang_to_remove)
    assert len(sample_mls.mls_dict) == 3, "Not all langs are not still in dictionary."


def test_remove_lang_affects_only_target_language(sample_mls: MultiLangString):
    """Ensure removing a language only affects the targeted language, not others.

    :param sample_mls: A MultiLangString instance for testing.
    """
    before_remove = sample_mls.mls_dict.copy()
    sample_mls.remove_lang("en")
    before_remove.pop("en")
    assert sample_mls.mls_dict == before_remove, "Removing one language affected others."


def test_remove_language_from_empty_mls():
    """Test removing a language from an empty MultiLangString instance."""
    mls = MultiLangString()
    with pytest.raises(ValueError, match="Lang 'any' not found in the MultiLangString."):
        mls.remove_lang("any")


@pytest.mark.parametrize("invalid_lang", [None, 123, [], {}])
def test_remove_lang_with_invalid_type(sample_mls: MultiLangString, invalid_lang):
    """Test attempting to remove a language using an invalid type for `lang`.

    :param sample_mls: A MultiLangString instance for testing.
    :param invalid_lang: An invalid language identifier to test type validation.
    """
    with pytest.raises(TypeError, match=f"Argument .+ must be of type 'str', but got"):
        sample_mls.remove_lang(invalid_lang)


def test_remove_lang_with_empty_string(sample_mls: MultiLangString):
    """Test attempting to remove a language using an empty string for `lang`.

    :param sample_mls: A MultiLangString instance for testing.
    """
    with pytest.raises(ValueError, match="Lang '' not found in the MultiLangString."):
        sample_mls.remove_lang("")


def test_remove_lang_operation_on_itself(sample_mls: MultiLangString):
    """Test removing a language affects the instance itself and verifies internal state.

    :param sample_mls: A MultiLangString instance for testing.
    """
    sample_mls.remove_lang("es")
    assert "es" not in sample_mls.mls_dict, "Removing a language should affect the instance itself."
