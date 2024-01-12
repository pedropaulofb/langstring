"""The langstring module provides the LangString class to encapsulate a string with its language information.

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
from .flags import LangStringFlag
from .utils.validator import Validator


class LangString:
    """A class to encapsulate a string with its language information.

    This class provides functionality to associate a text string with a language tag, offering methods for string
    representation, equality comparison, and hashing. The behavior of this class is influenced by control flags
    from the Controller class, which can enforce non-empty text, valid language tags, and other constraints.

    :ivar text: The text string.
    :vartype text: Optional[str]
    :ivar lang: The language tag of the text.
    :vartype lang: str
    """

    def __init__(self, text: str = "", lang: str = "") -> None:
        """Initialize a new LangString object with text and an optional language tag.

        The behavior of this method is influenced by control flags set in Controller. For instance, if the
        DEFINED_TEXT flag is enabled, an empty 'text' string will raise a ValueError.

        :param text: The text string.
        :type text: Optional[str]
        :param lang: The language tag of the text.
        :type lang: str
        """

        self.text: str = text
        self.lang: str = lang

    @property
    def text(self) -> str:
        """Getter for text."""
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        """Setter for text."""
        self._text = Validator.validate_text(LangStringFlag, new_text)

    @property
    def lang(self) -> str:
        """Getter for lang."""
        return self._lang

    @lang.setter
    def lang(self, new_lang: str) -> None:
        """Setter for lang."""
        self._lang = Validator.validate_lang(LangStringFlag, new_lang)

    def to_string(self) -> str:
        """Convert the LangString object to a string representation.

        This method is a convenience wrapper for the __str__ method.

        :return: The string representation of the LangString object, including the language tag.
        :rtype: str
        """
        return self.__str__()

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        :return: The string representation of the LangString object. Format: '"text"@lang'.
        :rtype: str
        """
        return f'"{self.text}"@{self.lang}'

    def __eq__(self, other: object) -> bool:
        """Check equality of this LangString with another object.

        :param other: Another object to compare with.
        :type other: object
        :return: True if 'other' is a LangString object with the same text and language tag, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, LangString):
            return NotImplemented
        return self.text == other.text and self.lang == other.lang

    def __hash__(self) -> int:
        """Generate a hash new_text for a LangString object.

        :return: The hash new_text of the LangString object, based on its text and language tag.
        :rtype: int
        """
        return hash((self.text, self.lang))
