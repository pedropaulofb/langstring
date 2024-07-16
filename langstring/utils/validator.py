"""This module defines the Validator class.
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

    @classmethod
    def validate_flags_text(cls, flag_type: type[Enum], text: Optional[str]) -> str:
        cls.validate_type_single(flag_type, type)
        cls.validate_type_single(text, str, optional=True)

        # Initial message for potential errors
        original_text = text
        msg = f"Invalid 'text' value received ('{original_text}')."

        # Transform the text string according to STRIP_TEXT flag
        if text is not None:
            text = text.strip() if Controller.get_flag(flag_type.STRIP_TEXT) else text  # Apply STRIP_TEXT if enabled
            validate_text = text.strip()  # Remove 'whitespace characters' for validation
        else:
            validate_text = None

        if Controller.get_flag(flag_type.DEFINED_TEXT) and not validate_text:
            raise ValueError(f"{msg} '{flag_type.__name__}.DEFINED_TEXT' is enabled. "
                             f"Expected non-empty 'str' or 'str' with non-space characters.")

        return text

    @staticmethod
    def validate_flags_lang(flag_type: type[Enum], lang: Optional[str]) -> str:
        Validator.validate_type_single(flag_type, type)
        Validator.validate_type_single(lang, str, optional=True)

        # Initial message for potential errors
        original_lang = lang
        msg = f"Invalid 'lang' value received ('{original_lang}')."

        # Transform the lang string according to STRIP_LANG and LOWERCASE_LANG flags
        if lang is not None:
            lang = lang.strip() if Controller.get_flag(flag_type.STRIP_LANG) else lang  # Apply STRIP_LANG if enabled
            transformed_lang = lang.casefold() if Controller.get_flag(
                flag_type.LOWERCASE_LANG) else lang  # Apply LOWERCASE_LANG if enabled
            validate_lang = transformed_lang.strip()  # Remove 'whitespace characters' for validation
        else:
            transformed_lang = None
            validate_lang = None

        if Controller.get_flag(flag_type.DEFINED_LANG) and not validate_lang:
            raise ValueError(f"{msg} '{flag_type.__name__}.DEFINED_LANG' is enabled. "
                             f"Expected non-empty 'str' or 'str' with non-space characters.")

        # Validation is performed on the transformed language string
        if Controller.get_flag(flag_type.VALID_LANG):
            try:
                from langcodes import tag_is_valid

                if not tag_is_valid(transformed_lang):
                    raise ValueError(
                        f"Invalid 'lang' value received ('{original_lang}'). '{flag_type.__name__}.VALID_LANG' is enabled. "
                        f"Expected valid language code."
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

        return transformed_lang

    @staticmethod
    def _check_arg(arg: Any, hint: type[Any]) -> bool:
        """Check if the argument matches the type hint."""
        origin = get_origin(hint)
        args = get_args(hint)

        if origin is Union:
            if not any(isinstance(arg, t) for t in args):
                allowed_types = " or ".join(f"'{t.__name__}'" for t in args)
                raise TypeError(
                    f"Invalid argument with value '{arg}'. Expected one of {allowed_types}, but got '{type(arg).__name__}'."
                )
            return True

        if origin is not None:  # This handles parameterized generics like list[int]
            if not isinstance(arg, origin):
                raise TypeError(
                    f"Invalid argument with value '{arg}'. Expected '{origin.__name__}', but got '{type(arg).__name__}'."
                )
            if args:
                if origin in (list, set, tuple):
                    for item in arg:
                        if not any(isinstance(item, arg_type) for arg_type in args):
                            allowed_types = " or ".join(f"'{t.__name__}'" for t in args)
                            raise TypeError(
                                f"Invalid item with value '{item}' in '{origin.__name__}'. "
                                f"Expected one of {allowed_types}, but got '{type(item).__name__}'."
                            )
            return True

        if not isinstance(arg, hint):
            raise TypeError(
                f"Invalid argument with value '{arg}'. Expected '{hint.__name__}', but got '{type(arg).__name__}'."
            )

        return True

    @classmethod
    def validate_type_decorator(cls, func: Callable[..., T]) -> Callable[..., T]:
        """
                Decorator to validate the types of arguments passed to a function or method based on their type hints.

                This method checks if each argument's type matches its corresponding type hint. It is intended for use with
                functions or instance methods where explicit type hints are provided for all arguments.

                Usage:
                    - Apply this decorator to functions or instance methods that require type validation based on type hints.

                When to Use:
                    - Use this decorator for functions or methods where argument types need to be strictly validated.
                    - Suitable for validating primitive types (int, str, float, bool, etc.), Optional types, and Union types.
                    - Useful for parameterized generics like List[int], Set[str], etc., to ensure both the container and
                      its contents match the specified types.
                    - Appropriate for instance methods, adjusting for the 'self' parameter automatically.
                    - Suitable for static methods but requires manual validation for class methods and setters.

                When Not to Use:
                    - Do not use this decorator for class methods with the 'cls' parameter, as it does not handle 'cls' explicitly.
                    - Avoid using this decorator for property setters.
                    - This decorator is not suitable for methods with parameters involving generic collections parameterized
                      with type variables (e.g., List[T] where T is a type variable).
                    - Complex nested generics (e.g., List[Dict[str, Union[int, List[str]]]]) might not be fully validated.
                    - Specifically, cases like `(["test", 1], list, False)` (List with mixed types) are out of scope and will not be correctly validated by this decorator.

                :param func: The function or method to be decorated.
                :type func: Callable[..., T]
                :return: The decorated function or method with type validation applied.
                :rtype: Callable[..., T]
                :raises TypeError: If an argument's type does not match its type hint.
                """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            type_hints = {k: v for k, v in get_type_hints(func).items() if k != "return"}
            param_names = list(inspect.signature(func).parameters)
            is_instance_method = "self" in param_names and len(args) > 0 and isinstance(args[0], args[0].__class__)
            if is_instance_method:
                param_names.remove("self")
                type_hints.pop("self", None)
                args_to_check = args[1:]
            else:
                args_to_check = args
            for arg, (name, hint) in zip(args_to_check, zip(param_names, type_hints.values())):
                if not Validator._check_arg(arg, hint):
                    raise TypeError(
                        f"Invalid argument with value '{arg}'. Expected '{hint.__name__}', but got '{type(arg).__name__}'."
                    )
            for kwarg, hint in type_hints.items():
                if kwarg in kwargs and not Validator._check_arg(kwargs[kwarg], hint):
                    raise TypeError(
                        f"Invalid argument with value '{kwarg}'. Expected '{hint.__name__}', but got '{type(kwargs[kwarg]).__name__}'."
                    )
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def validate_type_single(arg: Any, arg_exp_type: type, optional: bool = False) -> None:
        if optional and arg is None:
            return

        if not isinstance(arg, arg_exp_type):
            raise TypeError(
                f"Invalid argument with value '{arg}'. "
                f"Expected '{arg_exp_type.__name__}', but got '{type(arg).__name__}'."
            )

    @classmethod
    def validate_type_iterable(
        cls, arg: Any, arg_exp_type: type, arg_content_exp_type: type, optional: bool = False
    ) -> None:
        if optional and arg is None:
            return
        cls.validate_type_single(arg, arg_exp_type)
        for elem in arg:
            cls.validate_type_single(elem, arg_content_exp_type)
