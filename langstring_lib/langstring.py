"""The langstring_lib module provides the LangString class to encapsulate a string with its language information.

This module utilizes the langcodes library for validating language tags and the loguru library for logging
warnings in case of invalid language tags.
"""

from langcodes import tag_is_valid, Language
from loguru import logger


class LangString:
    """A class to encapsulate a string with its language information.

    :ivar text: The actual text string.
    :vartype text: str
    :ivar lang: The language of the text, as a Language object or None if not specified.
    :vartype lang: Language
    """

    def __init__(self, text: str, lang: Language = None) -> None:
        """Initialize a new LangString object.

        :param text: The actual text string.
        :type text: str
        :param lang: The language of the text, defaults to None.
        :type lang: Language, optional
        """
        if text and not isinstance(text, str):
            raise TypeError
        if lang and not isinstance(lang, str):
            raise TypeError

        if not text:
            logger.warning("Received empty string.")
        if lang and not tag_is_valid(lang):
            logger.warning(f"Invalid language tag '{lang}' used.")

        self.text: str = text
        self.lang: Language = lang

    def to_string(self) -> str:
        """Convert the LangString object to a string.

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


