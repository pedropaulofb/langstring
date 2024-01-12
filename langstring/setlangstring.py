from .utils.validation_base import ValidationBase


class SetLangString(ValidationBase):
    def __init__(self, texts: set[str], lang: str) -> None:
        if texts and not isinstance(texts, set):
            raise TypeError(f"Invalid type of argument texts. Expected 'set', got '{type(lang).__name__}'.")
        if lang and not isinstance(lang, str):
            raise TypeError(f"Invalid type of argument lang. Expected 'str', got '{type(lang).__name__}'.")
        if not lang:
            raise ValueError("Language not defined. SetLangStrings are expected to have an associated language.")

        self.texts = texts
        self.lang = lang

    def __eq__(self, other):
        if not isinstance(other, SetLangString):
            return NotImplemented
        return self.texts == other.texts and self.lang == other.lang
