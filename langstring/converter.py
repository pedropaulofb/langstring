"""This module provides a Converter class for converting between different string types used in language processing.

The Converter class is designed as a utility class to facilitate the conversion between `LangString`, `SetLangString`,
and `MultiLangString` objects. These objects represent different ways of handling language-tagged strings, which are
common in applications dealing with multilingual data. The class methods in Converter allow for seamless and efficient
transformation of these string types, ensuring compatibility and ease of use in various language processing tasks.

Classes:
    Converter: Provides methods for converting between `LangString`, `SetLangString`, and `MultiLangString`.

Usage:
    The Converter class is used as a utility and should not be instantiated. Instead, its class methods are called
    directly to perform conversions. For example, `Converter.to_langstring(arg_obj)` where `arg_obj` could
    be an instance of `SetLangString` or `MultiLangString`.

Note:
    The module is designed with the assumption that the arg objects are well-formed instances of their respective
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
    # Strings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_string_to_langstring(arg_string: str, ignore_at_sign: bool = False) -> LangString:
        """Convert a string into a LangString.

        If the string contains '@', it splits the string into text (left part) and lang (right part).
        If there is no '@', the entire string is set as text and lang is set to an empty string.

        :param arg_string: The arg string to be converted.
        :return: A LangString
        """
        if "@" in arg_string and not ignore_at_sign:
            parts = arg_string.rsplit("@", 1)
            text, lang = parts[0], parts[1]
        else:
            text, lang = arg_string, ""

        return LangString(text, lang)

    @staticmethod
    def from_strings_to_langstrings(arg: Union[set[str], list[str]], lang: str) -> list[LangString]:
        if not (isinstance(arg, set) or isinstance(arg, list)):
            raise TypeError(
                f"Argument '{arg}' must be of types 'set[str]' or 'list[str]', but got '{type(arg).__name__}'."
            )

        output = []
        for text in arg:
            output.append(LangString(text=text, lang=lang))
        return output

    @staticmethod
    def from_string_to_setlangstring(arg):
        # TODO: To be implemented.
        pass

    @staticmethod
    def from_strings_to_setlangstrings(arg):
        # TODO: To be implemented.
        pass

    @staticmethod
    def from_strings_to_setlangstring(arg: Union[set[str], list[str]], lang: str) -> SetLangString:
        if not arg:
            raise ValueError("Cannot convert the empty arg to a SetLangString.")
        if not (isinstance(arg, set) or isinstance(arg, list)):
            raise TypeError(
                f"Argument '{arg}' must be of types 'set[str]' or 'list[str]' but got '{type(arg).__name__}'."
            )
        texts = set()

        for text in arg:
            if not isinstance(text, str):
                raise TypeError(
                    f"Invalid element type inside arg argument. Expected 'str', got '{type(text).__name__}'."
                )
            texts.add(text)

        return SetLangString(texts=texts, lang=lang)

    @staticmethod
    def from_string_to_multilangstring(arg):
        # TODO: To be implemented.
        pass

    @classmethod
    def from_strings_to_multilangstring(cls, arg: Union[set[str], list[str]]) -> MultiLangString:
        if not (isinstance(arg, set) or isinstance(arg, list)):
            raise TypeError(
                f"Invalid arg argument type. Expected 'list[str]' or 'set[str]', got '{type(arg).__name__}'."
            )
        new_mls = MultiLangString()

        for element in arg:
            new_mls.add_langstring(cls.from_string_to_langstring(element))

        return new_mls

    # ---------------------------------------------
    # LangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_simple_type
    @staticmethod
    def from_langstring_to_string(arg: LangString) -> str:
        return arg.__str__()

    @staticmethod
    def from_langstrings_to_strings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_langstring_to_setlangstring(arg: LangString) -> SetLangString:
        """
        Convert a LangString to a SetLangString.

        This method creates a SetLangString from a LangString. The resulting SetLangString contains the text of the
        LangString in a set and retains its language.

        :param arg: The LangString to be converted.
        :type arg: LangString
        :return: A SetLangString containing the text from the arg LangString.
        :rtype: SetLangString
        :raises TypeError: If the arg is not of type LangString.
        """
        return SetLangString(texts={arg.text}, lang=arg.lang)

    @staticmethod
    def from_langstrings_to_setlangstring(arg: list[LangString]) -> SetLangString:
        if not isinstance(arg, list):
            raise TypeError(f"Invalid 'arg' argument type. Expected 'list', got '{type(arg).__name__}'.")
        if not arg:
            raise ValueError("Cannot convert an empty list to a SetLangString.")

        new_texts = set()
        new_lang = set()

        for langstring in arg:
            if not isinstance(langstring, LangString):
                raise TypeError(
                    f"Invalid element type inside arg argument. "
                    f"Expected 'LangString', got '{type(langstring).__name__}'."
                )
            new_texts.add(langstring.text)
            new_lang.add(langstring.lang)

        if len(new_lang) > 1:
            raise ValueError("The conversion can only be performed from LangStrings with the same language.")

        return SetLangString(texts=new_texts, lang=new_lang.pop())

    @staticmethod
    def from_langstrings_to_setlangstrings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_langstring_to_multilangstring(arg: LangString) -> MultiLangString:
        """Convert a LangString to a MultiLangString.

        This method takes a single LangString and converts it into a MultiLangString. The resulting MultiLangString
        contains the text and language of the arg LangString.

        :param arg: The LangString to be converted.
        :type arg: LangString
        :return: A MultiLangString containing the text and language from the arg LangString.
        :rtype: MultiLangString
        :raises TypeError: If the arg is not of type LangString.
        """
        new_mls_dict: dict[str, set[str]] = {arg.lang: {arg.text}}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=arg.lang)

    @staticmethod
    def from_langstrings_to_multilangstring(arg: list[LangString]) -> MultiLangString:
        if arg and not isinstance(arg, list):
            raise TypeError(f"Invalid 'arg' argument type. Expected 'list', got '{type(arg).__name__}'.")

        new_mls = MultiLangString()

        for langstring in arg:
            new_mls.add_langstring(langstring)

        return new_mls

    # ---------------------------------------------
    # SetLangStrings' Conversion Methods
    # ---------------------------------------------

    @staticmethod
    def from_setlangstring_to_string(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_setlangstring_to_strings(
        arg: SetLangString, print_quotes: bool = True, separator: str = "@", print_lang: bool = True
    ) -> list[str]:
        return arg.to_strings(print_quotes=print_quotes, separator=separator, print_lang=print_lang)


    @staticmethod
    def from_setlangstrings_to_strings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_setlangstring_to_langstrings(arg: SetLangString) -> list[LangString]:
        """Convert a SetLangString to a list of LangStrings.

        This method takes a SetLangString and converts it into a list of LangStrings, each containing one of the texts
        from the SetLangString and its associated language.

        :param arg: The SetLangString to be converted.
        :type arg: SetLangString
        :return: A list of LangStrings, each corresponding to a text in the arg SetLangString.
        :rtype: list[LangString]
        :raises TypeError: If the arg is not of type SetLangString.
        """
        return arg.to_langstrings()

    @staticmethod
    def from_setlangstrings_to_langstrings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_setlangstring_to_multilangstring(arg: SetLangString) -> MultiLangString:
        """Convert a SetLangString to a MultiLangString.

        This method creates a MultiLangString from a SetLangString. The resulting MultiLangString contains all texts
        from the SetLangString, associated with its language.

        :param arg: The SetLangString to be converted.
        :type arg: SetLangString
        :return: A MultiLangString containing all texts from the arg SetLangString.
        :rtype: MultiLangString
        :raises TypeError: If the arg is not of type SetLangString.
        """
        new_mls_dict: dict[str, set[str]] = {arg.lang: arg.texts}
        return MultiLangString(mls_dict=new_mls_dict, pref_lang=arg.lang)

    @staticmethod
    def from_setlangstrings_to_multilangstring(arg: list[SetLangString]) -> MultiLangString:
        new_mls = MultiLangString()

        for setlangstring in arg:
            new_mls.add_setlangstring(setlangstring)

        return new_mls



    # ---------------------------------------------
    # MultiLangStrings' Conversion Methods
    # ---------------------------------------------


    @staticmethod
    def from_multilangstring_to_string(arg):
        # TODO: To be implemented.
        pass


    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_strings(
        arg: MultiLangString,
        languages: Optional[list[str]] = None,
        print_quotes: bool = True,
        separator: str = "@",
        print_lang: bool = True,
    ) -> list[str]:
        return arg.to_strings(
            languages=languages, print_quotes=print_quotes, separator=separator, print_lang=print_lang
        )

    @staticmethod
    def from_multilangstrings_to_strings(arg):
        # TODO: To be implemented.
        pass


    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_langstrings(
        arg: MultiLangString, languages: Optional[list[str]] = None
    ) -> list[LangString]:
        """Convert a MultiLangString to a list of LangStrings.

        This method takes a MultiLangString and converts it into a list of LangStrings, each representing one of the
        texts in the MultiLangString along with its associated language.

        :param arg: The MultiLangString to be converted.
        :type arg: MultiLangString
        :return: A list of LangStrings, each corresponding to a text in the arg MultiLangString.
        :rtype: list[LangString]
        :raises TypeError: If the arg is not of type MultiLangString.
        """
        return arg.to_langstrings(langs=languages)

    @staticmethod
    def from_multilangstrings_to_langstrings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_simple_type
    @staticmethod
    def from_multilangstring_to_setlangstrings(
        arg: MultiLangString, languages: Optional[list[str]] = None
    ) -> list[SetLangString]:
        """Convert a MultiLangString to a list of SetLangStrings.

        This method creates a list of SetLangStrings from a MultiLangString. Each SetLangString in the list contains
        texts of a single language from the MultiLangString.

        :param arg: The MultiLangString to be converted.
        :type arg: MultiLangString
        :return: A list of SetLangStrings, each containing texts of a single language from the arg MultiLangString.
        :rtype: list[SetLangString]
        :raises TypeError: If the arg is not of type MultiLangString.
        """
        return arg.to_setlangstrings(langs=languages)

    @staticmethod
    def from_multilangstrings_to_setlangstrings(arg):
        # TODO: To be implemented.
        pass
