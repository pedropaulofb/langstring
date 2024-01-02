from typing import Union

from .langstring import LangString
from .multilangstring import MultiLangString
from .setlangstring import SetLangString
from .utils.controls_base import NonInstantiable


class Converter(metaclass=NonInstantiable):
    @classmethod
    def convert_to_langstring(cls, input:Union[SetLangString, MultiLangString]):
        if not (isinstance(input, SetLangString) or isinstance(input, MultiLangString)):
            raise TypeError(f"Invalid input argument type. "
                            f"Expected SetLangString or MultiLangString, got {type(input).__name__}.")

    @classmethod
    def convert_to_setlangstring(cls, input:Union[LangString, MultiLangString]):
        if not (isinstance(input, LangString) or isinstance(input, MultiLangString)):
            raise TypeError(f"Invalid input argument type. "
                            f"Expected LangString or MultiLangString, got {type(input).__name__}.")

    @classmethod
    def convert_to_multilangstring(cls, input:Union[LangString, SetLangString]):
        if not (isinstance(input, LangString) or isinstance(input, SetLangString)):
            raise TypeError(f"Invalid input argument type. "
                            f"Expected LangString or SetLangString, got {type(input).__name__}.")

    @classmethod
    def convert_langstring_to_multilangstring(cls, input: LangString):
        pass

    @classmethod
    def convert_langstring_to_setlangstring(cls, input: LangString) -> SetLangString:
        pass

    @classmethod
    def convert_setlangstring_to_langstrings(cls, input) -> list[LangString]:
        pass

    @classmethod
    def convert_setlangstring_to_multilangstring(cls, input) -> MultiLangString:
        pass

    @classmethod
    def convert_multilangstring_to_langstrings(cls, input)->list[LangString]:
        pass

    @classmethod
    def convert_multilangstring_to_setlangstrings(cls, input)->list[SetLangString]:
        pass
