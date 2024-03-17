from typing import Iterator
from typing import Optional
from typing import Union

from .controller import Controller
from .flags import SetLangStringFlag
from .langstring import LangString
from .utils.validator import Validator


class SetLangString:
    def __init__(self, texts: Optional[set[str]] = None, lang: str = "") -> None:
        self.texts: set[str] = texts if (texts is not None) else set()
        self.lang: str = lang

    # -------------------------------------------
    # Getters and Setters
    # -------------------------------------------

    @property
    def texts(self) -> set[str]:
        """Getter for texts."""
        return self._texts

    @texts.setter
    def texts(self, new_texts: set[str]) -> None:
        """Setter for texts."""
        msg = f"Invalid 'texts' value received ('{new_texts}')."
        if not isinstance(new_texts, set):
            raise TypeError(f"{msg}'). Expected 'set', got '{type(new_texts).__name__}'.")

        self._texts = set()
        for text_value in new_texts:
            self._texts.add(Validator.validate_text(SetLangStringFlag, text_value))

    @property
    def lang(self) -> str:
        """Getter for lang."""
        return self._lang

    @lang.setter
    def lang(self, new_lang: str) -> None:
        """Setter for lang."""
        self._lang = Validator.validate_lang(SetLangStringFlag, new_lang)

    # -------------------------------------------
    # SetLangString's Regular Methods
    # -------------------------------------------

    @Validator.validate_simple_type
    def add_langstring(self, langstring: LangString) -> None:
        self._validate_match_types_and_langs(langstring, True)
        self.texts.add(Validator.validate_text(SetLangStringFlag, langstring.text))

    @Validator.validate_simple_type
    def add_text(self, text: str) -> None:
        self.texts.add(Validator.validate_text(SetLangStringFlag, text))

    @Validator.validate_simple_type
    def discard_text(self, text: str) -> None:
        self.texts.discard(text)

    @Validator.validate_simple_type
    def discard_langstring(self, langstring: LangString) -> None:
        self._validate_match_types_and_langs(langstring, True)
        self.texts.discard(langstring.text)

    # TODO: Analyze creation of setlangstring add/discard/remove setlangstring
    # TODO: Analyze creation of contains methods (similar to MLSs)

    @Validator.validate_simple_type
    def remove_langstring(self, langstring: LangString) -> None:
        self._validate_match_types_and_langs(langstring, True)
        self.texts.remove(langstring.text)

    @Validator.validate_simple_type
    def remove_text(self, text: str) -> None:
        self.texts.remove(text)

    @Validator.validate_simple_type
    def to_langstrings(self) -> list[LangString]:
        langstrings = []
        for text in self.texts:
            langstrings.append(LangString(text=text, lang=self.lang))
        return langstrings

    @Validator.validate_simple_type
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

    @Validator.validate_simple_type
    def __contains__(self, element: Union[str, LangString]) -> bool:
        # Check language compatibility
        self._validate_match_types_and_langs(element)

        # If element is a string, check if it's in the texts
        if isinstance(element, str):
            return element in self.texts

        # If element is a LangString, check if its text is in the texts
        if isinstance(element, LangString):
            return element.text in self.texts

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

        :return: The string representation of the LangString object.
        :rtype: str
        """
        texts_str = "{}" if not self.texts else str(self.texts)

        if Controller.get_flag(SetLangStringFlag.PRINT_WITH_LANG):
            lang_representation = f"@{self.lang}" if self.lang else "@"
            return f"{texts_str}{lang_representation}"

        return texts_str

    def __sub__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.difference(other)

    def __xor__(self, other: Union[set[str], "SetLangString"]) -> "SetLangString":
        return self.symmetric_difference(other)

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
