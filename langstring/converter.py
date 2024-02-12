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

from typing import Optional
from typing import Union

from .langstring import LangString
from .multilangstring import MultiLangString
from .setlangstring import SetLangString
from .utils.non_instantiable import NonInstantiable
from .utils.validator import Validator


class Converter(metaclass=NonInstantiable):
    """A utility class for converting between different string types used in language processing.

    This class provides methods to convert between `LangString`, `SetLangString`, and `MultiLangString` types.
    It is designed to be non-instantiable as it serves as a utility class with class methods only.
    """

    # ---------------------------------------------
    # General Conversion Methods
    # ---------------------------------------------

    @classmethod
    def to_string(cls, input: Union[LangString, SetLangString, MultiLangString]) -> str:
        if isinstance(input, LangString):
            return cls.from_langstring_to_string(input)

        if isinstance(input, SetLangString):
            return cls.from_setlangstring_to_string(input)

        if isinstance(input, MultiLangString):
            return cls.from_multilangstring_to_string(input)

        raise TypeError(
            f"Invalid input argument type. Expected LangString, SetLangString or MultiLangString, "
            f"got '{type(input).__name__}'."
        )

    @classmethod
    def to_strings(cls, input: Union[SetLangString, MultiLangString]) -> list[str]:
        if isinstance(input, SetLangString):
            return cls.from_setlangstring_to_strings(input)

        if isinstance(input, MultiLangString):
            return cls.from_multilangstring_to_strings(input)

        raise TypeError(
            f"Invalid input argument type. Expected SetLangString or MultiLangString, got '{type(input).__name__}'."
        )

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
            f"Invalid input argument type. Expected str, SetLangString or MultiLangString, "
            f"got '{type(input).__name__}'."
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

    # ---------------------------------------------
    # Strings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_string_to_langstring(input_string: str, ignore_at_sign: bool = False) -> LangString:
        """Convert a string into a LangString.

        If the string contains '@', it splits the string into text (left part) and lang (right part).
        If there is no '@', the entire string is set as text and lang is set to an empty string.

        :param input_string: The input string to be converted.
        :return: A LangString
        """
        if "@" in input_string and not ignore_at_sign:
            parts = input_string.rsplit("@", 1)
            text, lang = parts[0], parts[1]
        else:
            text, lang = input_string, ""

        return LangString(text, lang)

    @staticmethod
    def from_strings_to_langstrings(input: Union[set[str], list[str]], lang: str) -> list[LangString]:
        if not (isinstance(input, set) or isinstance(input, list)):
            raise TypeError(
                f"Argument '{input}' must be of types 'set[str]' or 'list[str]', " f"but got '{type(input).__name__}'."
            )

        output = []
        for text in input:
            output.append(LangString(text=text, lang=lang))
        return output

    @staticmethod
    def from_strings_to_setlangstring(input: Union[set[str], list[str]], lang: str) -> SetLangString:
        if not input:
            raise ValueError("Cannot convert the empty input to a SetLangString.")
        if not (isinstance(input, set) or isinstance(input, list)):
            raise TypeError(
                f"Argument '{input}' must be of types 'set[str]' or 'list[str]' but got '{type(input).__name__}'."
            )
        texts = set()

        for text in input:
            if not isinstance(text, str):
                raise TypeError(
                    f"Invalid element type inside input argument. " f"Expected 'str', got '{type(text).__name__}'."
                )
            texts.add(text)

        return SetLangString(texts=texts, lang=lang)

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

    # ---------------------------------------------
    # LangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_langstring_to_string(input: LangString) -> str:
        return input.__str__()

    @Validator.validate_simple_type
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
        return SetLangString(texts={input.text}, lang=input.lang)

    @staticmethod
    def from_langstrings_to_setlangstring(input: list[LangString]) -> SetLangString:
        if not isinstance(input, list):
            raise TypeError(f"Invalid input argument type. Expected 'list', got '{type(input).__name__}'.")
        if not input:
            raise ValueError("Cannot convert an empty list to a SetLangString.")

        new_texts = set()
        new_lang = set()

        for langstring in input:
            if not isinstance(langstring, LangString):
                raise TypeError(
                    f"Invalid element type inside input argument. "
                    f"Expected 'LangString', got '{type(langstring).__name__}'."
                )
            new_texts.add(langstring.text)
            new_lang.add(langstring.lang)

        if len(new_lang) > 1:
            raise ValueError("The conversion can only be performed from LangStrings with the same language.")

        return SetLangString(texts=new_texts, lang=new_lang.pop())

    @Validator.validate_simple_type
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
        new_mls_dict: dict[str, set[str]] = {input.lang: {input.text}}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    @Validator.validate_simple_type
    @staticmethod
    def from_langstrings_to_multilangstring(input: LangString) -> SetLangString:
        # TODO: TO BE IMPLEMENTED
        pass

    # ---------------------------------------------
    # SetLangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_setlangstring_to_string(input: SetLangString) -> str:
        return input.__str__()

    @Validator.validate_simple_type
    @staticmethod
    def from_setlangstring_to_strings(
        input: SetLangString, print_quotes: bool = True, separator: str = "@", print_lang: bool = True
    ) -> list[str]:
        return input.to_strings(print_quotes=print_quotes, separator=separator, print_lang=print_lang)

    @Validator.validate_simple_type
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
        return input.to_langstrings()

    @Validator.validate_simple_type
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
        new_mls_dict: dict[str, set[str]] = {input.lang: input.texts}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=input.lang)

    def from_setlangstrings_to_multilangstring(input: list[SetLangString]) -> MultiLangString:
        # TODO: To be implemented
        pass

    # ---------------------------------------------
    # MultiLangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_langstrings(
        input: MultiLangString, languages: Optional[list[str]] = None
    ) -> list[LangString]:
        """Convert a MultiLangString to a list of LangStrings.

        This method takes a MultiLangString and converts it into a list of LangStrings, each representing one of the
        texts in the MultiLangString along with its associated language.

        :param input: The MultiLangString to be converted.
        :type input: MultiLangString
        :return: A list of LangStrings, each corresponding to a text in the input MultiLangString.
        :rtype: list[LangString]
        :raises TypeError: If the input is not of type MultiLangString.
        """
        return input.to_langstrings(languages=languages)

    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_setlangstrings(
        input: MultiLangString, languages: Optional[list[str]] = None
    ) -> list[SetLangString]:
        """Convert a MultiLangString to a list of SetLangStrings.

        This method creates a list of SetLangStrings from a MultiLangString. Each SetLangString in the list contains
        texts of a single language from the MultiLangString.

        :param input: The MultiLangString to be converted.
        :type input: MultiLangString
        :return: A list of SetLangStrings, each containing texts of a single language from the input MultiLangString.
        :rtype: list[SetLangString]
        :raises TypeError: If the input is not of type MultiLangString.
        """
        return input.to_setlangstrings(languages=languages)

    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_string(input: MultiLangString) -> str:
        return input.__str__()

    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_strings(
        input: MultiLangString,
        languages: Optional[list[str]] = None,
        print_quotes: bool = True,
        separator: str = "@",
        print_lang: bool = True,
    ) -> list[str]:
        return input.to_strings(
            languages=languages, print_quotes=print_quotes, separator=separator, print_lang=print_lang
        )
