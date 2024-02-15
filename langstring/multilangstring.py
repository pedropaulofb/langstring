"""The MultiLangString module provides a class for managing and manipulating multilingual text strings.

It allows for the storage, retrieval, and manipulation of text strings in multiple languages, offering a flexible and
efficient way to handle multilingual content in applications.

The MultiLangString class utilizes a dictionary to store text entries associated with language tags, enabling the
representation and handling of text in various languages. It supports adding new entries, removing entries, and
retrieving entries in specific languages or across all languages. The class also allows setting a preferred language,
which can be used as a default for operations that involve retrieving text entries.

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

from .controller import Controller
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

    # --------------------------------------------------
    # Getters and Setters
    # --------------------------------------------------

    @property
    def mls_dict(self) -> dict[str, set[str]]:
        """Getter for texts."""
        return self._mls_dict

    @mls_dict.setter
    def mls_dict(self, new_mls_dict: dict[str, set[str]]) -> None:
        """Setter for mls_dict that ensures keys are strings and values are sets of strings."""
        if not isinstance(new_mls_dict, dict):
            raise TypeError(
                f"Invalid type of 'mls_dict' received. " f"Expected 'dict', got '{type(new_mls_dict).__name__}'."
            )

        temp_dict: dict[str, set[str]] = {}
        # Validating langs that are the dict's keys
        for lang, texts in new_mls_dict.items():
            if not isinstance(lang, str):
                raise TypeError(
                    f"Invalid 'lang' type in mls_dict init. Expected 'str', got '{type(new_mls_dict).__name__}'."
                )
            if not isinstance(texts, set):
                raise TypeError(
                    f"Invalid 'texts' type in mls_dict init. Expected 'set', got '{type(new_mls_dict).__name__}'."
                )

            validated_key = Validator.validate_lang(MultiLangStringFlag, lang)
            temp_dict[validated_key] = set()
            # Validating texts inside the dict's values
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
        self._pref_lang = Validator.validate_lang(MultiLangStringFlag, new_pref_lang)

    # --------------------------------------------------
    # MultiLangString's Regular Methods
    # --------------------------------------------------

    # ----- ADD METHODS -----

    def add(self, arg: Union[str, tuple[str, str], LangString, SetLangString]) -> None:
        if isinstance(arg, str):
            self.add_text_in_pref_lang(arg)
            return

        if isinstance(arg, LangString):
            self.add_langstring(arg)
            return

        if isinstance(arg, SetLangString):
            self.add_setlangstring(arg)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.add_entry(arg[0], arg[1])
            return

        raise TypeError(
            f"Argument '{arg}' must be of type 'str', 'tuple[str,str]', 'LangString', or 'SetLangString', "
            f"but got '{type(arg).__name__}'."
        )

    @Validator.validate_simple_type
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
        validated_text = Validator.validate_text(MultiLangStringFlag, text)
        validated_lang = Validator.validate_lang(MultiLangStringFlag, lang)

        registered_lang = self._get_registered_lang(validated_lang)

        if not registered_lang:
            self.mls_dict[validated_lang] = set()
            self.mls_dict[validated_lang].add(validated_text)
        else:
            self.mls_dict[registered_lang].add(validated_text)

    @Validator.validate_simple_type
    def add_text_in_pref_lang(self, text: str) -> None:
        """Add a text entry to the preferred language."""
        self.add_entry(text, self.pref_lang)

    @Validator.validate_simple_type
    def add_langstring(self, langstring: LangString) -> None:
        """Add a LangString to the MultiLangString.

        :param langstring: The LangString object to be added, representing a text in a specific language.
        :type langstring: LangString
        """
        self.add_entry(text=langstring.text, lang=langstring.lang)

    @Validator.validate_simple_type
    def add_setlangstring(self, setlangstring: SetLangString) -> None:
        """Add a SetLangString to the MultiLangString.

        :param setlangstring: The SetLangString object to be added, representing a text in a specific language.
        :type setlangstring: SetLangString
        """
        # Iterate through the texts in SetLangString and add them to the mls_dict
        for text in setlangstring.texts:
            self.add_entry(text=text, lang=setlangstring.lang)

    # ----- DISCARD METHODS -----

    def discard(self, arg: Union[str, tuple[str, str], LangString, SetLangString]) -> None:
        if isinstance(arg, str):
            self.discard_text_in_pref_lang(arg)
            return

        if isinstance(arg, LangString):
            self.discard_langstring(arg)
            return

        if isinstance(arg, SetLangString):
            self.discard_setlangstring(arg)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.discard_entry(arg[0], arg[1])
            return

        raise TypeError(
            f"Argument '{arg}' must be of type 'tuple[str,str]', 'LangString', or 'SetLangString', "
            f"but got '{type(arg).__name__}'."
        )

    @Validator.validate_simple_type
    def discard_entry(self, text: str, lang: str) -> None:
        registered_lang = self._get_registered_lang(lang)

        if registered_lang in self.mls_dict and text in self.mls_dict[registered_lang]:
            self.mls_dict[registered_lang].remove(text)
            if len(self.mls_dict[registered_lang]) == 0 and Controller.get_flag(MultiLangStringFlag.CLEAR_EMPTY_LANG):
                del self.mls_dict[registered_lang]

    @Validator.validate_simple_type
    def discard_text_in_pref_lang(self, text: str) -> None:
        """Discard a text entry from the preferred language."""
        self.discard_entry(text, self.pref_lang)

    @Validator.validate_simple_type
    def discard_langstring(self, langstring: LangString) -> None:
        self.discard_entry(text=langstring.text, lang=langstring.lang)

    @Validator.validate_simple_type
    def discard_setlangstring(self, setlangstring: SetLangString) -> None:
        for text in setlangstring.texts:
            self.discard_entry(text=text, lang=setlangstring.lang)

    @Validator.validate_simple_type
    def discard_lang(self, lang: str) -> None:
        registered_lang = self._get_registered_lang(lang)
        if registered_lang:
            del self.mls_dict[registered_lang]

    # TODO: Check if it is necessary/possible to have a discard/remove_multilangstring method.

    # ----- REMOVE METHODS -----

    def remove(self, arg: Union[str, tuple[str, str], LangString, SetLangString]) -> None:
        if isinstance(arg, str):
            self.remove_text_in_pref_lang(arg)
            return

        if isinstance(arg, LangString):
            self.remove_langstring(arg)
            return

        if isinstance(arg, SetLangString):
            self.remove_setlangstring(arg)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.remove_entry(arg[0], arg[1])
            return

        raise TypeError(
            f"Argument '{arg}' must be of type 'str', 'tuple[str,str]', 'LangString', or 'SetLangString', "
            f"but got '{type(arg).__name__}'."
        )

    @Validator.validate_simple_type
    def remove_entry(self, text: str, lang: str) -> None:
        """Remove a single entry from the set of a given language key in the dictionary.

        If the specified language key exists and the text is in its set, the text is removed. If this results in an
        empty set for the language, the language key is also removed from the dictionary.

        :param text: The text to be removed.
        :type text: str
        :param lang: The language key from which the text should be removed.
        :type lang: str
        """
        if self.contains_entry(text, lang):
            self.discard_entry(text, lang)
        else:
            raise ValueError(f"Entry '{text}@{lang}' not found in the MultiLangString.")

    @Validator.validate_simple_type
    def remove_text_in_pref_lang(self, text: str) -> None:
        """Remove a text entry from the preferred language."""
        self.remove_entry(text, self.pref_lang)

    @Validator.validate_simple_type
    def remove_langstring(self, langstring: LangString) -> None:
        self.remove_entry(langstring.text, langstring.lang)

    @Validator.validate_simple_type
    def remove_setlangstring(self, setlangstring: SetLangString) -> None:
        for text in setlangstring.texts:
            self.remove_entry(text, setlangstring.lang)

    @Validator.validate_simple_type
    def remove_lang(self, lang: str) -> None:
        """Remove all entries of a given language from the dictionary.

        If the specified language key exists, it and all its associated texts are removed from the dictionary.

        :param lang: The language key to be removed along with all its texts.
        :type lang: str
        """
        registered_lang = self._get_registered_lang(lang)
        if registered_lang:
            del self.mls_dict[registered_lang]
        else:
            raise ValueError(f"Lang '{lang}' not found in the MultiLangString.")

    # ----- CONVERSION METHODS -----

    @Validator.validate_simple_type
    def to_langstrings(self, languages: Optional[list[str]] = None) -> list[LangString]:
        langstrings = []
        selected_langs = self.mls_dict.keys() if languages is None else languages

        for lang in selected_langs:
            if lang in self.mls_dict:
                for text in self.mls_dict[lang]:
                    langstrings.append(LangString(text, lang))

        return langstrings

    @Validator.validate_simple_type
    def to_setlangstrings(self, languages: Optional[list[str]] = None) -> list[SetLangString]:
        setlangstrings = []
        selected_langs = self.mls_dict.keys() if languages is None else languages

        for lang in selected_langs:
            if lang in self.mls_dict:
                setlangstrings.append(SetLangString(self.mls_dict[lang], lang))

        return setlangstrings

    @Validator.validate_simple_type
    def to_strings(
        self,
        languages: Optional[list[str]] = None,
        print_quotes: bool = True,
        separator: str = "@",
        print_lang: bool = True,
    ) -> list[str]:
        strings = []
        selected_langs = self.mls_dict.keys() if languages is None else languages

        for lang in selected_langs:
            if lang in self.mls_dict:
                for text in self.mls_dict[lang]:
                    new_text = f'"{text}"' if print_quotes else text
                    new_lang = f"{separator}{lang}" if print_lang else ""
                    strings.append(f"{new_text}{new_lang}")

        return strings

    # ----- COUNT METHODS -----

    def count_lang_entries(self) -> dict[str, int]:
        """
        Returns the number of text entries for each language.

        :return: A dictionary with language codes as keys and counts of text entries as values.
        """
        return {lang: len(texts) for lang, texts in self.mls_dict.items()}

    def count_langs(self) -> int:
        return len(self.mls_dict)

    def count_total_entries(self) -> int:
        """Return the total number of text entries across all languages."""
        return sum(len(texts) for texts in self.mls_dict.values())

    # ----- CONTAIN METHODS -----

    def contains(self, arg: Union[str, tuple[str, str], LangString, SetLangString]) -> None:
        if isinstance(arg, str):
            self.contains_text_in_pref_lang(arg)
            return

        if isinstance(arg, LangString):
            self.contains_langstring(arg)
            return

        if isinstance(arg, SetLangString):
            self.contains_setlangstring(arg)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.contains_entry(arg[0], arg[1])
            return

        raise TypeError(
            f"Argument '{arg}' must be of type 'str', 'tuple[str,str]', 'LangString', or 'SetLangString', "
            f"but got '{type(arg).__name__}'."
        )

    @Validator.validate_simple_type
    def contains_entry(self, text: str, lang: str) -> bool:
        return lang in self.mls_dict and text in self.mls_dict[lang]

    @Validator.validate_simple_type
    def contains_text_in_pref_lang(self, text: str) -> bool:
        """Check if a specific text exists in the preferred language."""
        return self.contains_entry(text, self.pref_lang)

    @Validator.validate_simple_type
    def contains_langstring(self, langstring: LangString) -> bool:
        """Check if the given LangString's text and lang are part of this MultiLangString.

        :param langstring: A LangString object to check.
        :return: True if the LangString's text is found within the specified language's set; otherwise, False.
        """
        # Check if the lang exists in the mls_dict and if the text exists within that language's set.
        return langstring.lang in self.mls_dict and langstring.text in self.mls_dict[langstring.lang]

    @Validator.validate_simple_type
    def contains_setlangstring(self, setlangstring: SetLangString) -> bool:
        """Check if all texts and the language of a SetLangString are part of this MultiLangString.

        :param setlangstring: A SetLangString object to check.
        :return: True if the SetLangString's language exists and all its texts are found within the specified
        language's set; otherwise, False.
        """
        # First, check if the language exists in the MultiLangString
        if setlangstring.lang not in self.mls_dict:
            return False

        # Then, check if every text in the SetLangString is in the MultiLangString's set for that language
        return setlangstring.texts.issubset(self.mls_dict[setlangstring.lang])

    # ----- GENERAL METHODS -----

    def clear_empty_langs(self) -> None:
        empty_langs = [lang for lang, text in self.mls_dict.items() if not text]
        for lang in empty_langs:
            del self.mls_dict[lang]

    @Validator.validate_simple_type
    def has_lang(self, lang: str) -> bool:
        return self._get_registered_lang(lang)

    # --------------------------------------------------
    # Overwritten Dictionary's Built-in Regular Methods
    # --------------------------------------------------

    def copy(self) -> "MultiLangString":
        """Create a shallow copy of the MultiLangString instance.

        Returns a new MultiLangString instance with a shallow copy of the internal dictionary.
        """
        new_mls_dict = self.mls_dict.copy()  # Shallow copy of the dictionary
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=self.pref_lang)

    @classmethod
    def fromkeys(cls, seq, value=None) -> "MultiLangString":
        """Create a new MultiLangString instance with keys from seq and values set to value."""
        return cls({k: set(value) if value is not None else set() for k in seq})

    def get(self, key, default=None):
        """Return the value for key if key is in the dictionary, else default."""
        return self.mls_dict.get(key, default)

    def items(self):
        """Return items (language, texts set) in the MultiLangString."""
        return self.mls_dict.items()

    def keys(self):
        """Return the languages in the MultiLangString."""
        return self.mls_dict.keys()

    def pop(self, key, default=None):
        """Remove specified key and returns its value. If key is not found, default is returned if given."""
        return self.mls_dict.pop(key, default)

    def popitem(self):
        """Remove and returns a (key, value) pair as a 2-tuple."""
        return self.mls_dict.popitem()

    def setdefault(self, key, default=None):
        """If key is in the dict, return its value. If not, insert key with a value of default and return default."""
        return self.mls_dict.setdefault(key, default if default is not None else set())

    def update(self, other):
        """Update the dictionary with the key/value pairs from other, overwriting existing keys."""
        if isinstance(other, MultiLangString):
            self.mls_dict.update(other.mls_dict)
        elif isinstance(other, dict):
            self.mls_dict.update(other)
        else:
            for key, value in other:
                self.mls_dict[key] = value

    def values(self):
        """Return the sets of texts in the MultiLangString."""
        return self.mls_dict.values()

    # --------------------------------------------------
    # MultiLangString's Dunder Methods
    # --------------------------------------------------

    # TODO: Check if there is no __add__ method and if it is necessary to implement one.

    def __contains__(self, key: str) -> bool:
        """Check if a language is in the MultiLangString."""
        return key in self.mls_dict

    def __delitem__(self, key: str) -> None:
        """Allow deletion of language entries."""
        del self.mls_dict[key]

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

    def __getitem__(self, key: str) -> set[str]:
        """Allow retrieval of entries by language."""
        return self.mls_dict[key]

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

    def __ior__(self, other):
        """Implement in-place update operation (equivalent to self.update(other))."""
        self.update(other)
        return self

    def __iter__(self):
        """Allow iteration over the dictionary keys (language codes)."""
        return iter(self.mls_dict)

    def __len__(self) -> int:
        """Return the number of languages in the dictionary."""
        return len(self.mls_dict)

    def __ne__(self, other):
        """Define behavior for the inequality operator, !=."""
        if isinstance(other, MultiLangString):
            return self.mls_dict != other.mls_dict
        return self.mls_dict != other

    def __or__(self, other):
        """Implement merge operation, returning a new MultiLangString with merged content."""
        if not isinstance(other, (MultiLangString, dict)):
            return NotImplemented
        new_dict = self.mls_dict.copy()
        new_dict.update(other.mls_dict if isinstance(other, MultiLangString) else other)
        return MultiLangString(new_dict, self.pref_lang)

    def __repr__(self) -> str:
        """Return a detailed string representation of the MultiLangString object.

        This method provides a more verbose string representation of the MultiLangString, which includes the full
        dictionary of language strings and the preferred language, making it useful for debugging.

        :return: A detailed string representation of the MultiLangString.
        :rtype: str
        """
        class_name = self.__class__.__name__
        mls_dict_repr = repr(self.mls_dict)  # Provides a string representation of the dictionary
        pref_lang_repr = repr(self.pref_lang)  # Wraps the pref_lang in quotes
        return f"{class_name}(mls_dict={mls_dict_repr}, pref_lang={pref_lang_repr})"

    def __reversed__(self):
        """Return a reverse iterator over the dictionary keys."""
        return reversed(self.mls_dict.keys())

    def __ror__(self, other):
        """Implement right-side merge, used if the left operand does not support merge."""
        if not isinstance(other, dict):
            return NotImplemented
        # Create a new MultiLangString instance with 'other' as the base, then update with self
        new_instance = MultiLangString(other)
        new_instance.update(self.mls_dict)
        return new_instance

    def __setitem__(self, key: str, value: set[str]) -> None:
        """Allow setting entries by language."""
        self.mls_dict[key] = value

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        This method provides a concise string representation of the MultiLangString, listing each text entry with its
        associated language tag.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        parts = []
        for lang, texts in self.mls_dict.items():
            texts_repr = ", ".join(
                [f'"{text}"' if Controller.get_flag(MultiLangStringFlag.PRINT_WITH_QUOTES) else text for text in texts]
            )
            lang_representation = f"@{lang}" if Controller.get_flag(MultiLangStringFlag.PRINT_WITH_LANG) else ""
            parts.append(f"{{{texts_repr}}}{lang_representation}")

        # Join all language representations with a comma and space
        return ", ".join(parts)

    # --------------------------------------------------
    # Private Methods
    # --------------------------------------------------

    @Validator.validate_simple_type
    def _get_registered_lang(self, lang: str) -> Union[str, None]:
        lang_register = {s.casefold(): s for s in self.mls_dict.keys()}
        if lang.casefold() in lang_register:
            return lang_register[lang.casefold()]
        return None
