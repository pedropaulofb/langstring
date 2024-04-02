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

    @Validator.validate_type_decorator
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
    def from_strings_to_multilangstring(cls, arg: list[str]) -> MultiLangString:
        Validator.validate_type_iterable(arg, list, str)
        new_mls = MultiLangString()

        for element in arg:
            new_mls.add_langstring(cls.from_string_to_langstring(element))

        return new_mls

    # ---------------------------------------------
    # LangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_type_decorator
    @staticmethod
    def from_langstring_to_string(arg: LangString) -> str:
        return arg.__str__()

    @staticmethod
    def from_langstrings_to_strings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_type_decorator
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
        Validator.validate_type_iterable(arg, list, LangString)
        new_texts = set()
        new_lang = set()

        for langstring in arg:
            new_texts.add(langstring.text)
            new_lang.add(langstring.lang)

        if len(new_lang) > 1:
            raise ValueError("The conversion can only be performed from LangStrings with the same language.")

        final_lang = "" if not len(new_lang) else new_lang.pop()

        return SetLangString(texts=new_texts, lang=final_lang)

    @staticmethod
    def from_langstrings_to_setlangstrings(arg: list[LangString]) -> list[SetLangString]:
        Validator.validate_type_iterable(arg, list, LangString)

        # Step 1: Detect case variants
        original_langs = {langstring.lang for langstring in arg}
        casefolded_langs = {langstring.lang.casefold() for langstring in arg}
        normalize_langs = len(original_langs) != len(casefolded_langs)

        lang_groups = {}

        for langstring in arg:
            lang_key = langstring.lang.casefold() if normalize_langs else langstring.lang

            if lang_key not in lang_groups:
                lang_groups[lang_key] = set()
            lang_groups[lang_key].add(langstring.text)

        set_langstrings = []
        for lang, texts in lang_groups.items():
            # Decide on the language code to use in the output based on normalization
            final_lang = (
                lang
                if not normalize_langs
                else [original_lang for original_lang in original_langs if original_lang.casefold() == lang][0]
            )
            set_langstrings.append(SetLangString(texts=texts, lang=final_lang))

        return set_langstrings

    @Validator.validate_type_decorator
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
        Validator.validate_type_iterable(arg, list, LangString)
        new_mls = MultiLangString()

        for langstring in arg:
            new_mls.add_langstring(langstring)

        return new_mls

    # ---------------------------------------------
    # SetLangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_type_decorator
    @staticmethod
    def from_setlangstring_to_string(arg: SetLangString) -> str:
        return arg.__str__()

    @Validator.validate_type_decorator
    @staticmethod
    def from_setlangstring_to_strings(
        arg: SetLangString, print_quotes: bool = True, separator: str = "@", print_lang: bool = True
    ) -> list[str]:
        return arg.to_strings(print_quotes=print_quotes, separator=separator, print_lang=print_lang)

    @Validator.validate_type_decorator
    @staticmethod
    def from_setlangstrings_to_strings(arg):
        # TODO: To be implemented.
        pass

    @Validator.validate_type_decorator
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
    def from_setlangstrings_to_langstrings(arg: list[SetLangString]) -> list[LangString]:
        Validator.validate_type_iterable(arg, list, SetLangString)
        langstrings = []
        for setlangstring in arg:
            langstrings.extend(setlangstring.to_langstrings())
        return langstrings

    @Validator.validate_type_decorator
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
        new_mls = MultiLangString()
        new_mls.add_setlangstring(arg)
        return new_mls

    @staticmethod
    def from_setlangstrings_to_multilangstring(arg: list[SetLangString]) -> MultiLangString:
        """Convert a list of SetLangString objects to a MultiLangString object.

        If there are different casings for the same lang tag among the SetLangString objects in the input list,
        the casefolded version of the lang tag is used. If only a single case is used, that case is adopted.

        :param setlangstrings: List of SetLangString instances to be converted.
        :return: A MultiLangString instance with aggregated texts under normalized language tags.
        """
        Validator.validate_type_iterable(arg, list, SetLangString)
        lang_tags = {}
        for sls in arg:
            lang = sls.lang
            # Collect all variants of language tags
            if lang.lower() not in lang_tags:
                lang_tags[lang.lower()] = set()
            lang_tags[lang.lower()].add(lang)

        # Determine final lang tag casing
        final_lang_tags = {}
        for lang_lower, variants in lang_tags.items():
            if len(variants) > 1:
                # Multiple casings found, use casefolded version
                final_lang_tags[lang_lower] = lang_lower
            else:
                # Single casing, use as is
                final_lang_tags[lang_lower] = variants.pop()

        # Aggregate texts under the determined language tags
        aggregated_texts = {final_lang: set() for final_lang in final_lang_tags.values()}
        for sls in arg:
            normalized_lang = final_lang_tags[sls.lang.lower()]
            aggregated_texts[normalized_lang].update(sls.texts)

        # Create and return the MultiLangString object
        return MultiLangString(mls_dict=aggregated_texts)

    # ---------------------------------------------
    # MultiLangStrings' Conversion Methods
    # ---------------------------------------------

    @Validator.validate_type_decorator
    @staticmethod
    def from_multilangstring_to_string(arg: MultiLangString) -> str:
        return arg.__str__()

    @Validator.validate_type_decorator
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
        Validator.validate_type_single(arg, MultiLangString)
        Validator.validate_type_iterable(languages, list, str, optional=True)
        return arg.to_langstrings(langs=languages)

    @staticmethod
    def from_multilangstrings_to_langstrings(
        arg: list[MultiLangString], languages: Optional[list[str]] = None
    ) -> list[LangString]:
        # TODO: Add type validation.
        langstrings = []

        for multilangstring in arg:
            langstrings.extend(multilangstring.to_langstrings(languages))

        return langstrings

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
        Validator.validate_type_single(arg, MultiLangString)
        Validator.validate_type_iterable(languages, list, str, optional=True)
        return arg.to_setlangstrings(langs=languages)

    @staticmethod
    def from_multilangstrings_to_setlangstrings(
        arg: list[MultiLangString], languages: Optional[list[str]] = None
    ) -> list[SetLangString]:
        Validator.validate_type_iterable(arg, list, MultiLangString)
        Validator.validate_type_iterable(languages, list, str, optional=True)
        setlangstrings = []

        for multilangstring in arg:
            setlangstrings.extend(multilangstring.to_setlangstrings(languages))

        return setlangstrings
