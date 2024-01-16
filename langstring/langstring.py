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

    # GETTERS AND SETTERS

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

    # OVERWRITING BUILT-IN STRING METHODS

    def capitalize(self) -> "LangString":
        return LangString(self.text.capitalize(), self.lang)

    def casefold(self) -> "LangString":
        return LangString(self.text.casefold(), self.lang)

    def center(self, width: int, fillchar: str = " ") -> "LangString":
        return LangString(self.text.center(width, fillchar), self.lang)

    def count(self, sub: str, start: int = 0, end: int = None) -> int:
        return self.text.count(sub, start, end)

    def encode(self, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        return self.text.encode(encoding, errors)

    def endswith(self, suffix, start: int = 0, end: int = None) -> bool:
        return self.text.endswith(suffix, start, end)

    def expandtabs(self, tabsize: int = 8) -> "LangString":
        return LangString(self.text.expandtabs(tabsize), self.lang)

    def find(self, sub: str, start: int = 0, end: int = None) -> int:
        return self.text.find(sub, start, end)

    def format(self, *args, **kwargs) -> "LangString":
        return LangString(self.text.format(*args, **kwargs), self.lang)

    def format_map(self, mapping) -> "LangString":
        return LangString(self.text.format_map(mapping), self.lang)

    def index(self, sub: str, start: int = 0, end: int = None) -> int:
        return self.text.index(sub, start, end)

    def isalnum(self) -> bool:
        return (self.text).isalnum()

    def isalpha(self) -> bool:
        return (self.text).isalpha()

    def isascii(self) -> bool:
        return (self.text).isascii()

    def isdecimal(self) -> bool:
        return (self.text).isdecimal()

    def isdigit(self) -> bool:
        return (self.text).isdigit()

    def isidentifier(self) -> bool:
        return (self.text).isidentifier()

    def islower(self) -> bool:
        return (self.text).islower()

    def isnumeric(self) -> bool:
        return (self.text).isnumeric()

    def isprintable(self) -> bool:
        return (self.text).isprintable()

    def isspace(self) -> bool:
        return (self.text).isspace()

    def istitle(self) -> bool:
        return (self.text).istitle()

    def isupper(self) -> bool:
        return (self.text).isupper()

    def join(self, iterable) -> "LangString":
        """Join an iterable with the text of the LangString."""
        joined_text = self.text.join(iterable)
        return LangString(joined_text, self.lang)

    def ljust(self, width: int, fillchar: str = " ") -> "LangString":
        """Left justify the text."""
        justified_text = self.text.ljust(width, fillchar)
        return LangString(justified_text, self.lang)

    def lower(self) -> "LangString":
        return LangString(self.text.lower(), self.lang)

    def lstrip(self, chars: str = None) -> "LangString":
        return LangString(self.text.lstrip(chars), self.lang)

    @staticmethod
    def maketrans(intab, outtab):
        """Create a translation table."""
        return str.maketrans(intab, outtab)

    def partition(self, sep: str) -> tuple:
        """Partition the text."""
        parts = self.text.partition(sep)
        return tuple(LangString(part, self.lang) for part in parts)

    def replace(self, old: str, new: str, count: int = -1) -> "LangString":
        return LangString(self.text.replace(old, new, count), self.lang)

    def rfind(self, sub: str, start: int = 0, end: int = None) -> int:
        return self.text.rfind(sub, start, end)

    def rindex(self, sub: str, start: int = 0, end: int = None) -> int:
        return self.text.rindex(sub, start, end)

    def rjust(self, width: int, fillchar: str = " ") -> "LangString":
        """Right justify the text."""
        justified_text = self.text.rjust(width, fillchar)
        return LangString(justified_text, self.lang)

    def rpartition(self, sep: str) -> tuple:
        """Partition the text from the right."""
        parts = self.text.rpartition(sep)
        return tuple(LangString(part, self.lang) for part in parts)

    def rsplit(self, sep: str = None, maxsplit: int = -1) -> list:
        """Split the text from the right."""
        split_texts = self.text.rsplit(sep, maxsplit)
        return [LangString(part, self.lang) for part in split_texts]

    def rstrip(self, chars: str = None) -> "LangString":
        return LangString(self.text.rstrip(chars), self.lang)

    def split(self, sep: str = None, maxsplit: int = -1) -> list:
        """Split the text."""
        split_texts = self.text.split(sep, maxsplit)
        return [LangString(part, self.lang) for part in split_texts]

    def splitlines(self, keepends: bool = False) -> list:
        """Split the text into lines."""
        lines = self.text.splitlines(keepends)
        return [LangString(line, self.lang) for line in lines]

    def startswith(self, prefix, start: int = 0, end: int = None) -> bool:
        return self.text.startswith(prefix, start, end)

    def strip(self, chars: str = None) -> "LangString":
        return LangString(self.text.strip(chars), self.lang)

    def swapcase(self) -> "LangString":
        return LangString(self.text.swapcase(), self.lang)

    def title(self) -> "LangString":
        return LangString(self.text.title(), self.lang)

    def translate(self, table):
        """Translate the text using a translation table."""
        return LangString(self.text.translate(table), self.lang)

    def upper(self) -> "LangString":
        return LangString(self.text.upper(), self.lang)

    def zfill(self, width: int) -> "LangString":
        return LangString(self.text.zfill(width), self.lang)

    # OVERWRITING BUILT-IN STRING DUNDER METHODS

    def __add__(self, other):
        """Add another LangString or a string to this LangString.

        The operation can only be performed if:
        - Both are LangString objects with the same language tag.
        - The other is a string, which will be concatenated to the text of this LangString.

        :param other: The LangString or string to add.
        :return: A new LangString with the concatenated text.
        :raises TypeError: If the objects are not compatible for addition.
        """
        if isinstance(other, LangString):
            if (self.lang).lower() != (other.lang).lower():
                raise ValueError("Cannot add LangString objects with different language tags.")
            return LangString(self.text + other.text, self.lang)
        elif isinstance(other, str):
            return LangString(self.text + other, self.lang)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'LangString' and '{type(other).__name__}'")

    def __contains__(self, item: str) -> bool:
        """Check if a substring exists within the LangString's text."""
        return item in self.text

    def __delitem__(self, key):
        """Delete a slice or a character from the text."""
        self.text = self.text[:key] + self.text[key + 1 :]

    def __eq__(self, other: object) -> bool:
        """Check equality of this LangString with another object.

        :param other: Another object to compare with.
        :type other: object
        :return: True if 'other' is a LangString object with the same text and language tag, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, LangString):
            return NotImplemented
        return self.text == other.text and self.lang.lower() == other.lang.lower()

    def __ge__(self, other: object) -> bool:
        """Check if this LangString is greater than or equal to another LangString object."""
        if not isinstance(other, LangString) or self.lang.lower() != other.lang.lower():
            return NotImplemented
        return self.text >= other.text

    def __getitem__(self, key: slice) -> "LangString":
        """Retrieve a substring from the LangString's text."""
        return LangString(self.text[key], self.lang)

    def __gt__(self, other: object) -> bool:
        """Check if this LangString is greater than another LangString object."""
        if not isinstance(other, LangString) or (self.lang).lower() != (other.lang).lower():
            return NotImplemented
        return self.text > other.text

    def __hash__(self) -> int:
        """Generate a hash new_text for a LangString object.

        :return: The hash new_text of the LangString object, based on its text and language tag.
        :rtype: int
        """
        return hash((self.text, self.lang.lower()))

    def __iadd__(self, other):
        """Implement in-place addition."""
        if isinstance(other, LangString):
            if self.lang.lower() != other.lang.lower():
                raise ValueError("Cannot add LangString objects with different language tags.")
            self.text += other.text
        elif isinstance(other, str):
            self.text += other
        else:
            raise TypeError(f"Unsupported operand type(s) for +=: 'LangString' and '{type(other).__name__}'")
        return self

    def __imul__(self, other):
        """Implement in-place multiplication."""
        if isinstance(other, int):
            self.text *= other
        else:
            raise TypeError("Unsupported operand type(s) for *=: 'LangString' and '{}'".format(type(other).__name__))
        return self

    def __iter__(self):
        """Enable iteration over the text part of the LangString."""
        return iter(self.text)

    def __le__(self, other: object) -> bool:
        """Check if this LangString is less than or equal to another LangString object."""
        if not isinstance(other, LangString) or self.lang.lower() != other.lang.lower():
            return NotImplemented
        return self.text <= other.text

    def __len__(self) -> int:
        """Return the length of the LangString's text."""
        return len(self.text)

    def __lt__(self, other: object) -> bool:
        """Check if this LangString is less than another LangString object."""
        if not isinstance(other, LangString) or self.lang.lower() != other.lang.lower():
            return NotImplemented
        return self.text < other.text

    def __mul__(self, other: int) -> "LangString":
        """Repeat the LangString's text a specified number of times."""
        if not isinstance(other, int):
            raise TypeError("Can only multiply LangString by an integer")
        return LangString(self.text * other, self.lang)

    def __ne__(self, other: object) -> bool:
        """Check inequality of this LangString with another object."""
        if not isinstance(other, LangString):
            return NotImplemented
        return not (self.text == other.text and self.lang == other.lang)

    def __radd__(self, other):
        """Handle concatenation when LangString is on the right side of the '+' operator.

        This method allows a string to be added to the beginning of the LangString's text.

        :param other: The string to be concatenated to the beginning of this LangString's text.
        :type other: str
        :return: A new LangString with the concatenated text.
        :rtype: LangString
        :raises TypeError: If 'other' is not a string.
        """
        if not isinstance(other, str):
            raise TypeError(f"Unsupported operand type(s) for +: '{type(other).__name__}' and 'LangString'")
        return LangString(other + self.text, self.lang)


    def __reversed__(self):
        """Reverse the text."""
        return LangString(self.text[::-1], self.lang)

    def __setitem__(self, key, value):
        """Set a slice or a character in the text."""
        if not isinstance(value, str):
            raise TypeError("Assignment value must be a string")
        self.text = self.text[:key] + value + self.text[key + 1 :]

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        :return: The string representation of the LangString object.
        :rtype: str
        """
        text_representation = f'"{self.text}"' if LangStringFlag.PRINT_WITH_QUOTES else self.text

        if LangStringFlag.PRINT_WITH_LANG:
            return f"{text_representation}@{self.lang}"
        return text_representation
