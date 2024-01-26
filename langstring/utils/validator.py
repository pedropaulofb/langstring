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
import warnings
from enum import Enum
from typing import Optional

from ..controller import Controller
from ..flags import GlobalFlag
from .non_instantiable import NonInstantiable


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
                        str(e)
                        + ". VALID_LANG functionality requires the 'langcodes' library. Install it with 'pip install langstring[extras]'."
                    )
                    raise ImportError(error_message) from e
                else:
                    warnings.warn(
                        "Language validation skipped. VALID_LANG functionality requires the 'langcodes' library. "
                        "Install it with 'pip install langstring[extras]' to enable this feature.",
                        UserWarning,
                    )

        lang = lang if not Controller.get_flag(flag_type.STRIP_LANG) else lang.strip()
        return lang if not Controller.get_flag(flag_type.LOWERCASE_LANG) else lang.casefold()
