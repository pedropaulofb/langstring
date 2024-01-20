from typing import Optional, Iterator
from typing import Union

from .flags import SetLangStringFlag
from .langstring import LangString
from .utils.validator import Validator
from langstring import Controller


class SetLangString:
    def __init__(self, texts: Optional[set[str]] = None, lang: str = "") -> None:
        self.texts: set[str] = texts if (texts is not None) else set()
        self.lang: str = lang

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

    def add(self, new_element: Union[str, LangString]) -> None:
        if isinstance(new_element, str):
            self.add_text(new_element)
        elif isinstance(new_element, LangString):
            self.add_langstring(new_element)
        else:
            raise TypeError(f"Invalid type. Expected 'str' or 'LangString', got '{type(new_element).__name__}'.")

    def add_text(self, text: str) -> None:
        self.texts.add(Validator.validate_text(SetLangStringFlag, text))

    def add_langstring(self, langstring: LangString) -> None:
        self._check_language_compatibility(langstring, True)
        self.texts.add(Validator.validate_text(SetLangStringFlag, langstring.text))

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

    def discard_text(self, text: str) -> None:
        self.texts.discard(text)

    def discard_langstring(self, langstring: LangString) -> None:
        self._check_language_compatibility(langstring, True)
        self.texts.discard(langstring.text)

    def pop(self) -> str:
        return self.texts.pop()

    def remove(self, element: Union[str, LangString]) -> None:
        if isinstance(element, str):
            self.remove_text(element)
        elif isinstance(element, LangString):
            self.remove_langstring(element)
        else:
            raise TypeError(f"Invalid type. Expected 'str' or 'LangString', got '{type(element).__name__}'.")

    def remove_text(self, text: str) -> None:
        self.texts.remove(text)

    def remove_langstring(self, langstring: LangString) -> None:
        self._check_language_compatibility(langstring, True)
        self.texts.remove(langstring.text)

    def __str__(self) -> str:
        """Define the string representation of the LangString object.

        :return: The string representation of the LangString object.
        :rtype: str
        """
        print_with_lang = Controller.get_flag(SetLangStringFlag.PRINT_WITH_LANG)

        lang_representation = f"@{self.lang}" if print_with_lang else ""

        return str(self.texts) + lang_representation

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetLangString):
            return NotImplemented
        return self.texts == other.texts and self.lang.casefold() == other.lang.casefold()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, SetLangString):
            return NotImplemented
        return self.texts != other.texts or self.lang.casefold() != other.lang.casefold()

    def __hash__(self) -> int:
        """Generate a hash for a SetLangString object."""
        # Convert the set to a frozenset for hashing, as sets mutable and, hence, unhashable.
        return hash((frozenset(self.texts), self.lang.casefold()))

    # Dunder methods for set-like behavior
    def __len__(self) -> int:
        return len(self.texts)

    def __contains__(self, element: Union[str, LangString]) -> bool:
        if isinstance(element, str):
            return element in self.texts

        if isinstance(element, LangString):
            if self.lang.casefold() == element.lang.casefold():
                return element.text in self.texts
            raise ValueError("Operation can only be performed on 'str' or 'LangString' with same language.")
        raise TypeError(f"Invalid operation. Expected type 'str' or 'LangString', got {type(element).__name__}.")

    def __iter__(self) -> Iterator[str]:
        return iter(self.texts)

    def difference(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        difference_texts = self.texts.difference(*others_texts)
        return SetLangString(texts=difference_texts, lang=self.lang)

    def difference_update(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        self.texts.difference_update(*others_texts)

    def isdisjoint(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts.isdisjoint(other_texts)

    def issubset(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts.issubset(other_texts)

    def issuperset(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts.issuperset(other_texts)

    def intersection(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        intersection_texts = self.texts.intersection(*others_texts)
        return SetLangString(texts=intersection_texts, lang=self.lang)

    def intersection_update(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        self.texts.intersection_update(*others_texts)

    def symmetric_difference(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        other_texts = self._extract_texts(other)
        self._check_language_compatibility(other, strict)
        sym_diff_texts = self.texts.symmetric_difference(other_texts)
        return SetLangString(texts=sym_diff_texts, lang=self.lang)

    def symmetric_difference_update(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> None:
        other_texts = self._extract_texts(other)
        self._check_language_compatibility(other, strict)
        self.texts.symmetric_difference_update(other_texts)

    def union(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        union_texts = self.texts.union(*others_texts)
        return SetLangString(texts=union_texts, lang=self.lang)

    def update(self, *others: Union[set[str], "SetLangString"], strict: bool = False) -> None:
        others_texts = [self._extract_texts(other) for other in others]
        for other in others:
            self._check_language_compatibility(other, strict)
        self.texts.update(*others_texts)

    def __and__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        return self.intersection(other, strict=strict)

    def __iand__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        self.intersection_update(other, strict=strict)
        return self

    def __or__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        return self.union(other, strict=strict)

    def __ior__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        self.update(other, strict=strict)
        return self

    def __sub__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        return self.difference(other, strict=strict)

    def __isub__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        self.difference_update(other, strict=strict)
        return self

    def __xor__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        return self.symmetric_difference(other, strict=strict)

    def __ixor__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> "SetLangString":
        self.symmetric_difference_update(other, strict=strict)
        return self

    def __le__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        """Check if self is a subset of other."""
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts <= other_texts

    def __lt__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        """Check if self is a proper subset of other."""
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts < other_texts

    def __ge__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        """Check if self is a superset of other."""
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts >= other_texts

    def __gt__(self, other: Union[set[str], "SetLangString"], strict: bool = False) -> bool:
        """Check if self is a proper superset of other."""
        self._check_language_compatibility(other, strict)
        other_texts = self._extract_texts(other)
        return self.texts > other_texts

    def __repr__(self) -> str:
        """Return the official string representation of the SetLangString object."""
        texts_repr = repr(self.texts)
        return f"SetLangString(texts={texts_repr}, lang='{self.lang}')"

    def _check_language_compatibility(self, other: Union[set, "SetLangString", "LangString"], strict: bool) -> None:
        if strict and not isinstance(other, (SetLangString, LangString)):
            raise TypeError("Strict mode is enabled. Operand must be of type SetLangString or LangString.")
        if isinstance(other, SetLangString) and self.lang.casefold() != other.lang.casefold():
            raise ValueError("Operation cannot be performed. Incompatible languages between SetLangString objects.")
        elif isinstance(other, LangString) and self.lang.casefold() != other.lang.casefold():
            raise ValueError(
                "Operation cannot be performed. Incompatible languages between SetLangString and LangString."
            )

    def _extract_texts(self, other: Union[set[str], "SetLangString"]) -> set[str]:
        return other.texts if isinstance(other, SetLangString) else other
