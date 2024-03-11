import pytest

from langstring import MultiLangString


@pytest.mark.parametrize(
    "mls_dict, expected_exception, expected_message",
    [
        ({"en": ["Hello", "World"]}, TypeError, "Invalid 'texts' type in mls_dict init. Expected 'set', got 'dict'."),
        ({"en-US": "Not a set"}, TypeError, "Invalid 'texts' type in mls_dict init. Expected 'set', got 'dict'."),
        (
            {"nested": {"key": {"Nested": "dict"}}},
            TypeError,
            "Invalid 'texts' type in mls_dict init. Expected 'set', got 'dict'.",
        ),
        (123, TypeError, "Invalid type of 'mls_dict' received. Expected 'dict', got 'int'."),
        ([("en", {"Hello"})], TypeError, "Invalid type of 'mls_dict' received. Expected 'dict', got 'list'."),
        # Adding cases with invalid 'texts' types (tuple, int, None) and invalid 'lang' types (int, list)
        ({"en": (1, 2)}, TypeError, "Invalid 'texts' type in mls_dict init. Expected 'set', got"),
        (1, TypeError, "Invalid type of 'mls_dict' received. Expected 'dict', got"),
        ({"en": 100}, TypeError, "Invalid 'texts' type in mls_dict init. Expected 'set', got"),
        ({"en": None}, TypeError, "Invalid 'texts' type in mls_dict init. Expected 'set', got"),
        ({1: {"One", "Two"}}, TypeError, "Invalid 'lang' type in mls_dict init. Expected 'str', got"),
    ],
)
def test_validate_input_mls_dict_errors(mls_dict: dict, expected_exception: Exception, expected_message: str) -> None:
    """
    Test _validate_input_mls_dict for various error scenarios including invalid types and structures.

    :param mls_dict: Dictionary to validate.
    :param expected_exception: The type of exception expected to be raised.
    :param expected_message: Expected message in the raised exception.
    :raises AssertionError: If the function does not raise the expected exception or if the exception message does not match.
    """
    mls = MultiLangString()
    with pytest.raises(expected_exception, match=expected_message):
        mls._validate_input_mls_dict(mls_dict)


@pytest.mark.parametrize(
    "mls_dict",
    [
        ({"en": {"Hello", "World"}}),
        ({"en-US": {"A valid set"}, "fr-FR": {"Un ensemble valide"}}),
        ({}),  # Empty dictionary
        ({"zh": {"你好", "世界"}, "ar": {"مرحبا", "عالم"}}),
        ({"en": set(), "fr": set()}),  # Empty sets
        ({"mixedCase": {"Mixed", "Case"}, "NUM123": {"Numbers", "123"}}),
        ({"русский": {"Привет", "Мир"}, "ελληνικά": {"Γειά", "Κόσμος"}}),
        ({"emojis": {"😊", "🚀", "🌍"}}),
        ({"special chars": {"!@#$%", "^&*()"}}),
    ],
)
def test_validate_input_mls_dict_success(mls_dict: dict) -> None:
    """
    Test _validate_input_mls_dict for valid input scenarios, ensuring it accepts correctly structured dictionaries.

    :param mls_dict: Dictionary to validate.
    """
    mls = MultiLangString()
    try:
        mls._validate_input_mls_dict(mls_dict)
        no_exception_raised = True
    except Exception:
        no_exception_raised = False
    assert no_exception_raised, f"Validation should pass without exceptions for valid mls_dict: {mls_dict}"
