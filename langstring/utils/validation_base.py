"""This module defines the ValidationBase class.

The ValidationBase provides validation functionalities for LangString and MultiLangString classes.
It includes methods to validate argument types, ensure text and language requirements, and check the validity of
language tags based on configurable control flags.

The mixin is designed to be used with classes that handle language strings and need to enforce specific validation
rules. It leverages control flags from a control class (like LangStringControl or MultiLangStringControl) to
determine the validation behavior.

Classes:
    ValidationBase: A mixin class providing validation methods for LangString and MultiLangString classes.

Example Usage:
    class LangString(ValidationBase):
        # LangString implementation
        ...

    class MultiLangString(ValidationBase):
        # MultiLangString implementation
        ...
"""
from abc import abstractmethod
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

from langcodes import tag_is_valid  # type: ignore

if TYPE_CHECKING:
    from ..langstring_control import LangStringControl, LangStringFlag
    from ..multilangstring_control import MultiLangStringControl, MultiLangStringFlag


class ValidationBase:
    """A mixin class that provides validation methods for classes handling language strings.

    It ensures that the text and language arguments meet specific criteria, such as type correctness, non-emptiness,
    and language tag validity. The validation rules are determined by control flags from a control class.
    """

    @abstractmethod
    def _get_control_and_flags_type(
        self,
    ) -> tuple[Union["LangStringControl", "MultiLangStringControl"], Union["LangStringFlag", "MultiLangStringFlag"]]:
        """Abstract method that must be implemented by subclasses.

        It should return the control class and its flags enumeration used for validation.
        This method is intended to be overridden in subclasses to return a tuple containing the specific control
        class and the corresponding flags enumeration. These are used for configuring and validating instances of
        the subclass. The exact types of the control class and flags enumeration will depend on the subclass.

        Subclasses should return:
            - The control class that manages configuration flags.
            - The flags enumeration that defines these flags.
        """

    def _validate_arguments(self, text: Optional[str], lang: Optional[str]) -> None:
        """Validate the types of the 'text' and 'lang' arguments.

        Ensures that 'text' is a string and 'lang' is either a string or None. Raises a TypeError if the types do not
        match the expected types. Additionally, checks if 'text' is not None.

        :param text: The text to be validated.
        :type text: Optional[str]
        :param lang: The language code to be validated.
        :type lang: Optional[str]
        :raises TypeError: If 'text' is not a string or if 'lang' is provided and is not a string or None.
        :raises ValueError: If 'text' is None.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'text' to be of type str, but got {type(text).__name__}.")
        if lang is not None and not isinstance(lang, str):
            raise TypeError(f"Expected 'lang' to be of type str, but got {type(lang).__name__}.")

        # Text field cannot be None
        if text is None:
            raise ValueError(f"{self.__class__.__name__}'s 'text' field cannot be None.")

    def _validate_ensure_text(self, text: Optional[str]) -> None:
        """Validate the 'text' argument based on the ENSURE_TEXT control flag.

        Checks if the 'text' field is empty and raises a ValueError or logs a warning depending on the ENSURE_TEXT
        flag set in the control class.

        :param text: The text to be validated.
        :type text: Optional[str]
        :raises ValueError: If ENSURE_TEXT is enabled and 'text' is an empty string.
        """
        control, flags = self._get_control_and_flags_type()

        # ignore added to bypass mypy's false positive on enums
        if text == "" and control.get_flag(flags.ENSURE_TEXT):  # type: ignore
            raise ValueError(
                f"ENSURE_TEXT enabled: {self.__class__.__name__}'s 'text' field cannot receive empty string."
            )

    def _validate_ensure_any_lang(self, lang: Optional[str]) -> None:
        """Validate the 'lang' argument based on the ENSURE_ANY_LANG and ENSURE_VALID_LANG control flags.

        Checks if the 'lang' field is empty and raises a ValueError or logs a warning depending on the ENSURE_ANY_LANG,
        ENSURE_VALID_LANG flag set in the control class.

        :param lang: The language code to be validated.
        :type lang: Optional[str]
        :raises ValueError: If ENSURE_ANY_LANG or ENSURE_VALID_LANG is enabled and 'lang' is an empty string.
        """
        control, flags = self._get_control_and_flags_type()

        if not lang:
            # ignore added to bypass mypy's false positive on enums
            if control.get_flag(flags.ENSURE_ANY_LANG):  # type: ignore
                raise ValueError(
                    f"ENSURE_ANY_LANG enabled: {self.__class__.__name__}'s 'lang' field cannot receive empty string."
                )
            # ignore added to bypass mypy's false positive on enums
            if control.get_flag(flags.ENSURE_VALID_LANG):  # type: ignore
                raise ValueError(
                    f"ENSURE_VALID_LANG enabled: {self.__class__.__name__}'s 'lang' field cannot receive empty string."
                )

    def _validate_ensure_valid_lang(self, lang: Optional[str]) -> None:
        """Validate the language tag for its validity.

        This method checks if the language tag is valid. If the tag is invalid, it raises a warning or an error
        depending on the control flags set in the control class.

        :param lang: The language code to be validated.
        :type lang: Optional[str]
        :raises ValueError: If ENSURE_VALID_LANG is enabled and the language tag is invalid.
        """
        control, flags = self._get_control_and_flags_type()

        if lang and not tag_is_valid(lang):
            # ignore added to bypass mypy's false positive on enums
            if control.get_flag(flags.ENSURE_VALID_LANG):  # type: ignore
                raise ValueError(
                    f"ENSURE_VALID_LANG enabled: {self.__class__.__name__}'s 'lang' field cannot be invalid."
                )
