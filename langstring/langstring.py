"""The langstring module provides the LangString class to encapsulate a string with its language information.

This module utilizes the langcodes library for validating language tags and the loguru library for logging
warnings in case of invalid language tags.
"""
import warnings

from langcodes import tag_is_valid
from loguru import logger

# Suppress the display of UserWarnings
warnings.simplefilter("ignore", UserWarning)


class LangString:
    """A class to encapsulate a string with its language information.

    :ivar text: The actual text string.
    :vartype text: str
    :ivar lang: The language of the text, as a Language object or None if not specified.
    :vartype lang: Language
    """

    def __init__(self, text: str, lang: str = None) -> None:
        """Initialize a new LangString object.

        :param text: The actual text string.
        :type text: str
        :param lang: The language of the text, defaults to None.
        :type lang: Language, optional
        """
        if text is not None and not isinstance(text, str):
            raise TypeError(f"Expected 'text' to be of type str, but got {type(text).__name__}.")
        if lang is not None and not isinstance(lang, str):
            raise TypeError(f"Expected 'lang' to be of type str, but got {type(lang).__name__}.")

        if not text:
            warning_msg = "Received empty string."
            warnings.warn(warning_msg, UserWarning)
            logger.warning(warning_msg)
        if lang and not tag_is_valid(lang):
            warning_msg = f"Invalid language tag '{lang}' used."
            warnings.warn(warning_msg, UserWarning)
            logger.warning(warning_msg)

        self.text: str = text
        self.lang: str = lang

    def to_string(self) -> str:
        """Convert the LangString object to a string. Syntactical sugar for calling self.__str__().

        :return: The string representation of the LangString object.
        :rtype: str
        """
        return self.__str__()

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        :return: The string representation of the LangString object.
        :rtype: str
        """
        if self.lang is None:
            return f'"{self.text}"'
        else:
            return f'"{self.text}"@{self.lang}'

    def __eq__(self, other: 'LangString') -> bool:
        """
        Check equality of this LangString with another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if both LangString objects are equal, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, LangString):
            return NotImplemented
        return self.text == other.text and self.lang == other.lang

    def __ne__(self, other: 'LangString') -> bool:
        """
        Check inequality of this LangString with another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if both LangString objects are not equal, False otherwise.
        :rtype: bool
        """
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """
        Generate a hash value for a LangString object.

        :return: The hash value of the LangString object.
        :rtype: int
        """
        return hash((self.text, self.lang))

    def __lt__(self, other: 'LangString') -> bool:
        """
        Check if this LangString is less than another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if this LangString is less than the other, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, LangString):
            return NotImplemented
        return (self.text, self.lang) < (other.text, other.lang)

    def __le__(self, other: 'LangString') -> bool:
        """
        Check if this LangString is less than or equal to another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if this LangString is less than or equal to the other, False otherwise.
        :rtype: bool
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: 'LangString') -> bool:
        """
        Check if this LangString is greater than another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if this LangString is greater than the other, False otherwise.
        :rtype: bool
        """
        return not self.__le__(other)

    def __ge__(self, other: 'LangString') -> bool:
        """
        Check if this LangString is greater than or equal to another LangString.

        :param other: Another LangString object to compare with.
        :type other: LangString
        :return: True if this LangString is greater than or equal to the other, False otherwise.
        :rtype: bool
        """
        return not self.__lt__(other)
