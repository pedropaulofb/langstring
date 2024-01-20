"""This module provides a Converter class for converting between different string types used in language processing.

The Converter class is designed as a utility class to facilitate the conversion between `LangString`, `SetLangString`,
and `MultiLangString` objects. These objects represent different ways of handling language-tagged strings, which are
common in applications dealing with multilingual data. The class methods in Converter allow for seamless and efficient
transformation of these string types, ensuring compatibility and ease of use in various language processing tasks.

Classes:
    Converter: Provides methods for converting between `LangString`, `SetLangString`, and `MultiLangString`.

Usage:
    The Converter class is used as a utility and should not be instantiated. Instead, its class methods are called
    directly to perform conversions. For example, `Converter.to_langstring(input_obj)` where `input_obj` could
    be an instance of `SetLangString` or `MultiLangString`.

Note:
    The module is designed with the assumption that the input objects are well-formed instances of their respective
    classes. Error handling is provided for type mismatches, but not for malformed objects.

This module is part of a larger package dealing with language processing and RDF data manipulation, providing
foundational tools for handling multilingual text data in various formats.
"""
from typing import Union

from .langstring import LangString
from .multilangstring import MultiLangString
from .setlangstring import SetLangString
from .utils.non_instantiable import NonInstantiable


class Converter(metaclass=NonInstantiable):
    """A utility class for converting between different string types used in language processing.

    This class provides methods to convert between `LangString`, `SetLangString`, and `MultiLangString` types.
    It is designed to be non-instantiable as it serves as a utility class with class methods only.
    """

    @classmethod
    def to_langstring(cls, input: Union[str, SetLangString, MultiLangString]) -> Union[LangString, list[LangString]]:
        """Convert a SetLangString or MultiLangString to a list of LangStrings.

        :param input: The SetLangString or MultiLangString to be converted.
        :type input: Union[SetLangString, MultiLangString]
        :return: A list of LangStrings.
        :rtype: list[LangString]
        :raises TypeError: If the input is not of type SetLangString or MultiLangString.
        """

        if isinstance(input, str):
            return cls.from_string_to_langstring(input)

        if isinstance(input, SetLangString):
            return cls.from_setlangstring_to_langstrings(input)

        if isinstance(input, MultiLangString):
            return cls.from_multilangstring_to_langstrings(input)

        raise TypeError(
            f"Invalid input argument type. Expected str, SetLangString or MultiLangString, got '{type(input).__name__}'."
        )

    @classmethod
    def to_setlangstring(cls, input: Union[LangString, MultiLangString]) -> Union[SetLangString, list[SetLangString]]:
        """Convert a LangString or MultiLangString to a SetLangString or a list of SetLangStrings.

        :param input: The LangString or MultiLangString to be converted.
        :type input: Union[LangString, MultiLangString]
        :return: A SetLangString or a list of SetLangStrings.
        :rtype: Union[SetLangString, list[SetLangString]]
        :raises TypeError: If the input is not of type LangString or MultiLangString.
        """
        if isinstance(input, LangString):
            return cls.from_langstring_to_setlangstring(input)

        if isinstance(input, MultiLangString):
            return cls.from_multilangstring_to_setlangstrings(input)

        raise TypeError(
            f"Invalid input argument type. Expected LangString or MultiLangString, got '{type(input).__name__}'."
        )

    @classmethod
    def to_multilangstring(cls, input: Union[set[str], list[str], LangString, SetLangString]) -> MultiLangString:
        """Convert a LangString or SetLangString to a MultiLangString.

        :param input: The LangString or SetLangString to be converted.
        :type input: Union[LangString, SetLangString]
        :return: A MultiLangString.
        :rtype: MultiLangString
        :raises TypeError: If the input is not of type LangString or SetLangString.
        """

        if isinstance(input, set) or isinstance(input, list):
            return cls.from_strings_to_multilangstring(input)

        if isinstance(input, LangString):
            return cls.from_langstring_to_multilangstring(input)

        if isinstance(input, SetLangString):
            return cls.from_setlangstring_to_multilangstring(input)

        raise TypeError(
            f"Invalid input argument type. Expected str, LangString or SetLangString, got '{type(input).__name__}'."
        )

    @staticmethod
    def from_langstring_to_setlangstring(input: LangString) -> SetLangString:
        """
        Convert a LangString to a SetLangString.

        This method creates a SetLangString from a LangString. The resulting SetLangString contains the text of the
        LangString in a set and retains its language.

        :param input: The LangString to be converted.
        :type input: LangString
        :return: A SetLangString containing the text from the input LangString.
        :rtype: SetLangString
        :raises TypeError: If the input is not of type LangString.
        """
        if not isinstance(input, LangString):
            raise TypeError(f"Invalid input argument type. Expected LangString, got '{type(input).__name__}'.")

        return SetLangString(texts={input.text}, lang=input.lang)

    @staticmethod
    def from_langstring_to_multilangstring(input: LangString) -> MultiLangString:
        """Convert a LangString to a MultiLangString.

        This method takes a single LangString and converts it into a MultiLangString. The resulting MultiLangString
        contains the text and language of the input LangString.

        :param input: The LangString to be converted.
        :type input: LangString
        :return: A MultiLangString containing the text and language from the input LangString.
        :rtype: MultiLangString
        :raises TypeError: If the input is not of type LangString.
        """
        if not isinstance(input, LangString):
            raise TypeError(f"Invalid input argument type. Expected LangString, got '{type(input).__name__}'.")

        new_mls_dict: dict[str, set[str]] = {input.lang: {input.text}}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    @staticmethod
    def from_setlangstring_to_langstrings(input: SetLangString) -> list[LangString]:
        """Convert a SetLangString to a list of LangStrings.

        This method takes a SetLangString and converts it into a list of LangStrings, each containing one of the texts
        from the SetLangString and its associated language.

        :param input: The SetLangString to be converted.
        :type input: SetLangString
        :return: A list of LangStrings, each corresponding to a text in the input SetLangString.
        :rtype: list[LangString]
        :raises TypeError: If the input is not of type SetLangString.
        """
        if not isinstance(input, SetLangString):
            raise TypeError(f"Invalid input argument type. Expected SetLangString, got '{type(input).__name__}'.")

        return_list = []

        for text in input.texts:
            return_list.append(LangString(text=text, lang=input.lang))

        return return_list

    @staticmethod
    def from_setlangstring_to_multilangstring(input: SetLangString) -> MultiLangString:
        """Convert a SetLangString to a MultiLangString.

        This method creates a MultiLangString from a SetLangString. The resulting MultiLangString contains all texts
        from the SetLangString, associated with its language.

        :param input: The SetLangString to be converted.
        :type input: SetLangString
        :return: A MultiLangString containing all texts from the input SetLangString.
        :rtype: MultiLangString
        :raises TypeError: If the input is not of type SetLangString.
        """
        if not isinstance(input, SetLangString):
            raise TypeError(f"Invalid input argument type. Expected SetLangString, got '{type(input).__name__}'.")

        new_mls_dict: dict[str, set[str]] = {input.lang: input.texts}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    @staticmethod
    def from_multilangstring_to_langstrings(input: MultiLangString) -> list[LangString]:
        """Convert a MultiLangString to a list of LangStrings.

        This method takes a MultiLangString and converts it into a list of LangStrings, each representing one of the
        texts in the MultiLangString along with its associated language.

        :param input: The MultiLangString to be converted.
        :type input: MultiLangString
        :return: A list of LangStrings, each corresponding to a text in the input MultiLangString.
        :rtype: list[LangString]
        :raises TypeError: If the input is not of type MultiLangString.
        """
        if not isinstance(input, MultiLangString):
            raise TypeError(f"Invalid input argument type. Expected MultiLangString, got '{type(input).__name__}'.")

        return [LangString(text, lang) for lang, texts in input.mls_dict.items() for text in texts]

    @staticmethod
    def from_multilangstring_to_setlangstrings(input: MultiLangString) -> list[SetLangString]:
        """Convert a MultiLangString to a list of SetLangStrings.

        This method creates a list of SetLangStrings from a MultiLangString. Each SetLangString in the list contains
        texts of a single language from the MultiLangString.

        :param input: The MultiLangString to be converted.
        :type input: MultiLangString
        :return: A list of SetLangStrings, each containing texts of a single language from the input MultiLangString.
        :rtype: list[SetLangString]
        :raises TypeError: If the input is not of type MultiLangString.
        """
        if not isinstance(input, MultiLangString):
            raise TypeError(f"Invalid input argument type. Expected MultiLangString, got '{type(input).__name__}'.")

        return_list = []

        for lang in input.mls_dict.keys():
            return_list.append(SetLangString(texts=input.mls_dict[lang], lang=lang))

        return return_list

    @staticmethod
    def from_string_to_langstring(input_string: str) -> LangString:
        """Convert a string into a LangString.

        If the string contains '@', it splits the string into text (left part) and lang (right part).
        If there is no '@', the entire string is set as text and lang is set to an empty string.

        :param input_string: The input string to be converted.
        :return: A LangString
        """
        if not isinstance(input, str):
            raise TypeError(f"Invalid input argument type. Expected 'str', got '{type(input).__name__}'.")

        if "@" in input_string:
            parts = input_string.rsplit("@", 1)
            text, lang = parts[0], parts[1]
        else:
            text, lang = input_string, ""

        return LangString(text, lang)

    @classmethod
    def from_strings_to_multilangstring(cls, input: Union[set[str], list[str]]) -> MultiLangString:
        if not (isinstance(input, set) or isinstance(input, list)):
            raise TypeError(
                f"Invalid input argument type. Expected 'list[str]' or 'set[str]', got '{type(input).__name__}'."
            )
        new_mls = MultiLangString()

        for element in input:
            new_mls.add_langstring(cls.from_string_to_langstring(element))

        return new_mls
