from typing import Optional
from typing import Union

from .flags import SetLangStringFlag
from .langstring import LangString
from .utils.validator import Validator
from langstring import Controller


# TODO: In all methods I am using the direct access (_text, _lang) instead of the setters (text, lang). Is it ok?


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
        self._texts.add(Validator.validate_text(SetLangStringFlag, text))

    def add_langstring(self, langstring: LangString):
        if (self.lang).casefold() != (langstring.lang).casefold():
            raise ValueError(
                f"Impossible to perform addition. "
                f"LangString (lang='{langstring.lang.casefold()}') and SetLangString (lang='{self.lang.casefold()}') "
                f"languages do not match."
            )

        self._texts.add(Validator.validate_text(SetLangStringFlag, langstring.text))

    def clear(self) -> None:
        self._texts.clear()

    def discard(self, text: str) -> None:
        self._texts.discard(text)

    def remove(self, text: str) -> None:
        self._texts.remove(text)

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

    def __hash__(self) -> int:
        """Generate a hash for a SetLangString object."""
        # Convert the set to a frozenset for hashing, as sets mutable and, hence, unhashable.
        return hash((frozenset(self.texts), self.lang.casefold()))
