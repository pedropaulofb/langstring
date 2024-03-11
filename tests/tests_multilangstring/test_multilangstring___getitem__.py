import pytest

from langstring import MultiLangString


@pytest.mark.parametrize(
    "lang, expected_set",
    [
        ("en", {"Hello World"}),  # Existing language
        ("EN", {"Hello World"}),  # Existing language
        ("es", {"Hola Mundo"}),  # Another existing language
        ("Es", {"Hola Mundo"}),  # Another existing language
    ],
)
def test_getitem_valid(lang: str, expected_set: set):
    """
    Test retrieval of valid language entries.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    assert mls[lang] == expected_set, f"Retrieving '{lang}' should return {expected_set}"


@pytest.mark.parametrize(
    "lang",
    [
        ("fr"),  # Non-existent language
        ("de"),  # Another non-existent language
        ("en "),
        ("en "),
        (" en "),
        ("ελ"),
        ("рус"),
        ("emoji"),
    ],
)
def test_getitem_key_error(lang: str):
    """
    Test that accessing non-existent language raises KeyError.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    with pytest.raises(KeyError, match=f".*{lang}.*"):
        _ = mls[lang]


@pytest.mark.parametrize(
    "lang",
    [
        (123),  # Integer
        (None),  # NoneType
        (["en"]),  # List
        ({}),  # Dictionary
        (set()),  # Empty set
    ],
)
def test_getitem_type_error(lang):
    """
    Test that providing an invalid type for language raises TypeError.
    """
    mls = MultiLangString(mls_dict={"en": {"Hello World"}, "es": {"Hola Mundo"}})
    with pytest.raises(TypeError):
        _ = mls[lang]
