"""This module defines the `MultiLangString` class for handling multilingual text strings."""
import warnings
from enum import Enum

from langcodes import Language, tag_is_valid
from loguru import logger

from langstring.langstring import LangString

# Suppress the display of UserWarnings
warnings.simplefilter("ignore", UserWarning)


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
            raise ValueError(
                f"Invalid control value: {control}. "
                f"Valid control values are: {ControlMultipleEntries._member_names_}."
            )

        if preferred_lang is None:
            warn_message = "Preferred language set to default value: 'en'."
            warnings.warn(warn_message, UserWarning)
            logger.warning(warn_message)
            self.preferred_lang = "en"
        elif not isinstance(preferred_lang, str):
            raise TypeError(
                f"preferred_lang should be of type string or None. Received '{type(preferred_lang).__name__}' "
                f"with value '{preferred_lang}'."
            )
        else:
            if not tag_is_valid(preferred_lang):
                warn_message = f"Invalid preferred language tag '{preferred_lang}' used."
                warnings.warn(warn_message, UserWarning)
                logger.warning(warn_message)

            self.preferred_lang: Language = preferred_lang

        self.langstrings: dict = {}  # Initialize self.langStrings here
        self.control: ControlMultipleEntries = ControlMultipleEntries[control]

        for arg in args:
            if not isinstance(arg, LangString):
                logger.error(
                    f"MultiLangString initialized with invalid argument. Expected a LangString but "
                    f"received '{type(arg).__name__}' with value '{arg}'."
                )
                raise TypeError
            else:
                self.add(arg)

    def add(self, langstring: LangString):
        """Add a LangString to the MultiLangString.

        :param langstring: The LangString to add.
        :type langstring: LangString
        """
        if isinstance(langstring, LangString):
            if self.control == ControlMultipleEntries.BLOCK_WARN and langstring.lang in self.langstrings:
                warn_message = (
                    f"Operation not possible, a LangString with language tag {langstring.lang} already exists."
                )
                warnings.warn(warn_message, UserWarning)
                logger.warning(warn_message)
            elif self.control == ControlMultipleEntries.BLOCK_ERROR and langstring.lang in self.langstrings:
                raise ValueError(
                    f"Operation not possible, a LangString with language tag {langstring.lang} already exists."
                )
            elif self.control == ControlMultipleEntries.OVERWRITE:
                self.langstrings[langstring.lang] = [langstring.text]
            else:  # self.control == ALLOW
                if langstring.text not in self.langstrings.get(langstring.lang, []):
                    self.langstrings.setdefault(langstring.lang, []).append(langstring.text)
        else:
            logger.error(
                f"MultiLangString initialized with invalid argument. Expected a LangString but "
                f"received '{type(langstring).__name__}' with value '{langstring}'."
            )
            raise TypeError

    def get_langstring(self, lang: str) -> list:
        """Get LangStrings for a specific language tag.

        :param lang: The language tag to retrieve LangStrings for.
        :type lang: str
        :return: List of LangStrings for the specified language tag.
        :rtype: list
        """
        if not isinstance(lang, str):
            raise TypeError(f"Expected a string but received '{type(lang).__name__}'.")
        return self.langstrings.get(lang, [])

    def get_pref_langstring(self) -> str:
        """Get the preferred language's LangString.

        :return: The LangString for the preferred language.
        :rtype: str
        """
        return self.langstrings.get(self.preferred_lang, None)

    def remove_langstring(self, langstring: LangString) -> bool:
        """Remove a LangString from the MultiLangString.

        :param langstring: The LangString to remove.
        :type langstring: LangString
        :return: True if the LangString was removed, False otherwise.
        :rtype: bool
        """
        langstrings = self.langstrings.get(langstring.lang, [])
        if langstring.text in langstrings:
            langstrings.remove(langstring.text)
            if not langstrings:
                del self.langstrings[langstring.lang]
            return True
        return False

    def remove_language(self, lang: str):
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
        return [
            f"{repr(langstring)}@{lang}" for lang, langstrings in self.langstrings.items() for langstring in langstrings
        ]

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
        return sum(len(langstrings) for langstrings in self.langstrings.values())

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        return ", ".join(
            f"{repr(langstring)}@{lang}" for lang, langstrings in self.langstrings.items() for langstring in langstrings
        )
