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

Classes:
- MultiLangString: The main class for creating and managing multilingual text strings.

Dependencies:
- LangString: A class for representing individual text entries with associated language tags.
- MultiLangStringControl and MultiLangStringFlag: for managing configuration and behavior of MultiLangString instances.
- ValidationBase: A base class providing validation functionalities.

Usage:
The MultiLangString class can be used to create multilingual text containers, add text entries in various languages,
retrieve entries based on language, and perform other operations related to multilingual text management. It is
particularly useful in applications where content needs to be presented in multiple languages, such as websites,
applications with internationalization support, and data processing tools that handle multilingual data.

Example:
    mls_dict = {"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}}
    mls = MultiLangString(mls_dict)
    mls.add_entry("Bonjour", "fr")
    print(mls.get_strings_lang("en"))  # Output: ['Hello', 'Good morning']
    print(mls)  # Output: "'Hello'@en, 'Good morning'@en, 'Hola'@es, 'Buenos días'@es, 'Bonjour'@fr"

By providing a comprehensive set of methods for managing multilingual text, the MultiLangString class aims to simplify
the development of multilingual applications and facilitate the handling of text in multiple languages.
"""
from typing import Any

from .langstring import LangString
from .multilangstring_control import MultiLangStringControl
from .multilangstring_control import MultiLangStringFlag
from .utils.validation_base import ValidationBase


class MultiLangString(ValidationBase):
    """A class for managing multilingual text strings with various language tags.

    Utilizes a global control strategy set in MultiLangStringControl to handle duplicate language tags. Supports
    operations like adding, removing, and retrieving language strings in multiple languages.

    :ivar pref_lang: The preferred language for this MultiLangString. Defaults to "en".
    :vartype pref_lang: str
    """

    def _get_control_and_flags_type(self) -> tuple[type[MultiLangStringControl], type[MultiLangStringFlag]]:
        """Retrieve the control class and its corresponding flags enumeration used in the MultiLangString class.

        This method provides the specific control class (MultiLangStringControl) and the flags enumeration
        (MultiLangStringFlag) that are used for configuring and validating the MultiLangString instances.
        It is essential for the functioning of the ValidationBase methods, which rely on these control settings.

        :return: A tuple containing the MultiLangStringControl class and the MultiLangStringFlag enumeration.
        :rtype: tuple[type[MultiLangStringControl], type[MultiLangStringFlag]]
        """
        return MultiLangStringControl, MultiLangStringFlag

    def _validate_langstring_arg(self, arg: Any) -> None:
        """Private helper method to validate if the argument is a LangString.

        :param arg: Argument to be checked.
        :type arg: Any
        :raises TypeError: If the passed argument is not an instance of LangString.
        """
        if not isinstance(arg, LangString):
            raise TypeError(
                f"MultiLangString received invalid argument. Expected a LangString but "
                f"received '{type(arg).__name__}' with value '{arg}'."
            )

    def __init__(self, mls_dict: dict[str, set[str]] = None, pref_lang: str = "en") -> None:
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
        if mls_dict and not isinstance(mls_dict, dict):
            raise TypeError(f"Invalid type for argument mls_dict. Expected 'dict', received '{type(mls_dict)}'.")
        if pref_lang and not isinstance(pref_lang, str):
            raise TypeError(f"Invalid type for argument pref_lang. Expected 'str', received '{type(pref_lang)}'.")

        if mls_dict is not None:
            self._validate_mls_dict(mls_dict)
        else:
            mls_dict = {}
        self.mls_dict: dict[str, set[str]] = mls_dict

        self._pref_lang: str = pref_lang

    # pref_lang GETTER
    @property
    def preferred_lang(self) -> str:
        """Get the preferred language for this MultiLangString.

        :return: The preferred language as a string.
        """
        return self._pref_lang

    # pref_lang SETTER
    @preferred_lang.setter
    def preferred_lang(self, preferred_lang_value: str) -> None:
        """Set the preferred language for this MultiLangString.

        :param preferred_lang_value: The preferred language as a string.
        :type preferred_lang_value: str
        :raises TypeError: If preferred_lang_value is not a string.
        """
        if isinstance(preferred_lang_value, str):
            self._pref_lang = preferred_lang_value
        else:
            raise TypeError(f"Invalid pref_lang type. Should be 'str', but is '{type(preferred_lang_value)}'.")

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
        self._validate_arguments(text, lang)
        self._validate_ensure_text(text)
        self._validate_ensure_any_lang(lang)
        self._validate_ensure_valid_lang(lang)

        if lang not in self.mls_dict:
            self.mls_dict[lang] = set()
        self.mls_dict[lang].add(text)

    def add_langstring(self, langstring: LangString) -> None:
        """Add a LangString to the MultiLangString.

        :param langstring: The LangString object to be added, representing a text in a specific language.
        :type langstring: LangString
        """
        self._validate_langstring_arg(langstring)
        self.add_entry(text=langstring.text, lang=langstring.lang)

    def remove_entry(self, text: str, lang: str) -> None:
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
            if len(self.mls_dict[lang]) == 0:
                del self.mls_dict[lang]
        else:
            raise ValueError(f"Entry '{text}@{lang}' not found in the MultiLangString.")

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

    def get_langstring(self, text: str, lang: str) -> LangString:
        """Retrieve a LangString object for a specific text and language.

        :param text: The text of the LangString.
        :type text: str
        :param lang: The language of the LangString.
        :type lang: str
        :return: A LangString object with the specified text and language.
        :rtype: LangString
        :raises ValueError: If the text/lang combination is not in mls_dict.
        """
        if lang in self.mls_dict and text in self.mls_dict[lang]:
            return LangString(text, lang)
        raise ValueError(f"Text '{text}' with language '{lang}' not found in mls_dict.")

    def get_langstrings_lang(self, lang: str) -> list[LangString]:
        """Retrieve a list of LangStrings for a given language.

        :param lang: The language for which to retrieve LangStrings.
        :type lang: str
        :return: A list of LangStrings, each containing a single entry for the specified language.
                 Returns an empty list if the specified language is not in mls_dict.
        :rtype: list[LangString]
        """
        if lang in self.mls_dict:
            return [LangString(text, lang) for text in self.mls_dict[lang]]
        return []

    def get_langstrings_all(self) -> list[LangString]:
        """Retrieve a list of all LangStrings in mls_dict.

        :return: A list of LangStrings, each representing a single entry from mls_dict.
        :rtype: list[LangString]
        """
        return [LangString(text, lang) for lang, texts in self.mls_dict.items() for text in texts]

    def get_langstrings_pref_lang(self) -> list[LangString]:
        """Retrieve a list of LangStrings for the preferred language.

        This method returns LangStrings for the language specified in the pref_lang attribute. If pref_lang is not
        a key in mls_dict, an empty list is returned.

        :return: A list of LangStrings for the preferred language.
        :rtype: list[LangString]
        """
        return self.get_langstrings_lang(self._pref_lang)

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

    def __repr__(self) -> str:
        """Return a detailed string representation of the MultiLangString object.

        This method provides a more verbose string representation of the MultiLangString, which includes the full
        dictionary of language strings and the preferred language, making it useful for debugging.

        :return: A detailed string representation of the MultiLangString.
        :rtype: str
        """
        return f"MultiLangString({self.mls_dict}, pref_lang='{self.preferred_lang}')"

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        This method provides a concise string representation of the MultiLangString, listing each LangString with its
        associated language tag.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        return ", ".join(
            f"{repr(langstring)}@{lang}" for lang, langstrings in self.mls_dict.items() for langstring in langstrings
        )

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
        """Generate a hash value for a MultiLangString object.

        The hash is computed based on the 'mls_dict' attribute of the MultiLangString. This approach ensures that
        MultiLangString objects with the same content will have the same hash value.

        :return: The hash value of the MultiLangString object.
        :rtype: int
        """
        # Convert dictionary to a hashable form (tuple of tuples) for consistent hashing
        hashable_mls_dict = tuple((lang, frozenset(texts)) for lang, texts in self.mls_dict.items())
        return hash(hashable_mls_dict)

    def _validate_mls_dict(self, mls_dict: dict[str, set[str]]) -> None:
        """
        Validate all elements in the provided mls_dict against the current flags' values.

        Iterates through each language and its associated texts in the mls_dict, applying validation methods to
        ensure compliance with the current flag settings.

        :param mls_dict: A dictionary where keys are language codes and values are sets of text entries.
        :type mls_dict: dict[str, set[str]]
        :raises TypeError: If any text or language in mls_dict does not comply with the expected types.
        :raises ValueError: If any text or language in mls_dict violates the rules set by the control flags.
        """
        control, flags = self._get_control_and_flags_type()

        for lang, texts in mls_dict.items():
            if not isinstance(texts, set):
                raise TypeError(f"Expected set of texts for language '{lang}', but got {type(texts).__name__}.")

            for text in texts:
                # Apply the validation methods to each text and language pair
                self._validate_arguments(text, lang)
                self._validate_ensure_text(text)

                # Only validate language tag if it's not empty
                if lang:
                    self._validate_ensure_any_lang(lang)
                    self._validate_ensure_valid_lang(lang)
