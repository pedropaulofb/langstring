"""This module defines the `MultiLangString` class for handling multilingual text strings."""
from enum import Enum

from langcodes import Language, tag_is_valid
from loguru import logger

from langstring.langstring import LangString


class ControlMultipleEntries(Enum):
    """ControlMultipleEntries Enum for specifying handling of duplicate language tags.

    Enum Members:
        OVERWRITE: Overwrite existing entries with the same language tag.
        ALLOW: Allow multiple entries with the same language tag.
        BLOCK_WARN: Block and log a warning for duplicate language tags.
        BLOCK_ERROR: Block and raise an error for duplicate language tags.
    """
    OVERWRITE = "OVERWRITE"
    ALLOW = "ALLOW"
    BLOCK_WARN = "BLOCK_WARN"
    BLOCK_ERROR = "BLOCK_ERROR"


class MultiLangString:
    """MultiLangString class for handling multilingual text strings.

    This class allows the management of multilingual text strings with different language tags.

    :ivar control: The control strategy for handling duplicate language tags.
    :vartype control: ControlMultipleEntries
    :ivar langstrings: A dictionary of LangStrings indexed by language tag.
    :vartype langstrings: dict
    :ivar preferred_lang: The preferred language for this MultiLangString.
    :vartype preferred_lang: Language
    """

    def __init__(self, *args: LangString, control: str = "ALLOW", preferred_lang: Language = "en"):
        """Initialize a new MultiLangString object.

        :param control: The control strategy for handling duplicate language tags, defaults to "ALLOW".
        :type control: str, optional
        :param preferred_lang: The preferred language for this MultiLangString, defaults to "en".
        :type preferred_lang: Language, optional
        :param args: LangString objects to initialize the MultiLangString with.
        :type args: LangString
        """
        try:
            self.control = ControlMultipleEntries[control]
        except KeyError:
            raise ValueError(f"Invalid control value: {control}. "
                             f"Valid control values are: {ControlMultipleEntries._member_names_}.")

        if not tag_is_valid(preferred_lang):
            logger.warning(f"Invalid preferred language tag '{preferred_lang}' used.")

        self.langstrings: dict = {}  # Initialize self.langStrings here
        self.control: ControlMultipleEntries = ControlMultipleEntries[control]
        self.preferred_lang: Language = preferred_lang

        for arg in args:
            self.add(arg)

    def add(self, lang_string: LangString):
        """Add a LangString to the MultiLangString.

        :param lang_string: The LangString to add.
        :type lang_string: LangString
        """
        if isinstance(lang_string, LangString):
            if self.control == ControlMultipleEntries.BLOCK_WARN and lang_string.lang in self.langstrings:
                logger.warning(
                    f"Operation not possible, a LangString with language tag {lang_string.lang} already exists.")
            elif self.control == ControlMultipleEntries.BLOCK_ERROR and lang_string.lang in self.langstrings:
                raise ValueError(
                    f"Operation not possible, a LangString with language tag {lang_string.lang} already exists.")
            elif self.control == ControlMultipleEntries.OVERWRITE:
                self.langstrings[lang_string.lang] = [lang_string.text]
            else:  # self.control == ALLOW
                if lang_string.text not in self.langstrings.get(lang_string.lang, []):
                    self.langstrings.setdefault(lang_string.lang, []).append(lang_string.text)

    def get_lang_string(self, lang: str) -> list:
        """Get LangStrings for a specific language tag.

        :param lang: The language tag to retrieve LangStrings for.
        :type lang: str
        :return: List of LangStrings for the specified language tag.
        :rtype: list
        """
        return self.langstrings.get(lang, [])

    def get_preferred_lang_string(self) -> str:
        """Get the preferred language's LangString.

        :return: The LangString for the preferred language.
        :rtype: str
        """
        return self.langstrings.get(self.preferred_lang, None)

    def remove_lang_string(self, lang_string: LangString) -> bool:
        """Remove a LangString from the MultiLangString.

        :param lang_string: The LangString to remove.
        :type lang_string: LangString
        :return: True if the LangString was removed, False otherwise.
        :rtype: bool
        """
        lang_strings = self.langstrings.get(lang_string.lang, [])
        if lang_string.text in lang_strings:
            lang_strings.remove(lang_string.text)
            if not lang_strings:
                del self.langstrings[lang_string.lang]
            return True
        return False

    def remove_lang(self, lang: str):
        """Remove all LangStrings for a specific language tag.

        :param lang: The language tag for which to remove LangStrings.
        :type lang: str
        """
        self.langstrings.pop(lang, None)

    def to_string(self) -> str:
        """Convert the MultiLangString to a string.

        :return: The string representation of the MultiLangString.
        :rtype: str
        """
        return self.__str__()

    def to_string_list(self) -> list[str]:
        """Convert the MultiLangString to a list of strings.

        :return: List of strings representing the MultiLangString.
        :rtype: list
        """
        return [f"{repr(lang_string)}@{lang}" for lang, lang_strings in self.langstrings.items() for lang_string in
            lang_strings]

    def __repr__(self):
        """Return a string representation of the MultiLangString object.

        :return: A string representation of the MultiLangString.
        :rtype: str
        """
        return f"MultiLangString({self.langstrings}, control={self.control}, preferred_lang={self.preferred_lang})"

    def __len__(self):
        """Return the total number of LangStrings stored in the MultiLangString.

        :return: The total number of LangStrings.
        :rtype: int
        """
        return sum(len(lang_strings) for lang_strings in self.langstrings.values())

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        return ", ".join(
            f"{repr(lang_string)}@{lang}" for lang, lang_strings in self.langstrings.items() for lang_string in
            lang_strings)
