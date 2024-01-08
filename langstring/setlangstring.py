from .utils.validation_base import ValidationBase


class SetLangString(ValidationBase):
    def __init__(self, texts: set[str], lang: str):
        self.texts = texts
        self.lang = lang
