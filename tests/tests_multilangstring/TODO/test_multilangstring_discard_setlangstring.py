import pytest

from langstring import MultiLangString
from langstring import SetLangString


@pytest.mark.parametrize(
    "initial_contents, setlangstring, expected_contents",
    [
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
            SetLangString({"Hello"}, "en"),
            {"en": {"World"}, "fr": {"Bonjour"}},
        ),
        (
            {"en": {"Hello"}, "fr": {"Bonjour", "Salut"}},
            SetLangString({"Bonjour"}, "fr"),
            {"en": {"Hello"}, "fr": {"Salut"}},
        ),
        (
            {"en": {"Hello"}},
            SetLangString({"Goodbye"}, "en"),
            {"en": {"Hello"}},
        ),  # Attempt to discard non-existing text
        ({}, SetLangString({"Hello"}, "en"), {}),  # Discard from an empty MultiLangString
        (
            {"en": {"Hello", "World"}, "es": {"Hola", "Mundo"}},
            SetLangString({"World"}, "en"),
            {"en": {"Hello"}, "es": {"Hola", "Mundo"}},
        ),  # Discarding one of multiple texts in a language
        (
            {"en": {"Hello", "World"}, "es": {"Hola"}},
            SetLangString({"Hello", "World"}, "en"),
            {"en": set(), "es": {"Hola"}},
        ),  # Discarding all texts in a language
    ],
)
def test_discard_setlangstring_various_scenarios(initial_contents, setlangstring, expected_contents):
    """
    Test the `discard_setlangstring` method across various scenarios, including discarding existing and non-existing texts.

    :param initial_contents: Initial contents of the MultiLangString instance.
    :param setlangstring: The SetLangString to discard.
    :param expected_contents: Expected contents of the MultiLangString after discarding.
    """
    mls = MultiLangString(initial_contents)
    mls.discard_setlangstring(setlangstring)
    assert (
        mls.mls_dict == expected_contents
    ), "MultiLangString contents did not match expected after discarding SetLangString."


def test_discard_setlangstring_with_invalid_type():
    """
    Test that passing an invalid type to `discard_setlangstring` raises a TypeError.
    """
    mls = MultiLangString({"en": {"Hello"}})
    with pytest.raises(TypeError, match="Argument '.+' must be of type 'SetLangString', but got"):
        mls.discard_setlangstring("not a SetLangString")  # Invalid type passed


@pytest.mark.parametrize(
    "initial_contents, setlangstring, clean_empty, expected_contents",
    [
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour", "Salut"}},
            SetLangString({"Bonjour", "Salut"}, "fr"),
            True,
            {"en": {"Hello", "World"}},
        ),
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour", "Salut"}},
            SetLangString({"Bonjour", "Salut"}, "fr"),
            False,
            {"en": {"Hello", "World"}, "fr": set()},
        ),
    ],
)
def test_discard_setlangstring_with_flags_effect(initial_contents, setlangstring, clean_empty, expected_contents):
    """
    Test the `discard_setlangstring` method considering the effect of flags that may influence its behavior,
    specifically testing the scenario where empty languages might be cleared based on flag settings.

    :param initial_contents: Initial contents of the MultiLangString instance.
    :param setlangstring: The SetLangString to discard.
    :param clean_empty: Boolean indicating if the flag to clear empty languages is active.
    :param expected_contents: Expected contents of the MultiLangString post-operation.
    """
    mls = MultiLangString(initial_contents)
    mls.discard_setlangstring(setlangstring, clean_empty)

    assert (
        mls.mls_dict == expected_contents
    ), "Contents after discarding SetLangString with flag effect did not match expectations."
