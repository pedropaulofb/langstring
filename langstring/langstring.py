"""
The langstring module provides the LangString class to encapsulate a string with its language information.

This module is designed to work with text strings and their associated language tags, offering functionalities
such as validation of language tags, handling of empty strings and language tags based on control flags, and
logging of warnings for invalid language tags. It utilizes the langcodes library for validating language tags and
the loguru library for logging warnings in case of invalid language tags.

Control flags from the langstring_control module are used to enforce certain behaviors like ensuring non-empty
text and valid language tags. These flags can be set externally to alter the behavior of the LangString class.

:Example:

    from langstring import LangString
    import langstring_control as ls_control

    # Set control flags
    ls_control.enable_verbose_mode(True)
    ls_control.ls_ensure_text(True)

    # Create a LangString object
    lang_str = LangString("Hello, World!", "en")

    # Print the string representation
    print(lang_str.to_string())  # Output: '"Hello, World!"@en'
"""
import warnings

from langcodes import tag_is_valid
from loguru import logger

import langstring_control as ls_control

# Suppress the display of UserWarnings
warnings.simplefilter("ignore", UserWarning)


class LangString:
    """A class to encapsulate a string with its language information.

    This class provides functionality to associate a text string with a language tag, offering methods for string
    representation, equality comparison, and hashing.

    :ivar text: The actual text string.
    :vartype text: str
    :ivar lang: The language of the text, represented by a language tag or None if not specified.
    :vartype lang: str or None
    """

    def __init__(self, text: str = "", lang: str = None) -> None:
        """
        Initialize a new LangString object with text and an optional language tag.

        :param text: The actual text string. Defaults to the empty string ("").
        :type text: str
        :param lang: The language tag of the text, defaults to None.
        :type lang: str, optional
        :raises TypeError: If 'text' is not a string, or if 'lang' is provided and is not a string.
        :raises ValueError: If 'text' is empty and _ENSURE_TEXT is enabled; if 'lang' is empty and _ENSURE_ANY_LANG is \
        enabled; or if 'lang' is invalid and _ENSURE_VALID_LANG is enabled.
        """
        # Type validation
        if not isinstance(text, str):
            raise TypeError(f"Expected 'text' to be of type str, but got {type(text).__name__}.")
        if lang is not None and not isinstance(lang, str):
            raise TypeError(f"Expected 'lang' to be of type str, but got {type(lang).__name__}.")

        # Text field cannot be empty
        if text is None:
            raise ValueError("Langstring's 'text' field cannot be None.")

        # Ensure text control option
        if text == "":
            if ls_control._VERBOSE_MODE:
                warning_msg = "Langstring's 'text' field received empty string."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if ls_control._ENSURE_TEXT:
                raise ValueError("ENSURE_TEXT enabled: Langstring's 'text' field cannot receive empty string.")

        # Ensure lang control option
        if lang == "":
            if ls_control._VERBOSE_MODE:
                warning_msg = "Langstring's 'lang' field received empty string."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if ls_control._ENSURE_ANY_LANG:
                raise ValueError("ENSURE_ANY_LANG enabled: Langstring's 'lang' field cannot receive empty string.")
            if ls_control._ENSURE_VALID_LANG:
                raise ValueError("ENSURE_VALID_LANG enabled: Langstring's 'lang' field cannot receive empty string.")

        # Validate lang control option
        if lang and not tag_is_valid(lang):
            if ls_control._VERBOSE_MODE:
                warning_msg = f"Invalid language tag '{lang}' used."
                warnings.warn(warning_msg, UserWarning)
                logger.warning(warning_msg)
            if ls_control._ENSURE_VALID_LANG:
                raise ValueError("ENSURE_VALID_LANG enabled: Langstring's 'lang' field cannot be invalid.")

        self.text: str = text
        self.lang: str = lang

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
        else:
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
