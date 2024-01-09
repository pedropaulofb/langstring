from .utils.validation_base import ValidationBase


class SetLangString(ValidationBase):
    def __init__(self, texts: set[str], lang: str) -> None:
        if not isinstance(texts, set):
            raise TypeError(f"Invalid type of argument texts. Expected 'set', got '{type(lang).__name__}'.")
        if not isinstance(lang, str):
            raise TypeError(f"Invalid type of argument lang. Expected 'str', got '{type(lang).__name__}'.")

        self.texts = texts
        self.lang = lang
