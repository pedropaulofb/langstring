from typing import Union

from .langstring import LangString
from .multilangstring import MultiLangString
from .setlangstring import SetLangString
from .utils.controls_base import NonInstantiable


class Converter(metaclass=NonInstantiable):
    @classmethod
    def convert_to_langstring(cls, input: Union[SetLangString, MultiLangString]) -> list[LangString]:
        if isinstance(input, SetLangString):
            return cls.convert_setlangstring_to_langstrings(input)

        if isinstance(input, MultiLangString):
            return cls.convert_multilangstring_to_langstrings(input)

        raise TypeError(
            f"Invalid input argument type. " f"Expected SetLangString or MultiLangString, got {type(input).__name__}."
        )

    @classmethod
    def convert_to_setlangstring(
        cls, input: Union[LangString, MultiLangString]
    ) -> Union[SetLangString, list[SetLangString]]:
        if isinstance(input, LangString):
            return cls.convert_langstring_to_setlangstring(input)

        if isinstance(input, MultiLangString):
            return cls.convert_multilangstring_to_setlangstrings(input)

        raise TypeError(
            f"Invalid input argument type. Expected LangString or MultiLangString, got {type(input).__name__}."
        )

    @classmethod
    def convert_to_multilangstring(cls, input: Union[LangString, SetLangString]) -> MultiLangString:
        if isinstance(input, LangString):
            return cls.convert_langstring_to_multilangstring(input)

        if isinstance(input, SetLangString):
            return cls.convert_setlangstring_to_multilangstring(input)

        raise TypeError(
            f"Invalid input argument type. Expected LangString or SetLangString, got {type(input).__name__}."
        )

    @classmethod
    def convert_langstring_to_multilangstring(cls, input: LangString) -> MultiLangString:
        if not isinstance(input, LangString):
            raise TypeError(f"Invalid input argument type. Expected LangString, got {type(input).__name__}.")

        new_mls_dict: dict[str, set[str]] = {input.lang: {input.text}}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    @classmethod
    def convert_langstring_to_setlangstring(cls, input: LangString) -> SetLangString:
        if not isinstance(input, LangString):
            raise TypeError(f"Invalid input argument type. Expected LangString, got {type(input).__name__}.")

        return SetLangString(texts={input.text}, lang=input.lang)

    @classmethod
    def convert_setlangstring_to_langstrings(cls, input: SetLangString) -> list[LangString]:
        if not isinstance(input, SetLangString):
            raise TypeError(f"Invalid input argument type. Expected SetLangString, got {type(input).__name__}.")

        return_list = []

        for text in input.texts:
            return_list.append(LangString(text=text, lang=input.lang))

        return return_list

    @classmethod
    def convert_setlangstring_to_multilangstring(cls, input: SetLangString) -> MultiLangString:
        if not isinstance(input, SetLangString):
            raise TypeError(f"Invalid input argument type. Expected SetLangString, got {type(input).__name__}.")

        new_mls_dict: dict[str, set[str]] = {input.lang: input.texts}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    @classmethod
    def convert_multilangstring_to_langstrings(cls, input: MultiLangString) -> list[LangString]:
        if not isinstance(input, MultiLangString):
            raise TypeError(f"Invalid input argument type. Expected MultiLangString, got {type(input).__name__}.")

        return [LangString(text, lang) for lang, texts in input.mls_dict.items() for text in texts]

    @classmethod
    def convert_multilangstring_to_setlangstrings(cls, input: MultiLangString) -> list[SetLangString]:
        if not isinstance(input, MultiLangString):
            raise TypeError(f"Invalid input argument type. Expected MultiLangString, got {type(input).__name__}.")

        return_list = []

        for lang in input.mls_dict.keys():
            return_list.append(SetLangString(texts=input.mls_dict[lang], lang=lang))

        return return_list
