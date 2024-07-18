"""
The setlangstring module provides the SetLangString class to encapsulate a set of strings with a common language tag.

This module is designed to work with sets of text strings and their associated language tags, offering functionalities
such as validation of language tags, handling of empty strings and language tags based on control flags. It optionally
utilizes the langcodes library for validating language tags, enhancing the robustness of the language tag validation
process.

Control flags from the controller module are used to enforce certain behaviors like ensuring non-empty text and valid
language tags. These flags can be set externally to alter the behavior of the SetLangString class.

The SetLangString class aims to make user interaction as similar as possible to working with regular sets. To achieve
this, many of the standard set methods have been overridden to return SetLangString objects, allowing seamless
integration and extended functionality. Additionally, the class provides mechanisms for validating input types,
matching language tags, and merging SetLangString objects.

:Example:

    # Create a SetLangString object
    set_lang_str = SetLangString({"Hello", "World"}, "en")

    # Print the set representation
    print(set_lang_str)  # Output: {'Hello', 'World'}@en

    # Add a new string
    set_lang_str.add("New String")
    print(set_lang_str)  # Output: {'Hello', 'New String', 'World'}@en

    # Remove a string
    set_lang_str.remove("World")
    print(set_lang_str)  # Output: {'Hello', 'New String'}@en

    # Check if a string is in the set
    contains_hello = "Hello" in set_lang_str
    print(contains_hello)  # Output: True

Modules:
    controller: Provides control flags that influence the behavior of the SetLangString class.
    flags: Defines the SetLangStringFlag class with various control flags for the SetLangString class.
    langstring: Provides the LangString class used within the SetLangString class.
    utils.validator: Provides validation methods used within the SetLangString class.
"""


from typing import Iterator
from typing import Optional
from typing import Union

from .controller import Controller
from .flags import SetLangStringFlag
from .langstring import LangString
from .utils.validator import Validator


