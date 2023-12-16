"""
The langstring module provides the LangString class to encapsulate a string with its language information.

This module is designed to work with text strings and their associated language tags, offering functionalities
such as validation of language tags, handling of empty strings and language tags based on control flags, and
logging of warnings for invalid language tags. It utilizes the langcodes library for validating language tags and
the loguru library for logging warnings in case of invalid language tags.

Control flags from the langstring_control module are used to enforce certain behaviors like ensuring non-empty
text and valid language tags. These flags can be set externally to alter the behavior of the LangString class.

:Example:

    # Create a LangString object
    lang_str = LangString("Hello, World!", "en")

    # Print the string representation
    print(lang_str.to_string())  # Output: '"Hello, World!"@en'
"""
import warnings
from typing import Optional

from langcodes import tag_is_valid
from loguru import logger

from .langstring_control import LangStringControl
from .langstring_control import LangStringFlag


class LangString:
    """A class to encapsulate a string with its language information.

    This class provides functionality to associate a text string with a language tag, offering methods for string
    representation, equality comparison, and hashing. The behavior of this class is influenced by control flags
    from the LangStringControl class, which can enforce non-empty text, valid language tags, and other constraints.

    :ivar text: The actual text string.
    :vartype text: str
    :ivar lang: The language of the text, represented by a language tag or None if not specified.
    :vartype lang: str or None
    """

    def __init__(self, text: Optional[str] = "", lang: Optional[str] = None) -> None:
        """Initialize a new LangString object with text and an optional language tag.

        The behavior of this method is influenced by control flags set in LangStringControl. For instance, if the
        ENSURE_TEXT flag is enabled, an empty 'text' string will raise a ValueError.

        :param text: The actual text string. Defaults to the empty string ("").
        :type text: str, optional
        :param lang: The language tag of the text, defaults to None.
        :type lang: str, optional
        :raises TypeError: If 'text' is not a string, or if 'lang' is provided and is not a string.
        :raises ValueError: If 'text' is empty and ENSURE_TEXT is enabled; if 'lang' is empty and ENSURE_ANY_LANG is \
        enabled; or if 'lang' is invalid and ENSURE_VALID_LANG is enabled.
        """

        self.text: Optional[str] = text
        self.lang: Optional[str] = lang

        self._validate_arguments_types()
        self._validate_ensure_text()
        self._validate_ensure_any_lang()
        self._validate_ensure_valid_lang()

    def to_string(self) -> str:
        """Convert the LangString object to a string representation.

        This method is a convenience wrapper for the __str__ method.

        :return: The string representation of the LangString object, including language tag if present.
        :rtype: str
        """
        return self.__str__()

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        :return: The string representation of the LangString object. Format: '"text"@lang' or '"text"' if lang is None.
        :rtype: str
        """
        if self.lang is None:
            return f'"{self.text}"'
        return f'"{self.text}"@{self.lang}'

    def __eq__(self, other: "LangString") -> bool:
        """Check equality of this LangString with another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if both LangString objects have the same text and language tag, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, LangString):
            return False
        return self.text == other.text and self.lang == other.lang

    def __hash__(self) -> int:
        """Generate a hash value for a LangString object.

        :return: The hash value of the LangString object, based on its text and language tag.
        :rtype: int
        """
        return hash((self.text, self.lang))

    def _validate_arguments_types(self) -> None:
        """Validate the types of the 'text' and 'lang' arguments.

        Ensures that 'text' is a string and 'lang' is either a string or None. Raises a TypeError if the types do not
        match the expected types.

        :raises TypeError: If 'text' is not a string or if 'lang' is provided and is not a string or None.
        """
        if not isinstance(self.text, str):
            raise TypeError(f"Expected 'text' to be of type str, but got {type(self.text).__name__}.")
        if self.lang is not None and not isinstance(self.lang, str):
            raise TypeError(f"Expected 'lang' to be of type str, but got {type(self.lang).__name__}.")

        # Text field cannot be empty
        if self.text is None:
            raise ValueError("Langstring's 'text' field cannot be None.")

    def _validate_ensure_text(self) -> None:
        """Validate the 'text' argument based on the ENSURE_TEXT control flag.

        Checks if the 'text' field is empty and raises a ValueError or warning depending on the ENSURE_TEXT and
        VERBOSE_MODE flags set in LangStringControl.

        :raises ValueError: If ENSURE_TEXT is enabled and 'text' is an empty string.
        """
        if self.text == "":
            if LangStringControl.get_flag(LangStringFlag.VERBOSE_MODE):
                warning_msg = "Langstring's 'text' field received empty string."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT):
                raise ValueError("ENSURE_TEXT enabled: Langstring's 'text' field cannot receive empty string.")

    def _validate_ensure_any_lang(self) -> None:
        """Validate the 'lang' argument based on the ENSURE_ANY_LANG and ENSURE_VALID_LANG control flags.

        Checks if the 'lang' field is empty and raises a ValueError or warning depending on the ENSURE_ANY_LANG,
        ENSURE_VALID_LANG, and VERBOSE_MODE flags set in LangStringControl.

        :raises ValueError: If ENSURE_ANY_LANG or ENSURE_VALID_LANG is enabled and 'lang' is an empty string.
        """
        if self.lang == "":
            if LangStringControl.get_flag(LangStringFlag.VERBOSE_MODE):
                warning_msg = "Langstring's 'lang' field received empty string."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if LangStringControl.get_flag(LangStringFlag.ENSURE_ANY_LANG):
                raise ValueError("ENSURE_ANY_LANG enabled: Langstring's 'lang' field cannot receive empty string.")
            if LangStringControl.get_flag(LangStringFlag.ENSURE_VALID_LANG):
                raise ValueError("ENSURE_VALID_LANG enabled: Langstring's 'lang' field cannot receive empty string.")

    def _validate_ensure_valid_lang(self) -> None:
        """Validate the language tag for its validity.

        This method checks if the language tag is valid. If the tag is invalid, it raises a warning or an error
        depending on the control flags set in LangStringControl.

        :raises ValueError: If ENSURE_VALID_LANG is enabled and the language tag is invalid.
        """
        if self.lang and not tag_is_valid(self.lang):
            if LangStringControl.get_flag(LangStringFlag.VERBOSE_MODE):
                warning_msg = f"Invalid language tag '{self.lang}' used."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if LangStringControl.get_flag(LangStringFlag.ENSURE_VALID_LANG):
                raise ValueError("ENSURE_VALID_LANG enabled: Langstring's 'lang' field cannot be invalid.")
