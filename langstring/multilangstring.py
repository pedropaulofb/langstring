"""The MultiLangString module provides a class for managing and manipulating multilingual text strings.

It allows for the storage, retrieval, and manipulation of text strings in multiple languages, offering a flexible and
efficient way to handle multilingual content in applications.

The MultiLangString class utilizes a dictionary to store text entries associated with language tags, enabling the
representation and handling of text in various languages. It supports adding new entries, removing entries, and
retrieving entries in specific languages or across all languages. The class also allows setting a preferred language,
which can be used as a default for operations that involve retrieving text entries.

Key Features:
- Store and manage text entries in multiple languages using language tags.
- Add and remove text entries for specific languages.
- Retrieve text entries for a specific language or all languages.
- Set and get a preferred language for default text retrieval.
- Support for equality comparison and hashing based on the content of the multilingual text entries.
- Validation and control strategies for handling duplicate language tags and ensuring the integrity of text entries.

This module is designed to be used in applications that require handling of text in multiple languages, providing a
convenient and standardized way to store and manipulate multilingual text data.

Usage:
The MultiLangString class can be used to create multilingual text containers, add text entries in various languages,
retrieve entries based on language, and perform other operations related to multilingual text management. It is
particularly useful in applications where content needs to be presented in multiple languages, such as websites,
applications with internationalization support, and data processing tools that handle multilingual data.

By providing a comprehensive set of methods for managing multilingual text, the MultiLangString class aims to simplify
the development of multilingual applications and facilitate the handling of text in multiple languages.
"""
from typing import Optional
from typing import Union

from .flags import MultiLangStringFlag
from .langstring import LangString
from .setlangstring import SetLangString
from .utils.validator import Validator


