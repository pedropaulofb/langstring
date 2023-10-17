from langcodes import tag_is_valid, Language
from loguru import logger


class LangString:
    def __init__(self, text: str, lang: Language = None):

        if lang and not tag_is_valid(lang):
            logger.warning(f"Invalid language tag '{lang}' used.")

        self.text: str = text
        self.lang: Language = lang

    def toString(self) -> str:
        if self.lang is None:
            return f'"{self.text}"'
        else:
            return f'"{self.text}"@{self.lang}'

    def __str__(self) -> str:
        self.toString(self)
