from .multilangstring import MultiLangString
from .utils.validation_base import ValidationBase


class SetLangString(ValidationBase):

    def __init__(self, texts: set[str], lang: str):
        self.texts = texts
        self.lang = lang

    def add_translations(self, source_lang: str, target_langs: list[str]):
        for mls in self._multilangstrings:
            mls.add_translations_lang(source_lang, target_langs)

    def get_multilangstrings(self) -> list[MultiLangString]:
        return self._multilangstrings


