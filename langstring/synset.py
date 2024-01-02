import nltk
from langcodes import Language

from .multilangstring import MultiLangString
from .utils.validation_base import ValidationBase
from nltk.corpus import wordnet

nltk.download("omw-1.4", quiet=True)


class SynSet(ValidationBase):
    def __init__(self, text: str, lang: str):
        self._multilangstrings: list[MultiLangString] = []
        mls = MultiLangString(pref_lang=lang)
        mls.add_entry(text,lang)
        self._multilangstrings.append(mls)
        std_lang = Language.get(lang).to_alpha3()
        synsets = wordnet.synonyms(text, lang=std_lang)

        for synset in synsets:
            if synset:
                self._multilangstrings.append(MultiLangString(mls_dict={lang: set(synset)}, pref_lang=lang))

    def add_translations(self, source_lang: str, target_langs: list[str]):
        for mls in self._multilangstrings:
            mls.add_translations_lang(source_lang, target_langs)

    def get_multilangstrings(self) -> list[MultiLangString]:
        return self._multilangstrings