class MultiLangString:
    """A class for managing multilingual text strings with various language tags.

    Utilizes a global control strategy set in Controller to handle duplicate language tags. Supports
    operations like adding, removing, and retrieving language strings in multiple languages.

    :cvar mls_dict: A dictionary representing the internal structure of the MultiLangString.
    :vartype mls_dict: Optional[dict[str, set[str]]]
    :ivar pref_lang: The preferred language for this MultiLangString. Defaults to "en".
    :vartype pref_lang: str
    """

    def __init__(self, mls_dict: Optional[dict[str, set[str]]] = None, pref_lang: str = "en") -> None:
        """Initialize a MultiLangString object with an optional dictionary and preferred language.

        Validates the provided mls_dict against the current flag settings. If mls_dict is not provided, initializes
        with an empty dictionary. The preferred language is set, which is used as a default when retrieving entries
        or LangStrings.

        :param mls_dict: A dictionary representing the internal structure of the MultiLangString, where keys are
                         language codes (str) and values are sets of text entries (set[str]). If not provided, an
                         empty dictionary is used. Defaults to None.
        :type mls_dict: Optional[dict[str, set[str]]]
        :param pref_lang: The preferred language for this MultiLangString, used as a default when retrieving entries
                          or LangStrings. Defaults to "en".
        :type pref_lang: str
        :raises TypeError: If mls_dict is not a dictionary or pref_lang is not a string.
        """
        self.mls_dict: dict[str, set[str]] = mls_dict if (mls_dict is not None) else {}
        self.pref_lang: str = pref_lang

    # ---------------------------------------------
    # Getters and Setters
    # ---------------------------------------------

    @property
    def mls_dict(self) -> dict[str, set[str]]:
        """Getter for texts."""
        return self._mls_dict

    @mls_dict.setter
    def mls_dict(self, new_mls_dict: dict[str, set[str]]) -> None:
        """Setter for mls_dict that ensures keys are strings and values are sets of strings."""
        msg = f"Invalid type of 'mls_dict' received ('{new_mls_dict}')."
        if not isinstance(new_mls_dict, dict):
            raise TypeError(f"{msg}'). Expected 'dict', got '{type(new_mls_dict).__name__}'.")

        temp_dict: dict[str, set[str]] = {}
        for lang, texts in new_mls_dict.items():
            validated_key = Validator.validate_lang(MultiLangStringFlag, lang)
            temp_dict[validated_key] = set()
            for text in texts:
                validated_value = Validator.validate_text(MultiLangStringFlag, text)
                temp_dict[validated_key].add(validated_value)

        self._mls_dict = temp_dict

    @property
    def pref_lang(self) -> str:
        """Get the preferred language for this MultiLangString.

        :return: The preferred language as a string.
        """
        return self._pref_lang

    @pref_lang.setter
    def pref_lang(self, new_pref_lang: str) -> None:
        """Set the preferred language for this MultiLangString.

        :param new_pref_lang: The preferred language as a string.
        :type new_pref_lang: str
        """
        self._pref_lang = Validator.validate_text(MultiLangStringFlag, new_pref_lang)

    # ---------------------------------------------
    # MultiLangString's Regular Methods
    # ---------------------------------------------

    def add(self, input: Union[str, LangString, SetLangString]):
        # TODO: to be implemented.
        pass

    def add_entry(self, text: str, lang: str = "") -> None:
        """Add a text entry to the MultiLangString under a specified language.

        Validates the provided text and language against the current flag settings before adding. If the specified
        language does not exist in the mls_dict, a new set for that language is created. The text is then added to
        this set. If the language already exists, the text is added to the existing set for that language.

        :param text: The text to be added to the MultiLangString.
        :type text: str
        :param lang: The language under which the text should be added. If not specified, defaults to an empty string.
        :type lang: str
        """
        if lang not in self.mls_dict:
            self.mls_dict[lang] = set()
        self.mls_dict[lang].add(text)

    def add_langstring(self, langstring: LangString) -> None:
        """Add a LangString to the MultiLangString.

        :param langstring: The LangString object to be added, representing a text in a specific language.
        :type langstring: LangString
        """
        if not isinstance(langstring, LangString):
            raise TypeError(f"Invalid argument type. Expected type 'LangString', got '{type(langstring).__name__}'")

        langstring.lang = "" if langstring.lang is None else langstring.lang
        self.add_entry(text=langstring.text, lang=langstring.lang)

    def add_setlangstring(self, setlangstring: SetLangString) -> None:
        """Add a SetLangString to the MultiLangString.

        :param setlangstring: The SetLangString object to be added, representing a text in a specific language.
        :type setlangstring: SetLangString
        """
        if not isinstance(setlangstring, SetLangString):
            raise TypeError(
                f"Invalid argument type. Expected type 'SetLangString', got '{type(setlangstring).__name__}'"
            )

        # TODO: To be implemented.

    def remove_entry(self, text: str, lang: str, clear_empty: bool = False) -> None:
        """Remove a single entry from the set of a given language key in the dictionary.

        If the specified language key exists and the text is in its set, the text is removed. If this results in an
        empty set for the language, the language key is also removed from the dictionary.

        :param text: The text to be removed.
        :type text: str
        :param lang: The language key from which the text should be removed.
        :type lang: str
        """
        if lang in self.mls_dict and text in self.mls_dict[lang]:
            self.mls_dict[lang].remove(text)
            if len(self.mls_dict[lang]) == 0 and clear_empty:
                del self.mls_dict[lang]
        else:
            raise ValueError(f"Entry '{text}@{lang}' not found in the MultiLangString.")

    def remove_langstring(self, langstring: LangString) -> None:
        # TODO: To be implemented
        pass

    def remove_lang(self, lang: str) -> None:
        """Remove all entries of a given language from the dictionary.

        If the specified language key exists, it and all its associated texts are removed from the dictionary.

        :param lang: The language key to be removed along with all its texts.
        :type lang: str
        """
        if lang in self.mls_dict:
            del self.mls_dict[lang]
        else:
            raise ValueError(f"Lang '{lang}' not found in the MultiLangString.")

    # TODO: create discard (do not raise error). See implementation for SLSs.

    def clear_empty(self) -> None:
        empty_langs = [lang for lang, text in self.mls_dict.items() if not text]
        for lang in empty_langs:
            del self.mls_dict[lang]

    def get_strings_lang(self, lang: str) -> list[str]:
        """Retrieve all text entries for a specific language.

        :param lang: The language key to retrieve entries for.
        :type lang: str
        :return: A list of text entries for the specified language.
        :rtype: list[str]
        """
        return list(self.mls_dict.get(lang, []))

    def get_strings_pref_lang(self) -> list[str]:
        """Retrieve all text entries for the preferred language.

        :return: A list of text entries for the specified language.
        :rtype: list[str]
        """
        return self.get_strings_lang(self._pref_lang)

    def get_strings_all(self) -> list[str]:
        """Retrieve all text entries across all languages.

        :return: A list of all text entries.
        :rtype: list[str]
        """
        return [text for texts in self.mls_dict.values() for text in texts]

    def get_strings_langstring_lang(self, lang: str) -> list[str]:
        """Retrieve all text entries for a specific language, formatted as '"text"@lang'.

        :param lang: The language key to retrieve entries for.
        :type lang: str
        :return: A list of formatted text entries for the specified language.
        :rtype: list[str]
        """
        return [f'"{text}"@{lang}' for text in self.mls_dict.get(lang, [])]

    def get_strings_langstring_pref_lang(self) -> list[str]:
        """Retrieve all text entries for the preferred language, formatted as '"text"@lang'.

        :return: A list of formatted text entries for the specified language.
        :rtype: list[str]
        """
        return self.get_strings_langstring_lang(self._pref_lang)

    def get_strings_langstring_all(self) -> list[str]:
        """Retrieve all text entries across all languages, formatted as '"text"@lang'.

        :return: A list of formatted text entries for all languages.
        :rtype: list[str]
        """
        return [f'"{text}"@{lang}' for lang, texts in self.mls_dict.items() for text in texts]

    def len_entries_all(self) -> int:
        """Calculate the total number of elements across all sets in the dictionary.

        Iterates through each set in the dictionary values and sums their lengths to get the total number of elements.

        :return: The total number of elements across all sets.
        :rtype: int
        """
        return sum(len(elements) for elements in self.mls_dict.values())

    def len_entries_lang(self, lang: str) -> int:
        """Calculate the number of entries of a given language in the dictionary.

        :return: The number of entries for a given language in a MultiLangString.
        :rtype: int
        """
        if lang in self.mls_dict.keys():
            return len(self.mls_dict[lang])
        return 0

    def len_langs(self) -> int:
        """Calculate the number of keys (languages) in the dictionary.

        This method returns the count of distinct keys in the dictionary, which represents the number of languages.

        :return: The number of keys in the dictionary.
        :rtype: int
        """
        return len(self.mls_dict)

    def is_entry(self, text: str, lang: str) -> bool:
        return lang in self.mls_dict and text in self.mls_dict[lang]

    def to_langstrings(self) -> list[LangString]:
        # TODO: To be implemented
        pass

    def to_setlangstrings(self) -> list[SetLangString]:
        # TODO: To be implemented
        pass

    # ---------------------------------------------
    # MultiLangString's Dunder Methods
    # ---------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Check equality of this MultiLangString with another MultiLangString.

        Equality is determined based on the mls_dict attribute. The pref_lang attribute is not considered in the
        equality check.

        :param other: Another object to compare with.
        :type other: object
        :return: True if both MultiLangString objects have the same mls_dict, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, MultiLangString):
            return False
        return self.mls_dict == other.mls_dict

    def __hash__(self) -> int:
        """Generate a hash new_text for a MultiLangString object.

        The hash is computed based on the 'mls_dict' attribute of the MultiLangString. This approach ensures that
        MultiLangString objects with the same content will have the same hash new_text.

        :return: The hash new_text of the MultiLangString object.
        :rtype: int
        """
        # Convert dictionary to a hashable form (tuple of tuples) for consistent hashing
        hashable_mls_dict = tuple((lang, frozenset(texts)) for lang, texts in self.mls_dict.items())
        return hash(hashable_mls_dict)

    def __repr__(self) -> str:
        """Return a detailed string representation of the MultiLangString object.

        This method provides a more verbose string representation of the MultiLangString, which includes the full
        dictionary of language strings and the preferred language, making it useful for debugging.

        :return: A detailed string representation of the MultiLangString.
        :rtype: str
        """
        return f"MultiLangString({self.mls_dict}, pref_lang='{self.pref_lang}')"

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        This method provides a concise string representation of the MultiLangString, listing each text entry with its
        associated language tag.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        entries = []
        for lang, texts in self.mls_dict.items():
            for text in texts:
                if lang:  # If there is a language tag
                    entries.append(f'"{text}"@{lang}')
                else:  # If there is no language tag
                    entries.append(text)
        return ", ".join(entries)
