from typing import Any, Optional

import pytest

from langstring.utils.validator import Validator


@pytest.mark.parametrize("arg, hint, expected", [
    (1, int, True),
    ("test", str, True),
    (3.14, float, True),
    (None, Optional[int], True),
    (None, int, False)
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
    ((1.0,), {"b": "test"}, "Expected 'int', but got 'float'")
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

