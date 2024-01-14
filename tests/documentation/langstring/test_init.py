import pytest

from langstring import Controller
from langstring import LangString
from langstring import LangStringFlag


# This example is designed to demonstrate the practical usage of the `init` method of the LangString class.
# It serves as a guide for understanding how to initialize LangString objects in various common scenarios.


def test_langstring_init_examples():
    # Initializing with English text
    # This is a straightforward example where we create a LangString object with English text.
    # The 'en' language code stands for English.
    english_text = LangString("Hello", "en")
    assert english_text.text == "Hello"
    assert english_text.lang == "en"
    # This object can now be used in contexts where English text is required.

    # Initializing with a non-English language, Japanese in this case
    # Here, 'ja' is the language code for Japanese.
    # This example shows the class's ability to handle text in languages other than English.
    japanese_text = LangString("こんにちは", "ja")
    assert japanese_text.text == "こんにちは"
    assert japanese_text.lang == "ja"
    # This object is particularly useful for applications supporting multiple languages.

    # Handling invalid input types
    # Demonstrates the class's error handling when provided with incorrect data types.
    # In this case, passing a number instead of a string should raise a TypeError.
    with pytest.raises(TypeError):
        invalid_text = LangString(123, "en")
    # This ensures that the LangString object is always initialized with the correct data types.

    # Initialization with default values
    # When no parameters are passed, LangString initializes with empty strings for both text and language.
    # This is useful when the text and language are to be determined or set later in the program.
    default_text = LangString()
    assert default_text.text == ""
    assert default_text.lang == ""
    # This approach provides flexibility, allowing for dynamic assignment of text and language.

    # Example with a specific language variant
    # Here, 'fr-CA' stands for Canadian French, demonstrating the class's support for language variants.
    # This is important for applications that need to distinguish between different dialects or regional languages.
    canadian_french_text = LangString("Bonjour", "fr-CA")
    assert canadian_french_text.text == "Bonjour"
    assert canadian_french_text.lang == "fr-CA"
    # This object can be used in contexts where specific language variants are important, such as localization.


# This test function comprehensively covers the basic and practical usage scenarios for the LangString class's __init__ method.
# It illustrates the class's versatility in handling different languages and input types, making it suitable for a wide range of applications.


# This enhanced example includes demonstrations of how LangStringFlags affect the initialization of LangString objects.
# These flags allow for additional control over how LangStrings are created and validated.


def test_langstring_init_with_flags_examples():
    # Basic initialization without any flags
    # This is the standard behavior without any additional constraints.
    basic_text = LangString("Hello", "en")
    assert basic_text.text == "Hello"
    assert basic_text.lang == "en"

    # Enabling the STRIP_TEXT flag
    # This flag will strip any leading/trailing whitespace from the text.
    Controller.set_flag(LangStringFlag.STRIP_TEXT, True)
    stripped_text = LangString("  Hello  ", "en")
    assert stripped_text.text == "Hello"
    # Resetting the flag to its default state for subsequent tests
    Controller.set_flag(LangStringFlag.STRIP_TEXT, False)

    # Enabling the LOWERCASE_LANG flag
    # This flag converts the language code to lowercase, ensuring consistency.
    Controller.set_flag(LangStringFlag.LOWERCASE_LANG, True)
    lowercase_lang = LangString("Hello", "EN")
    assert lowercase_lang.lang == "en"
    # Resetting the flag to its default state
    Controller.set_flag(LangStringFlag.LOWERCASE_LANG, False)

    # Enforcing non-empty strings with the DEFINED_TEXT and DEFINED_LANG flags
    # These flags ensure that both text and language fields are not empty.
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, True)
    Controller.set_flag(LangStringFlag.DEFINED_LANG, True)
    with pytest.raises(ValueError):
        empty_text = LangString("", "en")
    with pytest.raises(ValueError):
        empty_lang = LangString("Hello", "")
    # Resetting the flags to their default states
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.set_flag(LangStringFlag.DEFINED_LANG, False)

    # Validating language codes with the VALID_LANG flag
    # This flag ensures that the provided language code is valid and recognized.
    Controller.set_flag(LangStringFlag.VALID_LANG, True)
    with pytest.raises(ValueError):
        invalid_lang = LangString("Hello", "invalid-code")
    # Resetting the flag to its default state
    Controller.set_flag(LangStringFlag.VALID_LANG, False)


# This test function demonstrates how different LangStringFlags can be used to modify the behavior of the LangString class's __init__ method.
# These flags add a layer of control and validation, making the LangString class more versatile and robust for various use cases.
