"""This module defines the `MultiLangString` class for handling multilingual text strings."""
from typing import Any
from typing import Optional

from multilangstring_control import MultiLangStringControl
from multilangstring_control import MultiLangStringFlag
from utils.validation_base import ValidationBase

from langstring import LangString


class MultiLangString(ValidationBase):
    """A class for managing multilingual text strings with various language tags.

    Utilizes a global control strategy set in MultiLangStringControl to handle duplicate language tags. Supports
    operations like adding, removing, and retrieving language strings in multiple languages.

    :ivar langstrings: A dictionary of LangStrings indexed by language tag.
    :vartype mls_dict: dict[str, list[str]]
    :ivar preferred_lang: The preferred language for this MultiLangString. Defaults to "en".
    :vartype preferred_lang: str
    """

    def _get_control_and_flags_type(self) -> tuple[type[MultiLangStringControl], type[MultiLangStringFlag]]:
        """Retrieve the control class and its corresponding flags enumeration used in the MultiLangString class.

        This method provides the specific control class (MultiLangStringControl) and the flags enumeration
        (MultiLangStringFlag) that are used for configuring and validating the MultiLangString instances.
        It is essential for the functioning of the ValidationBase methods, which rely on these control settings.

        :return: A tuple containing the MultiLangStringControl class and the MultiLangStringFlag enumeration.
        :rtype: tuple[type[MultiLangStringControl], type[MultiLangStringFlag]]
        """
        return MultiLangStringControl, MultiLangStringFlag

    def _validate_langstring_arg(self, arg: Any) -> None:
        """Private helper method to validate if the argument is a LangString.

        :param arg: Argument to be checked.
        :type arg: Any
        :raises TypeError: If the passed argument is not an instance of LangString.
        """
        if not isinstance(arg, LangString):
            raise TypeError(
                f"MultiLangString received invalid argument. Expected a LangString but "
                f"received '{type(arg).__name__}' with value '{arg}'."
            )

    def __init__(self, mls_dict: dict[str, set[str]] = None, preferred_lang: str = "en") -> None:
        if mls_dict is None:
            mls_dict = {}
        self.mls_dict: dict[str, set[str]] = mls_dict

        self._preferred_lang: str = preferred_lang

    # preferred_lang GETTER
    @property
    def preferred_lang(self) -> str:
        """Get the preferred language for this MultiLangString.

        :return: The preferred language as a string.
        """
        return self._preferred_lang

    # preferred_lang SETTER
    @preferred_lang.setter
    def preferred_lang(self, preferred_lang_value: str) -> None:
        """Set the preferred language for this MultiLangString.

        :param preferred_lang_value: The preferred language as a string.
        :type preferred_lang_value: str
        :raises TypeError: If preferred_lang_value is not a string.
        """
        if isinstance(preferred_lang_value, str):
            self._preferred_lang = preferred_lang_value
        else:
            raise TypeError(f"Invalid preferred_lang type. Should be 'str', but is '{type(preferred_lang_value)}'.")

    def add_entry(self, text: str, lang: str = "") -> None:
        self._validate_arguments()

        if lang not in self.mls_dict:
            self.mls_dict[lang] = set()
        self.mls_dict[lang].add(text)

    def add_langstring(self, langstring: LangString) -> None:
        """Add a LangString to the MultiLangString.

        Depending on the current global control strategy (e.g., ALLOW, OVERWRITE, BLOCK_WARN, BLOCK_ERROR), the behavior
        for handling duplicate language tags varies. For example, BLOCK_ERROR will prevent adding a LangString with a
        duplicate language tag. For ALLOW, it adds the LangString unless an identical one exists for the same language tag.

        :param langstring: The LangString object to be added, representing a text in a specific language.
        :type langstring: LangString
        """
        self._validate_langstring_arg(langstring)
        self.add_entry(text=langstring.text, lang=langstring.lang)

    def get_langstring(self, lang: str) -> list[str]:
        """Get LangStrings for a specific language tag.

        Returns a list of LangStrings for the specified language tag. If the specified language tag is not present
        in the MultiLangString, an empty list is returned.

        Example:
            mls = MultiLangString()
            mls.add_langstring(LangString("Hello", "en"))
            print(mls.get_langstring("en"))  # Output: ["Hello"]

        :param lang: The language tag to retrieve LangStrings for.
        :type lang: str
        :return: List of LangStrings for the specified language tag. Returns an empty list if not found.
        :rtype: list[str]
        """
        if not isinstance(lang, str):
            raise TypeError(f"Expected a string but received '{type(lang).__name__}'.")
        return self.langstrings.get(lang, [])

    def get_pref_langstring(self) -> Optional[str]:
        """Get the preferred language's LangString.

        :return: The LangString for the preferred language.
        :rtype: str
        """
        return self.langstrings.get(self.preferred_lang, None)

    def remove_langstring(self, langstring: LangString) -> bool:
        """Remove a specified LangString from the MultiLangString.

        Attempts to remove a LangString from the MultiLangString. If the LangString is found and successfully removed,
        the method returns True. If the LangString is not found, it returns False.

        :param langstring: The LangString to be removed.
        :type langstring: LangString
        :return: True if the LangString was successfully removed, False otherwise.
        :rtype: bool
        :raises TypeError: If the provided argument is not an instance of LangString.
        """
        if not isinstance(langstring, LangString):
            raise TypeError(f"Expected a LangString but received '{type(langstring).__name__}'.")

        langstrings = self.langstrings.get(langstring.lang, [])
        if langstring.text in langstrings:
            langstrings.remove(langstring.text)
            if not langstrings:
                del self.langstrings[langstring.lang]
            return True
        return False

        # Perform cleaning method

    def remove_language(self, language_code: str) -> bool:
        """Remove all LangStrings associated with a specific language code from the MultiLangString.

        Attempts to remove all LangStrings that match a given language code. Returns True if the language code is found
        and the entries are successfully removed. Returns False if the language code is not found. Raises a ValueError
        for invalid language_code formats.

        :param language_code: The language code (e.g., "en", "fr") for which to remove LangStrings.
        :type language_code: str
        :return: True if language entries were removed, False otherwise.
        :rtype: bool
        :raises TypeError: If the provided language_code is not a string or is invalid.
        :raises ValueError: If the provided language_code contains non-alphabetical characters.
        """
        # Handling of Invalid Language Formats
        if not isinstance(language_code, str):
            raise TypeError(f"Invalid language format. Expected alphabetic string and received '{language_code}'.")

        if not language_code:
            raise TypeError(
                "Invalid language format. Expected non-empty alphabetic string and received an empty string."
            )

        if not language_code.isalpha():
            raise TypeError(f"Invalid language format. Expected alphabetic string and received '{language_code}'.")

        # Ensure case insensitivity
        language_code = language_code.lower()

        # Check if the language exists
        if language_code in self.langstrings:
            del self.langstrings[language_code]
            return True

        # If language was not found
        return False

    def to_string(self) -> str:
        """Convert the MultiLangString to a string. Syntactical sugar for self.__str()__.

        :return: The string representation of the MultiLangString.
        :rtype: str
        """
        return self.__str__()

    def to_string_list(self) -> list[str]:
        """Convert the MultiLangString to a list of strings.

        :return: List of strings representing the MultiLangString.
        :rtype: list
        """
        return [
            f"{repr(langstring)}@{lang}" for lang, langstrings in self.langstrings.items() for langstring in langstrings
        ]

    def to_langstrings_all(self) -> list[LangString]:
        pass

    def to_langstrings_lang(self, lang: str) -> list[LangString]:
        pass

    def __repr__(self) -> str:
        """Return a detailed string representation of the MultiLangString object.

        This method provides a more verbose string representation of the MultiLangString, which includes the full
        dictionary of language strings and the preferred language, making it useful for debugging.

        :return: A detailed string representation of the MultiLangString.
        :rtype: str
        """
        if not isinstance(self.langstrings, dict):
            raise TypeError("mls_dict must be a dictionary.")

        return f"MultiLangString({self.langstrings}, preferred_lang='{self.preferred_lang}')"

    def __len__(self) -> int:
        """Return the total number of LangStrings stored in the MultiLangString.

        :return: The total number of LangStrings.
        :rtype: int
        """
        return sum(len(langstrings) for langstrings in self.langstrings.values())

    def __str__(self) -> str:
        """Return a string representation of the MultiLangString, including language tags.

        This method provides a concise string representation of the MultiLangString, listing each LangString with its
        associated language tag.

        Example:
            mls = MultiLangString(LangString("Hello", "en"), LangString("Hola", "es"))
            print(str(mls))  # Output: "'Hello'@en, 'Hola'@es"

        :return: A string representation of the MultiLangString with language tags.
        :rtype: str
        """
        return ", ".join(
            f"{repr(langstring)}@{lang}" for lang, langstrings in self.langstrings.items() for langstring in langstrings
        )

    def __eq__(self, other: object) -> bool:
        """Check equality of this MultiLangString with another MultiLangString.

        This method compares the 'mls_dict' attribute of the two MultiLangString objects. The comparison is based on
        the content of the MultiLangString objects, irrespective of their internal handling of duplicates and preferred language.

        :param other: Another MultiLangString object to compare with.
        :type other: MultiLangString
        :return: True if both MultiLangString objects have the same content, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, MultiLangString):
            return False
        return self.langstrings == other.langstrings

    def __hash__(self) -> int:
        """Generate a hash value for a MultiLangString object.

        The hash is computed based on the 'mls_dict' attribute of the MultiLangString. This approach ensures that
        MultiLangString objects with the same content will have the same hash value.

        :return: The hash value of the MultiLangString object.
        :rtype: int
        """
        # Creating a frozenset for the dictionary items to ensure the hash is independent of order
        langstrings_hash = hash(frozenset((lang, frozenset(texts)) for lang, texts in self.langstrings.items()))
        return hash(langstrings_hash)

    def _exist_in_mls_dict(self, text_searched: str, lang_searched: str) -> bool:
        """Check if a given text is associated with a specified language in the dictionary.

        :param text_searched: The text to search for in the dictionary.
        :type text_searched: str
        :param lang_searched: The language key to search under in the dictionary.
        :type lang_searched: str
        :return: True if the text is found under the specified language, False otherwise.
        :rtype: bool
        """
        return lang_searched in self.mls_dict and text_searched in self.mls_dict[lang_searched]
