from functools import wraps
from typing import Any, Optional, List, Callable
import pytest
from langstring.utils.validator import Validator

@pytest.mark.parametrize("arg, hint, expected", [
    (1, int, True),
    ("test", str, True),
    (3.14, float, True),
    (True, bool, True),
    (None, Optional[int], True),
    (None, int, False),
    # Additional cases
    ("", str, True),  # Empty string
    ("   ", str, True),  # String with spaces
    ("Test", str, True),  # Capitalized string
    ("TEST", str, True),  # Uppercase string
    ("TeSt", str, True),  # Mixed case string
    ("тест", str, True),  # Cyrillic string
    ("δοκιμή", str, True),  # Greek string
    ("😀", str, True),  # Emoji
    ("test!", str, True),  # String with special character
    ([], list, True),  # Empty list
    ([""], list, True),  # List with empty string
    (["test"], list, True),  # List with one string
    (["test", ""], list, True),  # List with string and empty string
    ("test\ttest", str, True),  # String with tab character
    ("test\ntest", str, True),  # String with newline character
])
def test_check_arg_valid_cases(arg: Any, hint: type, expected: bool) -> None:
    """Test Validator._check_arg with valid cases.

    :param arg: The argument to check.
    :param hint: The type hint to check against.
    :param expected: The expected result.
    :return: None
    :raises: None
    """
    try:
        result = Validator._check_arg(arg, hint)
        assert result == expected, f"Expected {expected} but got {result} for arg: {arg} and hint: {hint}"
    except TypeError:
        assert not expected, f"Expected {expected} but got a TypeError for arg: {arg} and hint: {hint}"

def test_validate_type_decorator_with_valid_types() -> None:
    """Test Validator.validate_type_decorator with valid argument types.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: int, b: str) -> None:
        pass

    try:
        func(1, "test")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly!")

@pytest.mark.parametrize("args, kwargs, match", [
    ((1,), {"b": "test"}, None),
    ((1,), {"b": 2}, "Expected 'str', but got 'int'"),
    ((1.0,), {"b": "test"}, "Expected 'int', but got 'float'"),
    # Additional cases
    ((1,), {"b": ""}, None),  # Empty string
    ((1,), {"b": "   "}, None),  # String with spaces
    ((1,), {"b": "Test"}, None),  # Capitalized string
    ((1,), {"b": "TEST"}, None),  # Uppercase string
    ((1,), {"b": "TeSt"}, None),  # Mixed case string
    ((1,), {"b": "тест"}, None),  # Cyrillic string
    ((1,), {"b": "δοκιμή"}, None),  # Greek string
    ((1,), {"b": "😀"}, None),  # Emoji
    ((1,), {"b": "test!"}, None),  # String with special character
    ((1,), {"b": ["test", 1]}, "Expected 'str', but got 'list'"),  # List with mixed types
    ((1,), {"b": "test\ttest"}, None),  # String with tab character
    ((1,), {"b": "test\ntest"}, None),  # String with newline character
    ((1,), {"b": {"key": "value"}}, "Expected 'str', but got 'dict'"),  # Invalid type with dictionary
])
def test_validate_type_decorator_with_invalid_types(args: tuple, kwargs: dict, match: Optional[str]) -> None:
    """Test Validator.validate_type_decorator with invalid argument types.

    :param args: The positional arguments to pass to the function.
    :param kwargs: The keyword arguments to pass to the function.
    :param match: The expected error message.
    :return: None
    :raises: TypeError: If the argument types do not match the type hints.
    """
    @Validator.validate_type_decorator
    def func(a: int, b: str) -> None:
        pass

    if match:
        with pytest.raises(TypeError, match=match):
            func(*args, **kwargs)
    else:
        try:
            func(*args, **kwargs)
        except TypeError:
            pytest.fail("validate_type_decorator raised TypeError unexpectedly!")

def test_validate_type_decorator_instance_method() -> None:
    """Test Validator.validate_type_decorator on an instance method.

    :return: None
    :raises: None
    """
    class TestClass:
        @Validator.validate_type_decorator
        def instance_method(self, a: int, b: str) -> None:
            pass

    instance = TestClass()
    try:
        instance.instance_method(1, "test")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly on instance method!")

def test_validate_type_decorator_with_default_values() -> None:
    """Test Validator.validate_type_decorator with default argument values.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: int = 1, b: str = "default") -> None:
        pass

    try:
        func()
        func(2)
        func(3, "test")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with default values!")

def test_validate_type_decorator_with_empty_values() -> None:
    """Test Validator.validate_type_decorator with empty values.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: List[int]) -> None:
        pass

    try:
        func([])
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with empty values!")

def test_validate_type_decorator_with_null_values() -> None:
    """Test Validator.validate_type_decorator with null values.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: Optional[int]) -> None:
        pass

    try:
        func(None)
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with null values!")

def test_validate_type_decorator_with_optional_arguments() -> None:
    """Test Validator.validate_type_decorator with optional arguments.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: int, b: Optional[str] = None) -> None:
        pass

    try:
        func(1)
        func(1, "test")
        func(1, None)
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with optional arguments!")

def test_validate_type_decorator_with_keyword_arguments() -> None:
    """Test Validator.validate_type_decorator with keyword arguments.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: int, b: str) -> None:
        pass

    try:
        func(a=1, b="test")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with keyword arguments!")

def test_validate_type_decorator_with_unusual_but_valid_usage() -> None:
    """Test Validator.validate_type_decorator with unusual but valid usage.

    :return: None
    :raises: None
    """
    @Validator.validate_type_decorator
    def func(a: int, b: str = "test") -> None:
        pass

    try:
        func(1)
        func(1, "example")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with unusual but valid usage!")

def test_validate_type_decorator_with_nested_decorators() -> None:
    """Test Validator.validate_type_decorator with nested decorators.

    :return: None
    :raises: None
    """
    def example_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        return wrapper

    @example_decorator
    @Validator.validate_type_decorator
    def func(a: int, b: str) -> None:
        pass

    try:
        func(1, "test")
    except TypeError:
        pytest.fail("validate_type_decorator raised TypeError unexpectedly with nested decorators!")
