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

    def __init__(self, mls_dict: Optional[dict[str, set[str]]] = None, pref_lang: Optional[str] = "en") -> None:
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
        self.mls_dict = mls_dict
        self.pref_lang: str = pref_lang

    # --------------------------------------------------
    # Properties' Getters and Setters
    # --------------------------------------------------

    @property
    def mls_dict(self) -> dict[str, set[str]]:
        """Getter for texts."""
        return self._mls_dict

    @mls_dict.setter
    def mls_dict(self, in_mls_dict: Optional[dict[str, set[str]]]) -> None:
        """Setter for mls_dict that ensures keys are strings and values are sets of strings."""

        in_mls_dict = {} if in_mls_dict is None else in_mls_dict

        # Validate input before merging
        Validator.validate_type_iterable(in_mls_dict, dict, str)
        for key in in_mls_dict:
            Validator.validate_type_iterable(in_mls_dict[key], set, str)

        # Merge entries with case-insensitive language keys
        new_mls_dict = self._merge_language_entries(in_mls_dict)

        # Validate and transform texts in the merged dictionary
        temp_dict: dict[str, set[str]] = {}
        for lang, texts in new_mls_dict.items():
            validated_key = Validator.validate_flags_lang(MultiLangStringFlag, lang)
            temp_dict[validated_key] = set()
            # Validating texts inside the dict's values
            for text in texts:
                validated_value = Validator.validate_flags_text(MultiLangStringFlag, text)
                temp_dict[validated_key].add(validated_value)

        self._mls_dict = temp_dict

    @property
    def pref_lang(self) -> str:
        """Get the preferred language for this MultiLangString.

        :return: The preferred language as a string.
        """
        return self._pref_lang

    @pref_lang.setter
    def pref_lang(self, new_pref_lang: Optional[str]) -> None:
        """Set the preferred language for this MultiLangString.

        :param new_pref_lang: The preferred language as a string.
        :type new_pref_lang: str
        """
        new_pref_lang = "en" if new_pref_lang is None else new_pref_lang
        Validator.validate_type_single(new_pref_lang, str)
        self._pref_lang = Validator.validate_flags_lang(MultiLangStringFlag, new_pref_lang)

    # --------------------------------------------------
    # MultiLangString's Regular Methods
    # --------------------------------------------------

    # ----- ADD METHODS -----

    def add(self, arg: Union[tuple[str, str], LangString, SetLangString, "MultiLangString"]) -> None:
        if isinstance(arg, LangString):
            self.add_langstring(arg)
            return

        if isinstance(arg, SetLangString):
            self.add_setlangstring(arg)
            return

        if isinstance(arg, MultiLangString):
            self.add_multilangstring(arg)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.add_entry(arg[0], arg[1])
            return

        raise TypeError(
            f"Argument with value '{arg}' must be of type "
            f"'tuple[str,str]', 'LangString', 'SetLangString', or 'MultiLangString', but got '{type(arg).__name__}'."
        )

    @Validator.validate_type_decorator
    def add_entry(self, text: str, lang: Optional[str]) -> None:
        """Add a text entry to the MultiLangString under a specified language.

        Validates the provided text and language against the current flag settings before adding. If the specified
        language does not exist in the mls_dict, a new set for that language is created. The text is then added to
        this set. If the language already exists, the text is added to the existing set for that language.

        :param text: The text to be added to the MultiLangString.
        :type text: str
        :param lang: The language under which the text should be added. If not specified, defaults to an empty string.
        :type lang: str
        """
        validated_text = Validator.validate_flags_text(MultiLangStringFlag, text)
        validated_lang = Validator.validate_flags_lang(MultiLangStringFlag, lang)

        registered_lang = self._get_registered_lang(validated_lang)

        if registered_lang is None:
            self.mls_dict[validated_lang] = set()
            self.mls_dict[validated_lang].add(validated_text)
        else:
            self.mls_dict[registered_lang].add(validated_text)

    @Validator.validate_type_decorator
    def add_text_in_pref_lang(self, text: str) -> None:
        """Add a text entry to the preferred language."""
        self.add_entry(text, self.pref_lang)

    @Validator.validate_type_decorator
    def add_langstring(self, langstring: LangString) -> None:
        """Add a LangString to the MultiLangString.

        :param langstring: The LangString object to be added, representing a text in a specific language.
        :type langstring: LangString
        """
        self.add_entry(text=langstring.text, lang=langstring.lang)

    @Validator.validate_type_decorator
    def add_setlangstring(self, setlangstring: SetLangString) -> None:
        """Add a SetLangString to the MultiLangString.

        :param setlangstring: The SetLangString object to be added, representing a text in a specific language.
        :type setlangstring: SetLangString
        """
        self.add_empty_lang(setlangstring.lang)
        # Iterate through the texts in SetLangString and add them to the mls_dict
        for text in setlangstring.texts:
            self.add_entry(text=text, lang=setlangstring.lang)

    @Validator.validate_type_decorator
    def add_multilangstring(self, multilangstring: "MultiLangString") -> None:
        for lang in multilangstring.mls_dict:
            self.add_empty_lang(lang)
            for text in multilangstring.mls_dict[lang]:
                self.add_entry(text=text, lang=lang)

    @Validator.validate_type_decorator
    def add_empty_lang(self, lang: str) -> None:
        validated_lang = Validator.validate_flags_lang(MultiLangStringFlag, lang)
        registered_lang = self._get_registered_lang(validated_lang)
        if registered_lang is None:
            self.mls_dict[validated_lang] = set()

    # ----- DISCARD METHODS -----

    def discard(
        self, arg: Union[tuple[str, str], LangString, SetLangString, "MultiLangString"], clean_empty: bool = False
    ) -> None:
        if isinstance(arg, LangString):
            self.discard_langstring(arg, clean_empty)
            return

        if isinstance(arg, SetLangString):
            self.discard_setlangstring(arg, clean_empty)
            return

        if isinstance(arg, MultiLangString):
            self.discard_multilangstring(arg, clean_empty)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.discard_entry(arg[0], arg[1], clean_empty)
            return

        raise TypeError(
            f"Argument with value '{arg}' must be of type "
            f"'tuple[str,str]', 'LangString', 'SetLangString', or 'MultiLangString', but got '{type(arg).__name__}'."
        )

    @Validator.validate_type_decorator
    def discard_entry(self, text: str, lang: str, clean_empty: bool = False) -> None:
        registered_lang = self._get_registered_lang(lang)

        if registered_lang in self.mls_dict and text in self.mls_dict[registered_lang]:
            self.mls_dict[registered_lang].remove(text)
            if len(self.mls_dict[registered_lang]) == 0 and clean_empty:
                del self.mls_dict[registered_lang]

    @Validator.validate_type_decorator
    def discard_text_in_pref_lang(self, text: str, clean_empty: bool = False) -> None:
        """Discard a text entry from the preferred language."""
        self.discard_entry(text, self.pref_lang, clean_empty)

    @Validator.validate_type_decorator
    def discard_langstring(self, langstring: LangString, clean_empty: bool = False) -> None:
        self.discard_entry(text=langstring.text, lang=langstring.lang, clean_empty=clean_empty)

    @Validator.validate_type_decorator
    def discard_setlangstring(self, setlangstring: SetLangString, clean_empty: bool = False) -> None:
        for text in setlangstring.texts:
            self.discard_entry(text=text, lang=setlangstring.lang, clean_empty=clean_empty)

    @Validator.validate_type_decorator
    def discard_multilangstring(self, multilangstring: "MultiLangString", clean_empty: bool = False) -> None:
        for lang in multilangstring.mls_dict:
            for text in list(multilangstring.mls_dict[lang]):
                self.discard_entry(text=text, lang=lang, clean_empty=clean_empty)

    @Validator.validate_type_decorator
    def discard_lang(self, lang: str) -> None:
        registered_lang = self._get_registered_lang(lang)
        if registered_lang is not None:
            del self.mls_dict[registered_lang]

    # ----- REMOVE METHODS -----

    def remove(
        self, arg: Union[tuple[str, str], LangString, SetLangString, "MultiLangString"], clean_empty: bool = False
    ) -> None:
        if isinstance(arg, LangString):
            self.remove_langstring(arg, clean_empty)
            return

        if isinstance(arg, SetLangString):
            self.remove_setlangstring(arg, clean_empty)
            return

        if isinstance(arg, MultiLangString):
            self.remove_multilangstring(arg, clean_empty)
            return

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            self.remove_entry(arg[0], arg[1], clean_empty)
            return

        raise TypeError(
            f"Argument with value '{arg}' must be of type 'tuple[str,str]', 'LangString', 'SetLangString', or 'MultiLangString', "
            f"but got '{type(arg).__name__}'."
        )

    @Validator.validate_type_decorator
    def remove_entry(self, text: str, lang: str, clean_empty: bool = False) -> None:
        """Remove a single entry from the set of a given language key in the dictionary.

        If the specified language key exists and the text is in its set, the text is removed. If this results in an
        empty set for the language, the language key is also removed from the dictionary.

        :param text: The text to be removed.
        :type text: str
        :param lang: The language key from which the text should be removed.
        :type lang: str
        """
        if self.contains_entry(text, lang):
            self.discard_entry(text, lang, clean_empty)
        else:
            raise ValueError(f"Entry '{text}@{lang}' not found in the MultiLangString.")

    @Validator.validate_type_decorator
    def remove_text_in_pref_lang(self, text: str, clean_empty: bool = False) -> None:
        """Remove a text entry from the preferred language."""
        self.remove_entry(text, self.pref_lang, clean_empty)

    @Validator.validate_type_decorator
    def remove_langstring(self, langstring: LangString, clean_empty: bool = False) -> None:
        self.remove_entry(langstring.text, langstring.lang, clean_empty)

    @Validator.validate_type_decorator
    def remove_setlangstring(self, setlangstring: SetLangString, clean_empty: bool = False) -> None:
        for text in setlangstring.texts:
            self.remove_entry(text, setlangstring.lang, clean_empty)

    @Validator.validate_type_decorator
    def remove_multilangstring(self, multilangstring: "MultiLangString", clean_empty: bool = False) -> None:
        for lang in multilangstring.mls_dict:
            for text in multilangstring.mls_dict[lang]:
                self.remove_entry(text=text, lang=lang, clean_empty=clean_empty)

    @Validator.validate_type_decorator
    def remove_lang(self, lang: str) -> None:
        """Remove all entries of a given language from the dictionary.

        If the specified language key exists, it and all its associated texts are removed from the dictionary.

        :param lang: The language key to be removed along with all its texts.
        :type lang: str
        """
        registered_lang = self._get_registered_lang(lang)
        if registered_lang is not None:
            del self.mls_dict[registered_lang]
        else:
            raise ValueError(f"Lang '{lang}' not found in the MultiLangString.")

    def remove_empty_langs(self) -> None:
        empty_langs = [lang for lang, text in self.mls_dict.items() if not text]
        for lang in empty_langs:
            del self.mls_dict[lang]

    # ----- CONVERSION METHODS -----

    def to_strings(
        self,
        langs: Optional[list[str]] = None,
        print_quotes: Optional[bool] = None,
        separator: str = "@",
        print_lang: Optional[bool] = None,
    ) -> list[str]:
        Validator.validate_type_iterable(langs, list, str, optional=True)
        Validator.validate_type_single(print_quotes, bool, optional=True)
        Validator.validate_type_single(separator, str)
        Validator.validate_type_single(print_lang, bool, optional=True)

        if print_quotes is None:
            print_quotes = Controller.get_flag(MultiLangStringFlag.PRINT_WITH_QUOTES)
        if print_lang is None:
            print_lang = Controller.get_flag(MultiLangStringFlag.PRINT_WITH_LANG)

        strings = []
        selected_langs = langs if (langs is not None) else list(self.mls_dict.keys())

        for lang in selected_langs:
            registered_lang = self._get_registered_lang(lang)

            if registered_lang is not None:
                for text in self.mls_dict[registered_lang]:
                    new_text = f'"{text}"' if print_quotes else text
                    new_lang = f"{separator}{lang}" if print_lang else ""
                    strings.append(f"{new_text}{new_lang}")

        return sorted(strings)

    def to_langstrings(self, langs: Optional[list[str]] = None) -> list[LangString]:
        Validator.validate_type_iterable(langs, list, str, optional=True)

        langstrings = []
        self_reg_langs = []

        selected_langs = self.mls_dict.keys() if (langs is None) else langs

        for selected_lang in selected_langs:
            reg_lang = self._get_registered_lang(selected_lang)
            if reg_lang is not None:
                self_reg_langs.append(reg_lang)

        for lang in self_reg_langs:
            for text in self.mls_dict[lang]:
                langstrings.append(self.get_langstring(text, lang))

        return langstrings

    def to_setlangstrings(self, langs: Optional[list[str]] = None) -> list[SetLangString]:
        Validator.validate_type_iterable(langs, list, str, optional=True)

        setlangstrings = []
        self_reg_langs = []

        selected_langs = self.mls_dict.keys() if (langs is None) else langs

        for selected_lang in selected_langs:
            reg_lang = self._get_registered_lang(selected_lang)
            if reg_lang is not None:
                self_reg_langs.append(reg_lang)

        for reg_lang in self_reg_langs:
            setlangstrings.append(self.get_setlangstring(reg_lang))

        return setlangstrings

    # ----- COUNT METHODS -----

    @Validator.validate_type_decorator
    def count_entries_by_lang(self, lang: str) -> int:
        # Count the number of texts a given lang has.
        registered_lang = self._get_registered_lang(lang)
        return 0 if registered_lang is None else len(self.mls_dict[registered_lang])

    def count_entries_per_lang(self) -> dict[str, int]:
        """Return the number of text entries for each language.

        :return: A dictionary with language codes as keys and counts of text entries as values.
        """
        return {lang: len(texts) for lang, texts in self.mls_dict.items()}

    def count_entries_total(self) -> int:
        """Return the total number of text entries across all languages."""
        return sum(len(texts) for texts in self.mls_dict.values())

    def count_langs_total(self) -> int:
        # Count the total number of langs the MultiLangString has.
        return len(self.mls_dict)

    # ----- CONTAIN METHODS -----

    def contains(self, arg: Union[tuple[str, str], LangString, SetLangString, "MultiLangString"]) -> bool:
        if isinstance(arg, LangString):
            return self.contains_langstring(arg)

        if isinstance(arg, SetLangString):
            return self.contains_setlangstring(arg)

        if isinstance(arg, MultiLangString):
            return self.contains_multilangstring(arg)

        if isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(a, str) for a in arg):
            return self.contains_entry(arg[0], arg[1])

        raise TypeError(
            f"Argument with value '{arg}' must be of type "
            f"'tuple[str,str]', 'LangString', 'SetLangString', or 'MultiLangString', but got '{type(arg).__name__}'."
        )

    @Validator.validate_type_decorator
    def contains_entry(self, text: str, lang: str) -> bool:
        registered_lang = self._get_registered_lang(lang)
        return False if (registered_lang is None) else (text in self.mls_dict[registered_lang])

    @Validator.validate_type_decorator
    def contains_lang(self, lang: str) -> bool:
        return self._get_registered_lang(lang) is not None

    @Validator.validate_type_decorator
    def contains_text_in_pref_lang(self, text: str) -> bool:
        """Check if a specific text exists in the preferred language."""
        return self.contains_entry(text, self.pref_lang)

    @Validator.validate_type_decorator
    def contains_text_in_any_lang(self, text: str) -> bool:
        """Check if a specific text exists in the preferred language."""
        for lang in self.mls_dict:
            if text in self.mls_dict[lang]:
                return True
        return False

    @Validator.validate_type_decorator
    def contains_langstring(self, langstring: LangString) -> bool:
        """Check if the given LangString's text and lang are part of this MultiLangString.

        :param langstring: A LangString object to check.
        :return: True if the LangString's text is found within the specified language's set; otherwise, False.
        """
        return self.contains_entry(langstring.text, langstring.lang)

    @Validator.validate_type_decorator
    def contains_setlangstring(self, setlangstring: SetLangString) -> bool:
        """Check if all texts and the language of a SetLangString are part of this MultiLangString.

        :param setlangstring: A SetLangString object to check.
        :return: True if the SetLangString's language exists and all its texts are found within the specified
        language's set; otherwise, False.
        """
        # If the setlangstring.texts is empty, it will return true
        for text in setlangstring.texts:
            if not self.contains_entry(text, setlangstring.lang):
                return False
        return True

    @Validator.validate_type_decorator
    def contains_multilangstring(self, multilangstring: "MultiLangString") -> bool:
        """Check if the current instance contains all languages and texts of another MultiLangString instance.

        :param multilangstring: The MultiLangString instance to check against.
        :return: True if all languages and their respective texts in `multilangstring` are contained in this instance,
        False otherwise.
        """
        for lang, texts in multilangstring.mls_dict.items():
            for text in texts:
                if not self.contains_entry(text, lang):
                    return False
        return True

    # ----- GET METHODS -----

    @Validator.validate_type_decorator
    def get_langs(self, casefold: bool = False) -> list[str]:
        """Return a list with all languages in the MultiLangString."""
        return [lang.lower() for lang in self.mls_dict.keys()] if casefold else list(self.mls_dict.keys())

    def get_texts(self) -> list[str]:
        """Return a sorted list with all texts in the MultiLangString."""
        result = [item for subset in self.mls_dict.values() for item in subset]
        result.sort()
        return result

    @Validator.validate_type_decorator
    def get_langstring(self, text: str, lang: str) -> LangString:
        return LangString(text=text, lang=lang) if self.contains_entry(text=text, lang=lang) else LangString(lang=lang)

    @Validator.validate_type_decorator
    def get_setlangstring(self, lang: str) -> SetLangString:
        registered_lang = self._get_registered_lang(lang)
        if registered_lang is not None:
            return SetLangString(texts=self.mls_dict[registered_lang], lang=lang)
        return SetLangString(lang=lang)

    def get_multilangstring(self, langs: list[str]) -> "MultiLangString":
        Validator.validate_type_iterable(langs, list, str)

        new_mls = MultiLangString()
        for lang in langs:
            if self.contains_lang(lang):
                new_sls = self.get_setlangstring(lang)
                new_mls.add_setlangstring(new_sls)

        return new_mls

    # ----- POP METHODS -----

    @Validator.validate_type_decorator
    def pop_langstring(self, text: str, lang: str) -> Optional[LangString]:
        if self.contains_entry(text=text, lang=lang):
            new_ls = self.get_langstring(text=text, lang=lang)
            self.remove_entry(text=text, lang=lang)
            return new_ls

    @Validator.validate_type_decorator
    def pop_setlangstring(self, lang: str) -> Optional[SetLangString]:
        if self.contains_lang(lang=lang):
            new_sls = self.get_setlangstring(lang=lang)
            self.remove_lang(lang=lang)
            return new_sls

    def pop_multilangstring(self, langs: list[str]) -> "MultiLangString":
        Validator.validate_type_iterable(langs, list, str)

        new_mls = self.get_multilangstring(langs)
        for lang in langs:
            self.discard_lang(lang)
        return new_mls

    # ----- GENERAL METHODS -----

    def has_pref_lang_entries(self) -> bool:
        registered_lang = self._get_registered_lang(self.pref_lang)
        return len(self.mls_dict[registered_lang]) > 0 if (registered_lang is not None) else False

    # --------------------------------------------------
    # Overwritten Dictionary's Dunder Methods
    # --------------------------------------------------

    @Validator.validate_type_decorator
    def __contains__(self, lang: str) -> bool:
        """Check if a language is in the MultiLangString."""
        return self.contains_lang(lang)

    @Validator.validate_type_decorator
    def __delitem__(self, lang: str) -> None:
        """Allow deletion of language entries."""
        reg_lang = self._get_registered_lang(lang)

        # Del valid using registered lang or raise KeyError when invalid (not registered in any case)
        del_lang = reg_lang if (reg_lang is not None) else lang
        del self.mls_dict[del_lang]

    @Validator.validate_type_decorator
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
            return NotImplemented

        # Convert langs to casefolded version for both instances for comparison
        casefolded_self = {k.casefold(): v for k, v in self.mls_dict.items()}
        casefolded_other = {k.casefold(): v for k, v in other.mls_dict.items()}

        # Check if the sets of casefolded langs are the same
        if set(casefolded_self.keys()) != set(casefolded_other.keys()):
            return False

        # Check if the values of corresponding casefolded langs are the same
        for lang in casefolded_self:
            if casefolded_self[lang] != casefolded_other[lang]:
                return False

        return True

    @Validator.validate_type_decorator
    def __getitem__(self, lang: str) -> set[str]:
        """Allow retrieval of entries by language."""

        reg_lang = self._get_registered_lang(lang)

        # Get valid using registered lang or raise KeyError when invalid (not registered in any case)
        get_lang = reg_lang if (reg_lang is not None) else lang
        return self.mls_dict[get_lang]

    def __hash__(self) -> int:
        """Generate a hash new_text for a MultiLangString object.

        The hash is computed based on the 'mls_dict' attribute of the MultiLangString. This approach ensures that
        MultiLangString objects with the same content will have the same hash new_text.

        :return: The hash new_text of the MultiLangString object.
        :rtype: int
        """
        # Create a casefolded version of mls_dict with sorted values
        hashable_data = tuple(
            (lang.casefold(), tuple(sorted(self.mls_dict[lang])))
            for lang in sorted(self.mls_dict.keys(), key=str.casefold)
        )

        # Hash the hashable_data
        return hash(hashable_data)

    def __iter__(self):
        """Allow iteration over the dictionary keys (language codes)."""
        return iter(self.mls_dict)

    def __len__(self) -> int:
        """Return the number of languages in the dictionary."""
        return len(self.mls_dict)

    def __repr__(self) -> str:
        """Return a detailed string representation of the MultiLangString object.

        This method provides a more verbose string representation of the MultiLangString, which includes the full
        dictionary of language strings and the preferred language, making it useful for debugging.

        :return: A detailed string representation of the MultiLangString.
        :rtype: str
        """
        return f"{self.__class__.__name__}(mls_dict={repr(self.mls_dict)}, pref_lang={repr(self.pref_lang)})"

    def __reversed__(self):
        """Return a reverse iterator over the dictionary keys."""
        return reversed(self.mls_dict)

    def __setitem__(self, lang: str, texts: set[str]) -> None:
        # TODO: Maybe update to accept also list? Verify other methods that should also accept list.
        """Allow setting entries by language."""
        Validator.validate_type_single(lang, str)
        Validator.validate_type_iterable(texts, set, str)

        registered_lang = self._get_registered_lang(lang)
        add_lang = registered_lang if (registered_lang is not None) else lang

        self.mls_dict[add_lang] = set()
        if texts:
            for text in texts:
                self.add_entry(text, add_lang)

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        This method provides a concise string representation of the MultiLangString, listing each text entry with its
        associated language tag.

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        if not self.mls_dict:
            return "{}"

        formatted_items = []
        print_lang = Controller.get_flag(MultiLangStringFlag.PRINT_WITH_LANG)
        print_quotes = Controller.get_flag(MultiLangStringFlag.PRINT_WITH_QUOTES)
        for lang, texts in sorted(self.mls_dict.items()):  # Sort languages
            if texts:
                sorted_texts = sorted(texts)  # Sort texts within the language
                if print_quotes:
                    formatted_texts = "{" + ", ".join(f"'{text}'" for text in sorted_texts) + "}"
                else:
                    formatted_texts = "{" + ", ".join(f"{text}" for text in sorted_texts) + "}"
            else:
                formatted_texts = "{}"

            if print_lang:
                formatted_lang = f"@{lang}" if print_lang else ""
                formatted_item = f"{formatted_texts}{formatted_lang}"
            else:
                formatted_item = formatted_texts

            formatted_items.append(formatted_item)

        # TODO: JUSTIFY IN DOCSTRINGS THAT IT IS SORTED TO BE DETERMINISTIC
        sorted_formatted_items = sorted(formatted_items)  # Sort the formatted items
        result_string = ", ".join(sorted_formatted_items)
        return result_string

    # --------------------------------------------------
    # Static Methods
    # --------------------------------------------------

    @staticmethod
    def merge_multilangstrings(multilangstrings: list["MultiLangString"]) -> "MultiLangString":
        Validator.validate_type_iterable(multilangstrings, list, MultiLangString)

        if len(multilangstrings):
            unified_mls = multilangstrings[0]  # Initialize with the first element
            for mls in multilangstrings[1:]:  # Loop through elements from the second to the last
                unified_mls.add_multilangstring(mls)
        else:
            unified_mls = MultiLangString()

        return unified_mls

    # --------------------------------------------------
    # Private Methods
    # --------------------------------------------------

    @Validator.validate_type_decorator
    def _get_registered_lang(self, lang: str) -> Union[str, None]:
        lang_register = {s.casefold(): s for s in self.mls_dict.keys()}
        if lang.casefold() in lang_register:
            return lang_register[lang.casefold()]
        return None

    @staticmethod
    def _merge_language_entries(mls_dict: dict[str, set[str]]) -> dict[str, set[str]]:
        """Merge entries in the provided dict where the lang codes match case-insensitively. For duplicates,
        the entries are merged under their casefolded version. Original language codes are preserved
        if no case-insensitive duplicates are found.

        :param mls_dict: Dictionary with language codes as keys and sets of strings as values.
        :return: A dictionary with merged entries for case-insensitive duplicates, preserving original case otherwise.
        """

        Validator.validate_type_iterable(mls_dict, dict, str)
        for key in mls_dict:
            Validator.validate_type_iterable(mls_dict[key], set, str)

        # Step 1: Identify case-insensitive duplicates and prepare for merging
        duplicates = {}
        for lang in mls_dict:
            lang_cf = lang.casefold()
            if lang_cf in duplicates:
                duplicates[lang_cf].append(lang)
            else:
                duplicates[lang_cf] = [lang]

        # Step 2: Merge entries with case-insensitive duplication or preserve unique entries
        merged_dict = {}
        for lang_cf, langs in duplicates.items():
            merged_texts = set()
            for lang in langs:
                merged_texts.update(mls_dict[lang])  # Merge texts from all case variants
            # Use the casefolded version if there are duplicates, else preserve original casing
            if len(langs) > 1:
                merged_dict[lang_cf] = merged_texts
            else:
                merged_dict[langs[0]] = merged_texts  # Preserve original case for unique entries

        return merged_dict
