from typing import Optional
from typing import Union

import pytest

from langstring.utils.validator import Validator


# Fixture for the decorated function
@pytest.fixture
def decorated_func():
    # Test function to be decorated with Union type
    def test_func(arg1: Union[int, str], arg2: Union[str, bool], arg3: Optional[bool] = None):
        return f"{arg1}, {arg2}, {arg3}"

    # Return the decorated function
    return Validator.validate_type_decorator(test_func)


def test_validate_simple_type_with_correct_types(decorated_func):
    """Test validate_simple_type with correct argument types."""
    assert decorated_func(1, "test", True) == "1, test, True", "Should pass with correct types"


def test_validate_simple_type_with_incorrect_type(decorated_func):
    """Test validate_simple_type with incorrect argument type."""
    with pytest.raises(TypeError, match="Argument '2' must be of type '<class 'str'>'"):
        decorated_func(1, 2)


def test_validate_simple_type_with_missing_optional_arg(decorated_func):
    """Test validate_simple_type with a missing optional argument."""
    assert decorated_func(1, "test") == "1, test, None", "Should pass with missing optional argument"


def test_validate_simple_type_with_none_for_optional_arg(decorated_func):
    """Test validate_simple_type with None passed for an optional argument."""
    assert decorated_func(1, "test", None) == "1, test, None", "Should pass with None for optional argument"


def test_validate_simple_type_with_extra_keyword_arg(decorated_func):
    """Test validate_simple_type with an extra keyword argument."""
    with pytest.raises(TypeError, match="got an unexpected keyword argument 'arg4'"):
        decorated_func(1, "test", arg4="extra")


def test_validate_simple_type_with_no_arguments(decorated_func):
    """Test validate_simple_type with no arguments passed."""
    with pytest.raises(TypeError, match="missing 2 required positional arguments"):
        decorated_func()


def test_validate_simple_type_with_empty_string(decorated_func):
    """Test validate_simple_type with an empty string argument."""
    with pytest.raises(TypeError, match="Argument '' must be of type '<class 'int'>'"):
        decorated_func("", "")


def test_validate_simple_type_with_none(decorated_func):
    """Test validate_simple_type with None as an argument."""
    with pytest.raises(TypeError, match="Argument 'None' must be of type '<class 'int'>'"):
        decorated_func(None, "test")


def test_validate_simple_type_with_unusual_valid_usage(decorated_func):
    """Test validate_simple_type with unusual but valid usage."""
    # Example: passing a boolean as a string
    assert decorated_func(1, "True") == "1, True, None", "Should pass with unusual but valid usage"


def test_validate_simple_type_with_incorrect_type(decorated_func):
    """Test validate_simple_type with incorrect argument type."""
    with pytest.raises(TypeError, match="Argument '1.5' must be of type"):
        decorated_func(1.5, "test")


def test_validate_simple_type_with_empty_string(decorated_func):
    """Test validate_simple_type with an empty string argument."""
    # Empty string is valid for arg1 (Union[int, str])
    assert decorated_func("", "test") == ", test, None", "Should pass with empty string for Union type"


def test_validate_simple_type_with_none(decorated_func):
    """Test validate_simple_type with None as an argument."""
    with pytest.raises(TypeError, match="Argument 'None' must be of types .+, but got"):
        decorated_func(None, "test")
