from enum import Enum

from langcodes import Language, tag_is_valid
from loguru import logger

from langstring.langstring import LangString


class ControlMultipleEntries(Enum):
    OVERWRITE = "OVERWRITE"
    ALLOW = "ALLOW"
    BLOCK_WARN = "BLOCK_WARN"
    BLOCK_ERROR = "BLOCK_ERROR"


class MultiLangString:
    def __init__(self, *args: LangString, control: str = "ALLOW", preferred_lang: Language = "en"):
        try:
            self.control = ControlMultipleEntries[control]
        except KeyError:
            raise ValueError(
                f"Invalid control value: {control}. "
                f"Valid control values are: {ControlMultipleEntries._member_names_}."
            )

        if not tag_is_valid(preferred_lang):
            logger.warning(f"Invalid preferred language tag '{preferred_lang}' used.")

        self.langstrings: dict = {}  # Initialize self.langStrings here
        self.control: ControlMultipleEntries = ControlMultipleEntries[control]
        self.preferred_lang: Language = preferred_lang

        for arg in args:
            self.add(arg)

    def add(self, lang_string: LangString):
        if isinstance(lang_string, LangString):
            if self.control == ControlMultipleEntries.BLOCK_WARN and lang_string.lang in self.langstrings:
                logger.warning(
                    f"Operation not possible, a LangString with language tag {lang_string.lang} already exists."
                )
            elif self.control == ControlMultipleEntries.BLOCK_ERROR and lang_string.lang in self.langstrings:
                raise ValueError(
                    f"Operation not possible, a LangString with language tag {lang_string.lang} already exists."
                )
            elif self.control == ControlMultipleEntries.OVERWRITE:
                self.langstrings[lang_string.lang] = [lang_string.text]
            else:  # self.control == ALLOW
                if lang_string.text not in self.langstrings.get(lang_string.lang, []):
                    self.langstrings.setdefault(lang_string.lang, []).append(lang_string.text)

    def get_lang_string(self, lang: str) -> list:
        return self.langstrings.get(lang, [])

    def get_preferred_lang_string(self) -> str:
        return self.langstrings.get(self.preferred_lang, None)

    def remove_lang_string(self, lang_string: LangString) -> bool:
        lang_strings = self.langstrings.get(lang_string.lang, [])
        if lang_string.text in lang_strings:
            lang_strings.remove(lang_string.text)
            if not lang_strings:
                del self.langstrings[lang_string.lang]
            return True
        return False

    def remove_lang(self, lang: str):
        self.langstrings.pop(lang, None)

    def to_string(self) -> str:
        return self.__str__()

    def to_string_list(self) -> list[str]:
        return [
            f"{repr(lang_string)}@{lang}"
            for lang, lang_strings in self.langstrings.items()
            for lang_string in lang_strings
        ]

    def __repr__(self):
        return f"MultiLangString({self.langstrings}, control={self.control}, preferred_lang={self.preferred_lang})"

    def __len__(self):
        return sum(len(lang_strings) for lang_strings in self.langstrings.values())

    def __str__(self) -> str:
        return ", ".join(
            f"{repr(lang_string)}@{lang}"
            for lang, lang_strings in self.langstrings.items()
            for lang_string in lang_strings
        )