class SetLangString:
    """
    A class to encapsulate a set of strings with a common language tag.

    This class provides functionality to associate a set of text strings with a single language tag, offering methods
    for set representation, element addition, removal, and various set operations. The behavior of this class is
    influenced by control flags from the Controller class, which can enforce non-empty text, valid language tags,
    and other constraints.

    Many standard set methods are overridden to return SetLangString objects, allowing seamless integration and
    extended functionality. This design ensures that users can work with SetLangString instances similarly to
    regular sets.

    :ivar texts: The set of text strings.
    :vartype texts: set[str]
    :ivar lang: The language tag for the set of texts.
    :vartype lang: str
    :raises ValueError: If control flags enforce non-empty text and any text in the set is empty.
    :raises TypeError: If the types of parameters are incorrect based on validation.
    """
    def __init__(self, texts: Optional[Union[set[str], list[str]]] = None, lang: str = "") -> None:
        """
        Initialize a new SetLangString object with a set of texts and an optional language tag.

        The behavior of this method is influenced by control flags set in the Controller. For instance, if the
        DEFINED_TEXT flag is enabled, any empty string within 'texts' will raise a ValueError.

        :param texts: The set of text strings or a list of text strings.
        :type texts: Optional[Union[set[str], list[str]]]
        :param lang: The language tag for the set of texts.
        :type lang: str
        :raises ValueError: If the DEFINED_TEXT flag is enabled and any text string is empty.
        :raises TypeError: If the provided texts are not a set or list of strings, or if the lang is not a string.
        """
        self.texts: Union[set[str], list[str]] = texts if texts is not None else set()
        self.lang: str = lang

    # -------------------------------------------
    # Getters and Setters
    # -------------------------------------------

    @property
    def texts(self) -> set[str]:
        """
        Get the set of text strings.

        :return: The set of text strings.
        :rtype: set[str]
        """
        return self._texts

    @texts.setter
    def texts(self, new_texts: Optional[Union[set[str], list[str]]]) -> None:
        """
        Set the set of text strings. If the provided texts are None, it defaults to an empty set.
        This method also validates the type and the texts based on control flags.

        :param new_texts: The new set of text strings or a list of text strings.
        :type new_texts: Optional[Union[set[str], list[str]]]
        :raises TypeError: If the new texts are not a set or list of strings.
        :raises ValueError: If the control flags enforce non-empty text and any text string is empty.
        """
        new_texts = set() if new_texts is None else new_texts

        if isinstance(new_texts, list):
            Validator.validate_type_iterable(new_texts, list, str)
            new_texts = set(new_texts)

        Validator.validate_type_iterable(new_texts, set, str)

        self._texts = set()

        for text_value in new_texts:
            self._texts.add(Validator.validate_flags_text(SetLangStringFlag, text_value))

    @property
    def lang(self) -> str:
        """
        Get the language tag.

        :return: The language tag.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, new_lang: str) -> None:
        """
        Set the language tag. If the provided language tag is None, it defaults to an empty string. This method also
        validates the type and the language tag based on control flags.

        :param new_lang: The new language tag.
        :type new_lang: str
        :raises TypeError: If the new language tag is not of type str.
        :raises ValueError: If the control flags enforce valid language tags and the new language tag is invalid.
        """
        new_lang = "" if new_lang is None else new_lang
        Validator.validate_type_single(new_lang, str)
        self._lang = Validator.validate_flags_lang(SetLangStringFlag, new_lang)

    # -------------------------------------------
    # SetLangString's Regular Methods
    # -------------------------------------------

    @Validator.validate_type_decorator
    def add_langstring(self, langstring: LangString) -> None:
        """
        Add a LangString object to the set of texts.

        This method validates the type and language of the LangString object and adds its text to the set.
        The behavior is influenced by control flags set in the Controller.

        :param langstring: The LangString object to add.
        :type langstring: LangString
        :raises TypeError: If the provided langstring is not of type LangString.
        :raises ValueError: If the control flags enforce valid language tags and the langstring's language tag is
                            invalid, or if the language tag of the langstring does not match the set's language tag.

        :Example:

        >>> set_lang_str = SetLangString({"Hello"}, "en")
        >>> lang_str = LangString("World", "en")
        >>> set_lang_str.add_langstring(lang_str)
        >>> print(set_lang_str)  # Output: {'Hello', 'World'}@en
        """
        self._validate_match_types_and_langs(langstring, True)
        self.texts.add(Validator.validate_flags_text(SetLangStringFlag, langstring.text))

    @Validator.validate_type_decorator
    def add_text(self, text: str) -> None:
        """
        Add a text string to the set of texts.

        This method validates the type of the text string and adds it to the set.
        The behavior is influenced by control flags set in the Controller.

        :param text: The text string to add.
        :type text: str
        :raises TypeError: If the provided text is not of type str.
        :raises ValueError: If the control flags enforce non-empty text and the text string is empty.

        :Example:

        >>> set_lang_str = SetLangString({"Hello"}, "en")
        >>> set_lang_str.add_text("World")
        >>> print(set_lang_str)  # Output: {'Hello', 'World'}@en
        """
        self.texts.add(Validator.validate_flags_text(SetLangStringFlag, text))

    @Validator.validate_type_decorator
    def discard_text(self, text: str) -> None:
        """
        Discard a text string from the set of texts.

        This method removes the text string from the set if it is present. If the text string is not present,
        the set remains unchanged. The method does not raise an error if the text is not found.

        :param text: The text string to discard.
        :type text: str
        :raises TypeError: If the provided text is not of type str.

        :Example:

        >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
        >>> set_lang_str.discard_text("World")
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        >>> set_lang_str.discard_text("Python")
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        """
        self.texts.discard(text)

    @Validator.validate_type_decorator
    def discard_langstring(self, langstring: LangString) -> None:
        """
        Discard a LangString object from the set of texts.

        This method validates the type and language of the LangString object and removes its text from the set if it
        is present. If the text is not present, the set remains unchanged. The method does not raise an error if the
        text is not found.

        :param langstring: The LangString object to discard.
        :type langstring: LangString
        :raises TypeError: If the provided langstring is not of type LangString.
        :raises ValueError: If the language tag of the langstring does not match the set's language tag.

        :Example:

        >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
        >>> lang_str = LangString("World", "en")
        >>> set_lang_str.discard_langstring(lang_str)
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        >>> lang_str = LangString("Python", "en")
        >>> set_lang_str.discard_langstring(lang_str)
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        """
        self._validate_match_types_and_langs(langstring, True)
        self.texts.discard(langstring.text)

    @Validator.validate_type_decorator
    def remove_langstring(self, langstring: LangString) -> None:
        """
        Remove a text string from the set of texts.

        This method removes the text string from the set. If the text string is not present, a KeyError is raised.

        :param text: The text string to remove.
        :type text: str
        :raises TypeError: If the provided text is not of type str.
        :raises KeyError: If the text string is not found in the set.

        :Example:

        >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
        >>> set_lang_str.remove_text("World")
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        >>> set_lang_str.remove_text("Python")  # Raises KeyError
        """
        self._validate_match_types_and_langs(langstring, True)
        self.texts.remove(langstring.text)

    @Validator.validate_type_decorator
    def remove_text(self, text: str) -> None:
        """
        Remove a LangString object from the set of texts.

        This method validates the type and language of the LangString object and removes its text from the set. If the
        text is not present, a KeyError is raised.

        :param langstring: The LangString object to remove.
        :type langstring: LangString
        :raises TypeError: If the provided langstring is not of type LangString.
        :raises ValueError: If the language tag of the langstring does not match the set's language tag.
        :raises KeyError: If the text string is not found in the set.

        :Example:

        >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
        >>> lang_str = LangString("World", "en")
        >>> set_lang_str.remove_langstring(lang_str)
        >>> print(set_lang_str)  # Output: {'Hello'}@en
        >>> lang_str = LangString("Python", "en")
        >>> set_lang_str.remove_langstring(lang_str)  # Raises KeyError
        """
        self.texts.remove(text)

    @Validator.validate_type_decorator
    def to_langstrings(self) -> list[LangString]:
        langstrings = []
        for text in self.texts:
            langstrings.append(LangString(text=text, lang=self.lang))
        return langstrings

    @Validator.validate_type_decorator
    def to_strings(
        self, print_quotes: Optional[bool] = None, separator: str = "@", print_lang: Optional[bool] = None
    ) -> list[str]:
        if print_quotes is None:
            print_quotes = Controller.get_flag(SetLangStringFlag.PRINT_WITH_QUOTES)
        if print_lang is None:
            print_lang = Controller.get_flag(SetLangStringFlag.PRINT_WITH_LANG)

        strings = []

        for text in self.texts:
            new_text = f'"{text}"' if print_quotes else text
            new_lang = f"{separator}{self.lang}" if print_lang else ""
            strings.append(f"{new_text}{new_lang}")

        return sorted(strings)

    # -------------------------------------------
    # Overwritten Set's Built-in Regular Methods
    # -------------------------------------------

    def add(self, new_element: Union[str, LangString]) -> None:
        if isinstance(new_element, str):
            self.add_text(new_element)
        elif isinstance(new_element, LangString):
            self.add_langstring(new_element)
        else:
            raise TypeError(f"Invalid type. Expected 'str' or 'LangString', got '{type(new_element).__name__}'.")

    def clear(self) -> None:
        self.texts.clear()

    def copy(self) -> "SetLangString":
        return SetLangString(texts=self.texts.copy(), lang=self.lang)

    def discard(self, element: Union[str, LangString]) -> None:
        if isinstance(element, str):
            self.discard_text(element)
        elif isinstance(element, LangString):
            self.discard_langstring(element)
        else:
            raise TypeError(f"Invalid type. Expected 'str' or 'LangString', got '{type(element).__name__}'.")

    def pop(self) -> str:
        return self.texts.pop()

    def remove(self, element: Union[str, LangString]) -> None:
        if isinstance(element, str):
            self.remove_text(element)
        elif isinstance(element, LangString):
            self.remove_langstring(element)
        else:
            raise TypeError(f"Invalid type. Expected 'str' or 'LangString', got '{type(element).__name__}'.")

    def difference(self, *others: Union[set[str], "SetLangString"]) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        difference_texts = self.texts.difference(*others_texts)
        return SetLangString(texts=difference_texts, lang=self.lang)

    def difference_update(self, *others: Union[set[str], "SetLangString"]) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        self.texts.difference_update(*others_texts)

    def isdisjoint(self, other: Union[set[str], "SetLangString"]) -> bool:
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts.isdisjoint(other_texts)

    def issubset(self, other: Union[set[str], "SetLangString"]) -> bool:
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts.issubset(other_texts)

    def issuperset(self, other: Union[set[str], "SetLangString"]) -> bool:
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts.issuperset(other_texts)

    def intersection(self, *others: Union[set[str], "SetLangString"]) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        intersection_texts = self.texts.intersection(*others_texts)
        return SetLangString(texts=intersection_texts, lang=self.lang)

    def intersection_update(self, *others: Union[set[str], "SetLangString"]) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        self.texts.intersection_update(*others_texts)

    def symmetric_difference(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        other_texts = self._extract_texts(other)
        self._validate_match_types_and_langs(other)
        sym_diff_texts = self.texts.symmetric_difference(other_texts)
        return SetLangString(texts=sym_diff_texts, lang=self.lang)

    def symmetric_difference_update(self, other: Union[set[str], "SetLangString"]) -> None:
        other_texts = self._extract_texts(other)
        self._validate_match_types_and_langs(other)
        self.texts.symmetric_difference_update(other_texts)

    def union(self, *others: Union[set[str], "SetLangString"]) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        union_texts = self.texts.union(*others_texts)
        return SetLangString(texts=union_texts, lang=self.lang)

    def update(self, *others: Union[set[str], "SetLangString"]) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._validate_match_types_and_langs(other)
        self.texts.update(*others_texts)

    # -------------------------------------------
    # Overwritten Set's Built-in Dunder Methods
    # -------------------------------------------

    def __and__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.intersection(other)

    @Validator.validate_type_decorator
    def __contains__(self, element: Union[str, LangString]) -> bool:
        # Check language compatibility
        self._validate_match_types_and_langs(element)

        # If element is a string, check if it's in the texts
        if isinstance(element, str):
            return element in self.texts

        # If element is a LangString, check if its text is in the texts
        if isinstance(element, LangString):
            return element.text in self.texts

        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetLangString):
            return NotImplemented

        return self.texts == other.texts and self.lang.casefold() == other.lang.casefold()

    def __ge__(self, other: Union[set[str], "SetLangString"]) -> bool:
        """Check if self is a superset of another."""
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts >= other_texts

    def __gt__(self, other: Union[set[str], "SetLangString"]) -> bool:
        """Check if self is a proper superset of other."""
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts > other_texts

    def __hash__(self) -> int:
        """Generate a hash for a SetLangString object."""
        # Convert the set to a frozenset for hashing, as sets are mutable and, hence, unhashable.
        return hash((frozenset(self.texts), self.lang.casefold()))

    def __iand__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        self.intersection_update(other)
        return self

    def __ior__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        self.update(other)
        return self

    def __isub__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        self.difference_update(other)
        return self

    def __iter__(self) -> Iterator[str]:
        return iter(self.texts)

    def __ixor__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        self.symmetric_difference_update(other)
        return self

    def __le__(self, other: Union[set[str], "SetLangString"]) -> bool:
        """Check if self is a subset of other."""
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts <= other_texts

    def __len__(self) -> int:
        return len(self.texts)

    def __lt__(self, other: Union[set[str], "SetLangString"]) -> bool:
        """Check if self is a proper subset of other."""
        self._validate_match_types_and_langs(other)
        other_texts = self._extract_texts(other)
        return self.texts < other_texts

    def __or__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.union(other)

    def __repr__(self) -> str:
        """Return the official string representation of the SetLangString object."""
        return f"{self.__class__.__name__}(texts={repr(self.texts)}, lang={repr(self.lang)})"

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        This method provides a concise string representation of the LangString, listing each text entry with its
        associated language tag if the corresponding flags are set.

        :return: The string representation of the LangString object.
        :rtype: str
        """
        if not self.texts:
            texts_str = "{}"
        else:
            # The texts are sorted to ensure deterministic output.
            sorted_texts = sorted(self.texts)
            if Controller.get_flag(SetLangStringFlag.PRINT_WITH_QUOTES):
                texts_str = "{" + ", ".join(f"'{text}'" for text in sorted_texts) + "}"
            else:
                texts_str = "{" + ", ".join(f"{text}" for text in sorted_texts) + "}"

        if Controller.get_flag(SetLangStringFlag.PRINT_WITH_LANG):
            lang_representation = f"@{self.lang}" if self.lang else ""
            return f"{texts_str}{lang_representation}"

        return texts_str

    def __sub__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.difference(other)

    def __xor__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.symmetric_difference(other)

    # -------------------------------------------
    # Static Methods
    # -------------------------------------------

    @staticmethod
    def merge_setlangstrings(setlangstrings: list["SetLangString"]) -> list["SetLangString"]:
        """
        Merges duplicated SetLangStrings based on their language tags using the union method.

        If there's no case variation in the language tags among duplicates, the original casing is preserved.
        If case variations are found, the casefolded version of the language tag is used in the merged SetLangString.

        :param setlangstrings: The list of SetLangString instances.
        :return: A list of merged SetLangString instances without duplicates.
        """
        Validator.validate_type_iterable(setlangstrings, list, SetLangString)
        merged: dict[str, SetLangString] = {}
        lang_case_map: dict[str, str] = {}
        for setlangstring in setlangstrings:
            key = setlangstring.lang.casefold()
            if key in merged:
                merged[key] = merged[key].union(setlangstring)
                # If encountering a different casing, standardize to casefold.
                if setlangstring.lang != lang_case_map[key]:
                    lang_case_map[key] = key
            else:
                merged[key] = setlangstring
                lang_case_map[key] = setlangstring.lang  # Keep track of the original casing

        # Adjust the language tags based on detected case variations
        for key, setlangstring in merged.items():
            setlangstring.lang = lang_case_map[key]

        return list(merged.values())

    # -------------------------------------------
    # Private Methods
    # -------------------------------------------

    def _validate_match_types_and_langs(
        self, other: Union[str, set[str], "SetLangString", "LangString"], overwrite_strict: bool = False
    ) -> None:
        strict = (
            Controller.get_flag(SetLangStringFlag.METHODS_MATCH_TYPES) if not overwrite_strict else overwrite_strict
        )

        # If strict mode is enabled, only allow SetLangString or LangString types
        if strict and not isinstance(other, (SetLangString, LangString)):
            raise TypeError("Strict mode is enabled. Operand must be of type SetLangString or LangString.")

        # Check language compatibility for LangString and SetLangString types
        if isinstance(other, (LangString, SetLangString)) and self.lang.casefold() != other.lang.casefold():
            raise ValueError(
                f"Operation cannot be performed. "
                f"Incompatible languages between SetLangString and {type(other).__name__} object."
            )

    def _extract_texts(self, other: Union[set[str], "SetLangString"]) -> set[str]:
        return other.texts if isinstance(other, SetLangString) else other
