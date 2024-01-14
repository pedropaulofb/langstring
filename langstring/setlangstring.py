from typing import Optional
from typing import Union

from .flags import SetLangStringFlag
from .utils.validator import Validator


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

    def add_text(self, text: str) -> None:
        self._texts.add(Validator.validate_text(SetLangStringFlag, text))

    def add_texts(self, texts: Union[set[str], list[str]]) -> None:
        for text in texts:
            self._texts.add(Validator.validate_text(SetLangStringFlag, text))

    def remove_text(self, text: str) -> None:
        self._texts.remove(text)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetLangString):
            return NotImplemented
        return self.texts == other.texts and self.lang == other.lang

    def __hash__(self) -> int:
        """Generate a hash for a SetLangString object."""
        # Convert the set to a frozenset for hashing, as sets mutable and, hence, unhashable.
        return hash((frozenset(self.texts), self.lang))
