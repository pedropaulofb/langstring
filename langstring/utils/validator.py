"""This module defines the Validator class.

The Validator provides validation functionalities for LangString and MultiLangString classes.
It includes methods to validate argument types, ensure text and language requirements, and check the validity of
language tags based on configurable control flags.

The mixin is designed to be used with classes that handle language strings and need to enforce specific validation
rules. It leverages control flags from a control class (like Controller or Controller) to
determine the validation behavior.

Classes:
    Validator: A mixin class providing validation methods for LangString and MultiLangString classes.

Example Usage:
    class LangString(Validator):
        # LangString implementation
        ...

    class MultiLangString(Validator):
        # MultiLangString implementation
        ...
"""

import inspect
import warnings
from enum import Enum
from functools import wraps
from typing import Any
from typing import Callable
from typing import get_args
from typing import get_origin
from typing import get_type_hints
from typing import Optional
from typing import TypeVar
from typing import Union

from ..controller import Controller
from ..flags import GlobalFlag
from .non_instantiable import NonInstantiable

T = TypeVar("T")


class Validator(metaclass=NonInstantiable):
    """A mixin class that provides validation methods for classes handling language strings.

    It ensures that the text and language arguments meet specific criteria, such as type correctness, non-emptiness,
    and language tag validity. The validation rules are determined by control flags from a control class.
    """

    @staticmethod
    def validate_text(flag_type: type[Enum], text: Optional[str]) -> str:
        msg = f"Invalid 'text' value received ('{text}')."
        if not isinstance(text, str):
            raise TypeError(f"{msg} Expected 'str', got '{type(text).__name__}'.")

        if Controller.get_flag(flag_type.DEFINED_TEXT) and not text:
            print(Controller.get_flag(flag_type.DEFINED_TEXT))
            raise ValueError(f"{msg} '{flag_type.__name__}.DEFINED_TEXT' is enabled. Expected non-empty 'str'.")

        return text if not Controller.get_flag(flag_type.STRIP_TEXT) else text.strip()

    @staticmethod
    def validate_lang(flag_type: type[Enum], lang: Optional[str]) -> str:
        msg = f"Invalid 'lang' value received ('{lang}')."

        if not isinstance(lang, str):
            raise TypeError(f"{msg} Expected 'str', got '{type(lang).__name__}'.")

        if Controller.get_flag(flag_type.DEFINED_LANG) and not lang:
            raise ValueError(f"{msg} '{flag_type.__name__}.DEFINED_LANG' is enabled. Expected non-empty 'str'.")

        # Validation is performed on lowercase language, according to RDF definition
        if Controller.get_flag(flag_type.VALID_LANG):
            try:
                from langcodes import tag_is_valid

                if not tag_is_valid(lang.casefold()):
                    raise ValueError(
                        f"{msg} '{flag_type.__name__}.VALID_LANG' is enabled. Expected valid language code."
                    )
            except ImportError as e:
                if Controller.get_flag(GlobalFlag.ENFORCE_EXTRA_DEPEND):
                    error_message = (
                        str(e) + ". VALID_LANG functionality requires the 'langcodes' library. "
                        "Install it with 'pip install langstring[extras]'."
                    )
                    raise ImportError(error_message) from e

                warnings.warn(
                    "Language validation skipped. VALID_LANG functionality requires the 'langcodes' library. "
                    "Install it with 'pip install langstring[extras]' to enable this feature.",
                    UserWarning,
                )

        lang = lang if not Controller.get_flag(flag_type.STRIP_LANG) else lang.strip()
        return lang if not Controller.get_flag(flag_type.LOWERCASE_LANG) else lang.casefold()

    @classmethod
    def validate_simple_type(cls, func: Callable[..., T]) -> Callable[..., T]:
        """Validate the types of arguments passed to a function or method based on their type hints. Used as decorator.

        This method checks if each argument's type matches its corresponding type hint. It is intended for use with
        functions or class methods where explicit type hints are provided for all arguments.

        Note:
            This decorator is designed for use with functions, instance methods, and static methods where explicit
            type hints are provided for all arguments. It automatically adjusts for the 'self' parameter in instance
            methods. However, it is not suitable for class methods or setters in classes, as it does not handle
            the 'cls' parameter in class methods and may lead to incorrect behavior with setters. For class methods
            and setters, manual type validation is recommended.

            The decorator should not be used with methods that have parameters of generic types, such as `list`, `set`,
            or other collections that are parameterized with type variables (e.g., `list[str]` or `set[MyClass]`).
            This limitation stems from the dynamic nature of generic types in Python, which can lead to runtime errors
            when attempting to check against a parameterized type. Therefore, it is recommended to avoid applying this
            decorator to methods where the parameters or return types involve generic collections directly.

        :param func: The function or method to be decorated.
        :type func: Callable[..., T]
        :return: The decorated function or method with type validation applied.
        :rtype: Callable[..., T]
        :raises TypeError: If an argument's type does not match its type hint.
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Get type hints of the function (excluding 'return')
            type_hints = {k: v for k, v in get_type_hints(func).items() if k != "return"}
            param_names = list(inspect.signature(func).parameters)

            # Determine if the function is an instance method
            is_instance_method = "self" in param_names and len(args) > 0 and isinstance(args[0], args[0].__class__)

            # Skip 'self' in type checking if it's an instance method
            if is_instance_method:
                param_names.remove("self")
                type_hints.pop("self", None)
                args_to_check = args[1:]  # Adjust args to exclude 'self'
            else:
                args_to_check = args

            # Function to check if the argument matches the type hint
            def check_arg(arg: Any, hint: type[Any]) -> bool:
                """Check if the argument matches the type hint."""
                if get_origin(hint) is Union:
                    if not any(isinstance(arg, t) for t in get_args(hint)):
                        allowed_types = " or ".join(f"'{t.__name__}'" for t in get_args(hint))
                        raise TypeError(
                            f"Argument '{arg}' must be of types {allowed_types}, but got '{type(arg).__name__}'."
                        )
                    return True

                if not isinstance(arg, hint):
                    raise TypeError(
                        f"Argument '{arg}' must be of type '{hint.__name__}', but got '{type(arg).__name__}'."
                    )

                return True

            # Validate positional arguments
            for arg, (name, hint) in zip(args_to_check, zip(param_names, type_hints.values())):
                if not check_arg(arg, hint):
                    raise TypeError(f"Argument '{arg}' must be of type '{hint}', but got '{type(arg)}'.")

            # Validate keyword arguments
            for kwarg, hint in type_hints.items():
                if kwarg in kwargs and not check_arg(kwargs[kwarg], hint):
                    raise TypeError(f"Argument '{kwarg}' must be of type '{hint}', but got '{type(kwargs[kwarg])}'.")

            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def _get_origin(tp: Any) -> Any:
        return getattr(tp, "__origin__", None)

    @staticmethod
    def _get_args(tp: Any) -> tuple[Any, ...]:
        return getattr(tp, "__args__", ())
