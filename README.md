[![Project DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10211480.svg)](https://doi.org/10.5281/zenodo.10211480)
[![Project Status - Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![GitHub - Release Date - PublishedAt](https://img.shields.io/github/release-date/pedropaulofb/langstring)
![GitHub - Last Commit - Branch](https://img.shields.io/github/last-commit/pedropaulofb/langstring/main)
![PyPI - Project](https://img.shields.io/pypi/v/langstring)
![PyPI - Downloads](https://img.shields.io/pypi/dm/langstring)
![Language - Top](https://img.shields.io/github/languages/top/pedropaulofb/langstring)
![Language - Version](https://img.shields.io/pypi/pyversions/langstring)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/pedropaulofb/langstring)
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/pedropaulofb/langstring/badge)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License - GitHub](https://img.shields.io/github/license/pedropaulofb/langstring)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pedropaulofb/langstring/main.svg)](https://results.pre-commit.ci/latest/github/pedropaulofb/langstring/main)
![Website](https://img.shields.io/website/http/pedropaulofb.github.io/langstring.svg)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/pedropaulofb/langstring/code_testing.yml)

# LangString Python Library

The LangString Python Library offers a powerful and intuitive way to represent strings with associated language metadata. Designed with the intent to simplify language-specific string management, this library encapsulates a string with its language information, allowing for advanced linguistic operations and clear representations.

**📦 PyPI Package:**
The library is conveniently [available as a PyPI package](https://pypi.org/project/langstring/), allowing users to easily import it into other Python projects.

**📚 Documentation:**
For inquiries and further information, please refer to the [comprehensive docstring-generated documentation](https://pedropaulofb.github.io/langstring) available for this project.

## Contents

<!-- TOC -->

* [LangString Python Library](#langstring-python-library)
    * [Contents](#contents)
    * [LangString Library](#langstring-library)
        * [Purpose and Contextualization](#purpose-and-contextualization)
        * [Key Components](#key-components)
        * [Practical Use Cases](#practical-use-cases)
        * [Related Work and Differences](#related-work-and-differences)
    * [LangStrings](#langstrings)
        * [LangStrings’ Methods](#langstrings-methods)
            * [`__init__` Method](#init-method)
            * [`to_string` Method](#tostring-method)
            * [`__str__` Method](#str-method)
            * [`__eq__` Method](#eq-method)
            * [`__hash__` Method](#hash-method)
    * [MultiLangStrings](#multilangstrings)
        * [MultiLangStrings’ Methods](#multilangstrings-methods)
            * [`__init__` Method](#init-method-1)
            * [`add_entry` Method](#addentry-method)
            * [`add_langstring` Method](#addlangstring-method)
            * [`remove_entry` Method](#removeentry-method)
            * [`remove_lang` Method](#removelang-method)
            * [`get_langstring` Method](#getlangstring-method)
            * [`get_langstrings_lang` Method](#getlangstringslang-method)
            * [`get_langstrings_all` Method](#getlangstringsall-method)
            * [`get_langstrings_pref_lang` Method](#getlangstringspreflang-method)
            * [`get_strings_lang` Method](#getstringslang-method)
            * [`get_strings_pref_lang` Method](#getstringspreflang-method)
            * [`get_strings_all` Method](#getstringsall-method)
            * [`get_strings_langstring_lang` Method](#getstringslangstringlang-method)
            * [`get_strings_langstring_pref_lang` Method](#getstringslangstringpreflang-method)
            * [`get_strings_langstring_all` Method](#getstringslangstringall-method)
            * [`len_entries_all` Method](#lenentriesall-method)
            * [`len_entries_lang` Method](#lenentrieslang-method)
            * [`len_langs` Method](#lenlangs-method)
            * [`__repr__` Method](#repr-method)
            * [`__str__` Method](#str-method-1)
            * [`__eq__` Method](#eq-method-1)
            * [`__hash__` Method](#hash-method-1)
    * [Control and Flags](#control-and-flags)
        * [Flags](#flags)
        * [Control](#control)
            * [LangString Control Examples](#langstring-control-examples)
            * [MultiLangString Control Examples](#multilangstring-control-examples)
            * [`set_flag` Method](#setflag-method)
            * [`get_flag` Method](#getflag-method)
            * [`reset_flags` Method](#resetflags-method)
            * [`print_flags` Method](#printflags-method)
    * [Code Testing](#code-testing)
    * [Version 2: Key Differences and Improvements](#version-2-key-differences-and-improvements)
    * [How to Contribute](#how-to-contribute)
        * [Reporting Issues](#reporting-issues)
        * [Code Contributions](#code-contributions)
        * [Test Contributions](#test-contributions)
        * [General Guidelines](#general-guidelines)
    * [Dependencies](#dependencies)
        * [Using Poetry](#using-poetry)
        * [Using `requirements.txt`](#using-requirementstxt)
    * [License](#license)
    * [Author](#author)

<!-- TOC -->

## LangString Library

The LangString Library emerges as a solution to the intricate challenge of handling multilingual text in software applications. In today's globalized world, where digital platforms often cater to a diverse, multilingual audience, the need for efficiently managing text in multiple languages is paramount. This library is motivated by the necessity to simplify the representation, storage, and manipulation of language-specific text data, thereby addressing a common problem in internationalized applications.

### Purpose and Contextualization

The primary purpose of the LangString Library is to provide developers with robust tools for handling text in different languages, ensuring accurate and efficient processing of multilingual content. It aims to bridge the gap between the complexities of language-specific text management and the growing demand for applications that can seamlessly operate across linguistic boundaries.

### Key Components

The library comprises two main classes, each serving distinct roles in the realm of multilingual text management:

- **LangString**: This class encapsulates a single string along with its language information. It is ideal for scenarios where individual text strings are tied to specific languages, such as user-generated content in different languages or displaying messages in a user's preferred language.

- **MultiLangString**: This class, on the other hand, is designed for handling text strings across multiple languages. It is particularly useful in applications that need to store and display the same content in several languages, like multilingual websites or global e-commerce platforms.

### Practical Use Cases

- **LangString Use Case**: In a multilingual customer support system, LangString can be used to store user queries in their original language, facilitating accurate translation and response by support staff.

- **MultiLangString Use Case**: For a global marketing campaign, MultiLangString can manage promotional content in various languages, enabling the campaign to resonate with a diverse international audience.

In essence, the LangString Library is a strategic response to the challenges of modern, multilingual application development, offering essential tools for seamless and effective language-specific text handling.

### Related Work and Differences

The LangString Library offers unique functionalities for handling multilingual text in Python applications. While there are several libraries and tools available for internationalization, localization, and language processing, they differ from the LangString Library in scope and functionality. Below is an overview of related work and how they compare to the LangString Library:

- **Babel**
    - https://pypi.org/project/Babel/
    - Babel is a Python library for internationalization and localization. It primarily focuses on formatting dates, numbers, and currency values for different locales.
    - Difference: Unlike Babel, the LangString Library specifically manages multilingual text strings, providing a more direct approach to handling language-specific text data.

- **gettext**
    - https://pypi.org/project/python-gettext/
    - gettext is a GNU system used for internationalizing applications. It allows for translating fixed strings in different languages using message catalogs.
    - Difference: The LangString Library, in contrast, is designed for dynamic management of multilingual content, not just for translation of static strings.

- **langcodes**
    - https://pypi.org/project/langcodes/
    - langcodes provides tools for parsing and understanding language tags.
    - Difference: While langcodes is useful for handling language codes, the LangString Library extends beyond this by managing actual multilingual text strings associated with these codes.

- **Polyglot**
    - https://pypi.org/project/polyglot/
    - Polyglot is a natural language pipeline that supports multiple languages for various NLP tasks.
    - Difference: Polyglot focuses on language processing rather than the structured management of multilingual text, which is the core functionality of the LangString Library.

- **CLD3**
    - https://pypi.org/project/gcld3/
    - Google's CLD3 is a model for language identification.
    - Difference: CLD3 is specialized in detecting the language of a text, whereas the LangString Library is about storing and manipulating text in multiple languages.

- **spaCy**
    - https://pypi.org/project/spacy/
    - spaCy is a comprehensive NLP library that supports multiple languages.
    - Difference: spaCy is geared towards analyzing text, not managing it. The LangString Library, on the other hand, is designed for the structured handling and storage of multilingual text.

In summary, while these related tools and libraries offer valuable functionalities for internationalization, localization, and language processing, the LangString Library stands out for its specific focus on managing and manipulating multilingual text strings in a structured and efficient manner.

### Installation and Use

Install with:

```bash
pip install langstring
```

Then, encapsulate strings with their language tags as shown in the examples above.

After installation, you can use the `LangString` and `MultiLangString` classes in your project. Simply import the classes and start encapsulating strings with their language tags.

```python
from langstring import LangString, MultiLangString, LangStringControl, LangStringFlag, MultiLangStringControl, MultiLangStringFlag
```

## LangStrings

The `LangString` class is a fundamental component of the LangString Library, designed to encapsulate a single string along with its associated language information. It is primarily used in scenarios where the language context of a text string is crucial, such as in multilingual applications, content management systems, or any software that deals with language-specific data. The class provides a structured way to manage text strings, ensuring that each piece of text is correctly associated with its respective language.

### LangStrings’ Methods

The `LangString` class offers a range of methods to efficiently handle language-specific text. These methods enable the initialization, representation, comparison, and validation of text strings in their language context.

#### `__init__` Method

**Description**:
The `__init__` method initializes a new LangString object. It accepts `text`, the string to be encapsulated, and an optional `lang` parameter, which is the language tag associated with the text. This method is essential for creating LangString instances, tying the text to its language context.

**Examples**:

- Without language

```python
greeting = LangString("Hello")
```

- With language

```python
french_greeting = LangString("Bonjour", "fr")
```

#### `to_string` Method

**Description**:
The `to_string` method converts the LangString object into a string representation, including the language tag if present. This method is useful for displaying or logging the content of a LangString object in a human-readable format.

**Examples**:

```python
greeting = LangString("Hello", "en")
print(greeting.to_string())  # Output: '"Hello"@en'
```

#### `__str__` Method

**Description**:
The `__str__` method defines how a LangString object is converted to a string, typically used when the object is printed. It returns the text string, optionally followed by the language tag.

**Examples**:

```python
greeting = LangString("Hello", "en")
print(greeting)  # Output: '"Hello"@en'
```

#### `__eq__` Method

**Description**:
The `__eq__` method checks the equality of the LangString object with another object. It compares both the text and the language tag to determine if two LangString objects are the same.

**Examples**:

```python
greeting1 = LangString("Hello", "en")
greeting2 = LangString("Hello", "en")
print(greeting1 == greeting2)  # Output: True
```

#### `__hash__` Method

**Description**:
The `__hash__` method generates a hash value for the LangString object. This is particularly useful when LangString objects need to be used in hash-based collections like sets or dictionaries.

**Examples**:

```python
greeting = LangString("Hello", "en")
print(hash(greeting))
```

## MultiLangStrings

The `MultiLangString` class is a key component of the LangString Library, designed to manage and manipulate text strings across multiple languages. This class is particularly useful in applications that require handling of text in a multilingual context, such as websites, applications with internationalization support, and data processing tools that deal with multilingual data. The primary purpose of `MultiLangString` is to store, retrieve, and manipulate text entries in various languages, offering a flexible and efficient way to handle multilingual content.

### MultiLangStrings’ Methods

The `MultiLangString` class provides a suite of methods to facilitate the management of multilingual text. These methods enable the addition, removal, retrieval, and manipulation of text entries in multiple languages, as well as setting and getting a preferred language for default text retrieval.

#### `__init__` Method

The `__init__` method initializes a new MultiLangString object. It accepts an optional dictionary (`mls_dict`) representing the internal structure of the MultiLangString, where keys are language codes and values are sets of text entries. It also accepts a `pref_lang` parameter for setting the preferred language.

**Examples**:

- Initializing with a dictionary:

```python
mls = MultiLangString({"en": {"Hello", "Good morning"}})
```

- Initializing with a preferred language

```python
mls = MultiLangString(pref_lang="en")
```

#### `add_entry` Method

The `add_entry` method adds a text entry to the MultiLangString under a specified language. It ensures that the text and language comply with the set control flags.

**Examples**:

- Adding an entry

```python
mls.add_entry("Bonjour", "fr")
```

#### `add_langstring` Method

This method adds a LangString object to the MultiLangString, allowing for the integration of LangString instances directly.

**Examples**:

- Adding a LangString

```python
mls.add_langstring(LangString("Hola", "es"))
```

#### `remove_entry` Method

The `remove_entry` method removes a specific text entry from a given language in the MultiLangString.

**Examples**:

- Removing an entry

```python
mls.remove_entry("Hello", "en")
```

#### `remove_lang` Method

This method removes all entries of a given language from the MultiLangString.

**Examples**:

- Removing a language

```python
mls.remove_lang("en")
```

#### `get_langstring` Method

The `get_langstring` method retrieves a LangString object for a specific text and language combination from the MultiLangString.

**Examples**:

- Retrieving a LangString

```python
lang_str = mls.get_langstring("Hello", "en")
```

#### `get_langstrings_lang` Method

This method retrieves a list of LangStrings for a given language from the MultiLangString.

**Examples**:

- Retrieving LangStrings for a language

```python
lang_strings = mls.get_langstrings_lang("en")
```

#### `get_langstrings_all` Method

The `get_langstrings_all` method retrieves a list of all LangStrings in the MultiLangString.

**Examples**:

- Retrieving all LangStrings

```python
all_lang_strings = mls.get_langstrings_all()
```

#### `get_langstrings_pref_lang` Method

This method retrieves a list of LangStrings for the preferred language set in the MultiLangString.

**Examples**:

- Retrieving LangStrings for the preferred language

```python
pref_lang_strings = mls.get_langstrings_pref_lang()
```

#### `get_strings_lang` Method

The `get_strings_lang` method retrieves all text entries for a specific language from the MultiLangString.

**Examples**:

- Retrieving text entries for a language

```python
texts = mls.get_strings_lang("en")
```

#### `get_strings_pref_lang` Method

This method retrieves all text entries for the preferred language in the MultiLangString.

**Examples**:

- Retrieving text entries for the preferred language

```python
pref_texts = mls.get_strings_pref_lang()
```

#### `get_strings_all` Method

The `get_strings_all` method retrieves all text entries across all languages in the MultiLangString.

**Examples**:

- Retrieving all text entries

```python
all_texts = mls.get_strings_all()
```

#### `get_strings_langstring_lang` Method

This method retrieves all text entries for a specific language, formatted as '"text"@lang', from the MultiLangString.

**Examples**:

- Retrieving formatted text entries for a language

```python
formatted_texts = mls.get_strings_langstring_lang("en")
```

#### `get_strings_langstring_pref_lang` Method

The `get_strings_langstring_pref_lang` method retrieves all text entries for the preferred language, formatted as '"text"@lang'.

**Examples**:

```python

```

- Retrieving formatted text entries for the preferred language
  formatted_pref_texts = mls.get_strings_langstring_pref_lang()

#### `get_strings_langstring_all` Method

This method retrieves all text entries across all languages, formatted as '"text"@lang', in the MultiLangString.

**Examples**:

- Retrieving all formatted text entries

```python
all_formatted_texts = mls.get_strings_langstring_all()
```

#### `len_entries_all` Method

The `len_entries_all` method calculates the total number of text entries across all languages in the MultiLangString.

**Examples**:

- Getting the total number of entries

```python
total_entries = mls.len_entries_all()
```

#### `len_entries_lang` Method

This method calculates the number of text entries for a specific language in the MultiLangString.

**Examples**:

- Getting the number of entries for a language

```python
num_entries = mls.len_entries_lang("en")
```

#### `len_langs` Method

The `len_langs` method calculates the number of distinct languages represented in the MultiLangString.

**Examples**:

- Getting the number of languages

```python
num_languages = mls.len_langs()
```

#### `__repr__` Method

The `__repr__` method returns a detailed string representation of the MultiLangString object, including the full dictionary of language strings and the preferred language.

**Examples**:

- Printing the representation

```python
print(mls.__repr__())
```

#### `__str__` Method

The `__str__` method defines the string representation of the MultiLangString, listing each text entry with its associated language tag.

**Examples**:

- Printing the MultiLangString

```python
print(mls)
```

#### `__eq__` Method

The `__eq__` method checks the equality of the MultiLangString object with another object based on the `mls_dict` attribute.

**Examples**:

- Comparing two MultiLangStrings

```python
print(mls1 == mls2)
```

#### `__hash__` Method

The `__hash__` method generates a hash value for the MultiLangString object based on its `mls_dict` attribute.

**Examples**:

- Generating a hash value

```python
print(hash(mls))
```

## Control and Flags

The Control and Flags system in the LangString Library is designed to manage and configure the behavior of LangString and MultiLangString instances. This system allows for dynamic control over various aspects of handling multilingual text, such as validation rules and representation formats.

### Flags

Flags are enumeration types that define various control options for LangString and MultiLangString instances. They are used to toggle specific behaviors on or off, providing flexibility in how instances of these classes behave in different scenarios.

### Control

The Control classes, namely LangStringControl and MultiLangStringControl, act as static managers for the flags. They provide methods to set, retrieve, and reset the states of these flags, ensuring consistent behavior across all instances of LangString and MultiLangString.

#### LangString Control Examples

- Enabling a flag:
  ```python
  LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
  ```
- Checking if a flag is enabled:
  ```python
  is_ensure_text_enabled = LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT)
  print(is_ensure_text_enabled)  # Output: True or False
  ```

#### MultiLangString Control Examples

- Disabling a flag:
  ```python
  MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, False)
  ```
- Retrieving the current state of a flag:
  ```python
  is_valid_lang_enforced = MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_VALID_LANG)
  print(is_valid_lang_enforced)  # Output: True or False
  ```

#### `set_flag` Method

The `set_flag` method is used to enable or disable a specific flag for either LangString or MultiLangString. This method allows for dynamic configuration of behavior, such as enforcing non-empty text or valid language tags.

**Examples**:

- Enabling the ENSURE_TEXT flag for LangString:
  ```python
  LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
  ```
- Disabling the ENSURE_VALID_LANG flag for MultiLangString:
  ```python
  MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, False)
  ```

#### `get_flag` Method

The `get_flag` method retrieves the current state (enabled or disabled) of a specified flag. It is useful for checking the configuration status of LangString or MultiLangString instances.

**Examples**:

- Checking if ENSURE_TEXT is enabled for LangString:
  ```python
  is_text_ensured = LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT)
  print(is_text_ensured)  # Output: True or False
  ```
- Checking if ENSURE_VALID_LANG is enabled for MultiLangString:
  ```python
  is_valid_lang_enforced = MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_VALID_LANG)
  print(is_valid_lang_enforced)  # Output: True or False
  ```

#### `reset_flags` Method

The `reset_flags` method resets all flags to their default values. This is particularly useful for restoring the default behavior after temporary changes to the configuration flags.

**Examples**:

- Resetting all flags for LangString:
  ```python
  LangStringControl.reset_flags()
  ```
- Resetting all flags for MultiLangString:
  ```python
  MultiLangStringControl.reset_flags()
  ```

#### `print_flags` Method

The `print_flags` method prints the current state of all configuration flags to the console. It is a convenient tool for debugging or monitoring the current flag settings.

**Examples**:

- Printing all flags for LangString:
  ```python
  LangStringControl.print_flags()
  ```
- Printing all flags for MultiLangString:
  ```python
  MultiLangStringControl.print_flags()
  ```

This section provides an overview of the control and flag system in the LangString Library, including how to use the control classes and their methods to manage the behavior of LangString and MultiLangString instances. The examples illustrate practical use cases for these methods.

## Code Testing

The code provided has undergone rigorous testing to ensure its reliability and correctness. The tests can be found in the 'tests' directory of the project. To run the tests, navigate to the project root directory and execute the following command:

```bash
langstring> pytest .\tests
```

## Version 2: Key Differences and Improvements

The LangString Library has undergone significant enhancements from Version 1 (v1) to Version 2 (v2). These changes have improved the library's functionality and usability, particularly in terms of control mechanisms and handling multilingual strings. Below are the key differences and improvements:

- Global Control Availability
    - **V1**: Global control was not available for both `LangString` and `MultiLangString`.
    - **V2**: Global control has been introduced for both `LangString` and `MultiLangString`, allowing for more flexible and centralized management of behavior across all instances.

- Individual Level Control
    - **V1**: Individual level control was only available for `MultiLangString`, with no control options for `LangString`.
    - **V2**: Both `LangString` and `MultiLangString` now have global control capabilities, enhancing consistency and ease of configuration.

- Handling of Multilingual Strings
    - **V1**: `MultiLangString` was designed to handle a single string associated with multiple languages, allowing for synonyms.
    - **V2**: The internal structure of `MultiLangString` has been rebuilt. It now handles multiple strings associated with multiple languages, still allowing for synonyms. This change provides more versatility in managing multilingual content.

- Method Restructuring in MultiLangString
    - **V2**: Methods in `MultiLangString` have been restructured, offering more options and improved functionality in v2 compared to v1.

- Dependency Between MultiLangString and LangString
    - **V1**: `MultiLangStrings` were entirely dependent on `LangStrings`.
    - **V2**: This dependency has been removed. `MultiLangString` now operates independently of `LangString`, providing more flexibility and reducing coupling between these two components.

These improvements in v2 of the LangString Library mark a significant step forward in its capability to handle multilingual text data, offering users more control and flexibility in their applications.

## How to Contribute

### Reporting Issues

- If you encounter a bug or wish to suggest a feature, please [open a new issue](https://github.com/pedropaulofb/langstring/issues/new).
- If you notice any discrepancies in the documentation created with the aid of AI, feel free to [report them by opening an issue](https://github.com/pedropaulofb/langstring/issues/new).

### Code Contributions

1. Fork the project repository and create a new feature branch for your work: `git checkout -b feature/YourFeatureName`.
2. Make and commit your changes with descriptive commit messages.
3. Push your work back up to your fork: `git push origin feature/YourFeatureName`.
4. Submit a pull request to propose merging your feature branch into the main project repository.

### Test Contributions

- Enhance the project's reliability by adding new tests or improving existing ones.

### General Guidelines

- Ensure your code follows our coding standards.
- Update the documentation as necessary.
- Make sure your contributions do not introduce new issues.

We appreciate your time and expertise in contributing to this project!

## Dependencies

This project can be set up using either Poetry or `requirements.txt`. Both are kept in sync to ensure consistency in dependencies.

### Using Poetry

[Poetry](https://python-poetry.org/) is used for easy management of dependencies and packaging. To install the dependencies with Poetry, first [install Poetry](https://python-poetry.org/docs/#installation) if you haven't already, and then run:

```bash
poetry install
```

This will install all the dependencies as specified in `pyproject.toml`.

### Using `requirements.txt`

If you prefer not to use Poetry, a `requirements.txt` file is also provided. You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

This is a straightforward way to set up the project if you are accustomed to using pip and traditional requirements files.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/pedropaulofb/langstring/blob/main/LICENSE) file for details.

## Author

This project is an initiative of the [Semantics, Cybersecurity & Services (SCS) Group](https://www.utwente.nl/en/eemcs/scs/) at the [University of Twente](https://www.utwente.nl/), The Netherlands. The main developer is:

- Pedro Paulo Favato Barcelos [[GitHub](https://github.com/pedropaulofb)] [[LinkedIn](https://www.linkedin.com/in/pedro-paulo-favato-barcelos/)]

Feel free to reach out using the provided links. For inquiries, contributions, or to report any issues, you can [open a new issue](https://github.com/pedropaulofb/langstring/issues/new) on this repository.
