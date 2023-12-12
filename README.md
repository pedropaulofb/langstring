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
![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/langstring)
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
  * [LangString Overview](#langstring-overview)
    * [Benefits of LangStrings](#benefits-of-langstrings)
    * [Practical Use of LangStrings](#practical-use-of-langstrings)
    * [LangString Class - Usage Examples](#langstring-class---usage-examples)
    * [Control Options for LangString](#control-options-for-langstring)
      * [Available Flags](#available-flags)
      * [Setting and Retrieving Flags](#setting-and-retrieving-flags)
      * [Example Usage](#example-usage)
  * [MultiLangString: Handling Multiple Translations](#multilangstring-handling-multiple-translations)
    * [MultiLangString Control Options](#multilangstring-control-options)
      * [Available Controls](#available-controls)
    * [Usage Examples for the MultiLangString Class](#usage-examples-for-the-multilangstring-class)
  * [Getting Started](#getting-started)
    * [Installation](#installation)
    * [Importing and Using the Library](#importing-and-using-the-library)
      * [Example Usage of `LangString`](#example-usage-of-langstring)
      * [Example Usage of `MultiLangString`](#example-usage-of-multilangstring)
    * [Comparison and Hashing](#comparison-and-hashing)
      * [LangString](#langstring)
        * [Equality and Inequality](#equality-and-inequality)
        * [Hashing](#hashing)
      * [MultiLangString](#multilangstring)
        * [Equality and Inequality](#equality-and-inequality-1)
        * [Hashing](#hashing-1)
  * [Code Testing](#code-testing)
  * [Changelog and Future Development](#changelog-and-future-development)
    * [Version 1.3.0 - [To be developed: Translations for MultiLangString (Expected)]](#version-130---to-be-developed-translations-for-multilangstring-expected)
    * [Version 1.2.0 - [To be developed: MultiLangStringControl and MultiLangStringFlags (Expected)]](#version-120---to-be-developed-multilangstringcontrol-and-multilangstringflags-expected)
    * [Version 1.1.0 - [Released: LangStringControl and LangStringFlags]](#version-110---released-langstringcontrol-and-langstringflags)
      * [New Features](#new-features)
      * [Enhancements](#enhancements)
      * [Usage](#usage)
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

## LangString Overview

**LangString** is a powerful Python library inspired by the RDF's idea of language tagging. It offers a streamlined approach to handle multilingual data in Python.

### Benefits of LangStrings

- **Context**: Knowing the language of a text is crucial for processing and presentation.

- **User Experience**: For apps with global users, displaying data in a user's language improves their experience. LangStrings make this process efficient.

- **Data Consistency**: With LangStrings, multilingual data has a standard format, reducing complexity.

- **Tailored Operations**: Having the language info allows for specialized actions, especially in fields like NLP.

### Practical Use of LangStrings

Consider the value of LangStrings in real-world scenarios:

- **Greeting Users**:

```python
# English vs Japanese greeting
greeting_en = LangString(text="Hello", lang="en")
greeting_ja = LangString(text="こんにちは", lang="ja")

print(greeting_en.to_string())  # "Hello"@en
print(greeting_ja.to_string())  # "こんにちは"@ja
```

- **Multilingual Product Names**:

```python
# Eiffel Tower in English and French
eiffel_en = LangString(text="Eiffel Tower", lang="en")
eiffel_fr = LangString(text="Tour Eiffel", lang="fr")

print(eiffel_en.to_string())  # "Eiffel Tower"@en
print(eiffel_fr.to_string())  # "Tour Eiffel"@fr
```

### LangString Class - Usage Examples

The `LangString` class in the `langstring_lib` module encapsulates a string with its associated language information.

1. Initialization

```python
# Create a LangString object with only text
simple_string = LangString("Hello, world!")

# Create a LangString object with text and language information
english_greeting = LangString("Hello, world!", "en")
```

If an invalid language tag is used or non-string type is provided, appropriate warnings and errors will be raised:

```python
# This will log a warning because 'invalid-lang' is not a valid language tag
invalid_lang = LangString("Hello, world!", "invalid-lang")

# This will raise a TypeError since the text is not a string
try:
    invalid_text_type = LangString(12345)
except TypeError as e:
    print(f"Error: {e}")  # Outputs an error message if the input is not a string
```

### Control Options for LangString

The `LangString` class is designed to work with text strings and their associated language tags, offering enhanced functionality and control over how these strings are handled and validated. This control is achieved through a set of flags defined in the `LangStringControl` class, using the `LangStringFlag` enumeration. These flags allow for dynamic configuration of `LangString` behavior, enabling customization to fit various application needs.

#### Available Flags

- `ENSURE_TEXT`: When enabled, this flag ensures that the `text` field of a `LangString` object is not empty. An attempt to create a `LangString` with an empty `text` field will raise a `ValueError`.

- `ENSURE_ANY_LANG`: This flag mandates the presence of a non-empty language tag in the `lang` field of a `LangString`. If enabled, creating a `LangString` with an empty `lang` field will result in a `ValueError`.

- `ENSURE_VALID_LANG`: Enabling this flag requires that the `lang` field of a `LangString` contains a valid language code. Invalid language codes will lead to a `ValueError` upon `LangString` creation.

- `VERBOSE_MODE`: This flag activates verbose logging. When enabled, any warnings or informational messages related to `LangString` operations, such as the use of empty strings or invalid language tags, are logged for better traceability and debugging.

#### Setting and Retrieving Flags

Flags can be set globally and will affect the behavior of all `LangString` instances within the application. To set a flag, use:

```python
LangStringControl.set_flag(LangStringFlag.<FLAG_NAME>, <True/False>)
```

To check the current state of a flag:

```python
current_state = LangStringControl.get_flag(LangStringFlag.<FLAG_NAME>)
```

#### Example Usage
```python
from langstring import LangString, LangStringControl, LangStringFlag

# Enable the ENSURE_TEXT flag
LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

# Attempting to create a LangString with an empty text will raise an error
try:
    lang_str = LangString("", "en")
except ValueError as e:
    print(e)  # Output: "ENSURE_TEXT enabled: Langstring's 'text' field cannot receive empty string."

# Disable the ENSURE_TEXT flag
LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, False)

# Now, creating a LangString with an empty text will succeed
lang_str = LangString("", "en")
```

2. Converting the LangString Object to String

The `LangString` class provides two methods to convert the object into its string representation, `to_string()` and `__str__()`:

```python
english_greeting = LangString("Hello, world!", "en")

# Using the to_string() method
print(english_greeting.to_string())  # Outputs: "Hello, world!"@en

# Using the __str__() method (which is implicitly called when using Python's built-in str() function)
print(str(english_greeting))  # Outputs: "Hello, world!"@en
```

The string representation will include the text encapsulated in double quotes. If a language is associated with the text, it will be appended after the text, preceded by an "@" symbol.

## MultiLangString: Handling Multiple Translations

While `LangString` manages one string-language pair, `MultiLangString` holds several translations of a string. This is useful for keeping various translations of a term within one object.

For instance, if you have a product with multiple language names:

```python
from langstring import MultiLangString

product_names = MultiLangString({
    "en": "Smartphone",
    "fr": "Smartphone",
    "es": "Teléfono inteligente",
    "de": "Smartphone"
})

print(product_names.get_lang("es"))  # Teléfono inteligente
```

### MultiLangString Control Options

`MultiLangString` provides granular controls for handling situations where there are multiple entries with the same language tag. This behavior is defined by the `MULTIPLE_ENTRIES_CONTROLS` configuration.

#### Available Controls

1. **`ALLOW`**:
    - **Description**: Permits multiple entries with the same language tag. However, it ensures that no duplicate texts for the same language tag are added.
    - **Usage**: Beneficial in situations where multiple translations or interpretations of a term in the same language are valid.

2. **`OVERWRITE`**:
    - **Description**: If an entry with the same language tag already exists, this control will overwrite the existing entry with the new value.
    - **Usage**: Useful in scenarios where you want to ensure that there's only one entry per language and are okay with updating existing values.

3. **`BLOCK_WARN`**:
    - **Description**: Blocks the addition of a `LangString` if a matching language tag already exists and logs a warning.
    - **Usage**: Recommended for cases where you want to prevent duplicate entries but only want a log warning instead of a halt in operations.

4. **`BLOCK_ERROR`**:
    - **Description**: Blocks the addition of a `LangString` if a matching language tag is present and raises an error.
    - **Usage**: Useful when ensuring data integrity is paramount, and you want to halt the operation if a duplicate entry is encountered.

When setting the `control` property of a `MultiLangString` instance, it is essential to provide a valid control strategy. If an invalid strategy is supplied, the system will raise a `ValueError` highlighting the acceptable control values.

To utilize these controls, configure the desired behavior when initializing the `MultiLangString` object or updating its entries.

### Usage Examples for the MultiLangString Class

1. Initialization

You can initialize a `MultiLangString` object by passing in multiple `LangString` objects and specifying control and preferred language properties:

```python
from langstring import LangString, MultiLangString

english_greeting = LangString("Hello", "en")
french_greeting = LangString("Bonjour", "fr")

# Initializing MultiLangString with two LangString objects
multi_lang_str = MultiLangString(english_greeting, french_greeting, control="ALLOW", preferred_lang="en")
```

2. Add Method

Use the `add` method to add a new `LangString` object to the `MultiLangString`:

```python
lang_str3 = LangString("Hola", "es")
multi_lang_str.add_langstring(lang_str3)
```

3. Getting a Specific Language String

To retrieve a language string for a specific language:

```python
english_strings = multi_lang_str.get_langstring("en")  # Returns list of English strings
```

4. Getting the Preferred Language String

Retrieve the language string for the preferred language:

```python
preferred_string = multi_lang_str.get_pref_langstring()  # Returns the string for the preferred language
```

5. Removing a Specific LangString

Remove a specific `LangString` object from the `MultiLangString`:

```python
multi_lang_str.remove_langstring(lang_str3)  # Removes the Spanish string
```

6. Removing All Strings for a Specific Language

Remove all `LangString` objects associated with a specific language:

```python
multi_lang_str.remove_language("es")  # Removes all Spanish strings
```

7. Converting to String

You can convert a `MultiLangString` object to a string representation:

```python
str_representation = multi_lang_str.to_string()
print(str_representation)  # Outputs: '"Hello"@en, "Bonjour"@fr'
```

8. Converting to List of Strings

Convert the `MultiLangString` to a list of strings:

```python
list_representation = multi_lang_str.to_string_list()
print(list_representation)  # Outputs: ['"Hello"@en', '"Bonjour"@fr']
```

9. Getting the Length

Determine the number of `LangString` objects in a `MultiLangString`:

```python
length = len(multi_lang_str)  # Outputs: 2
```

10. String Representation

"Obtain a user-friendly string representation of the `MultiLangString`. This representation is ideal for displaying the content of the `MultiLangString` object in a readable format, suitable for user interfaces or textual outputs. The `str()` method is used to achieve this."

```python
print(str(multi_lang_str))  # Outputs: '"Hello"@en, "Bonjour"@fr'

```

11. Representation Method

Use the `repr()` method to get a formal, detailed string representation of the `MultiLangString` object. This output is more technical, showing the exact state of the object, which is particularly useful for debugging and development purposes. It provides a clear view of the internal structure and data of the `MultiLangString`."

```python
print(repr(multi_lang_str))  # Outputs a detailed, technical representation of the object
```

This is useful for understanding the current state of a `MultiLangString` object.

Remember, the `MultiLangString` class is designed to handle multiple language strings, allowing you to manage multilingual text strings effectively and efficiently.

## Getting Started

### Installation

Install with:

```bash
pip install langstring
```

Then, encapsulate strings with their language tags as shown in the examples above.

### Importing and Using the Library

After installation, you can use the `LangString` and `MultiLangString` classes in your project. Simply import the classes and start encapsulating strings with their language tags.

```python
from langstring import LangString, MultiLangString
```

#### Example Usage of `LangString`

```python
# Creating a LangString object for an English greeting
greeting_en = LangString("Hello", "en")

# Printing the LangString object, which shows the text and its language tag
print(greeting_en)  # Output: "Hello"@en
```

#### Example Usage of `MultiLangString`

```python
# Create LangString objects for greetings in English and Spanish
greeting_en = LangString("Hello", "en")
greeting_es = LangString("Hola", "es")

# Use MultiLangString to combine them. The 'control' parameter determines how duplicate language tags are handled.
combined_greeting = MultiLangString(greeting_en, greeting_es, control="ALLOW")

# Fetch and print a greeting based on language
# Note: The `get_langstring` method returns a list, so we'll take the first item if available
spanish_greetings = combined_greeting.get_langstring("es")
if spanish_greetings:
    print(spanish_greetings[0])  # Outputs: "Hola"@es
else:
    print("No greeting found for the specified language.")

# Retrieve the preferred language's greeting (defaults to English in this example)
preferred_greeting = combined_greeting.get_pref_langstring()
if preferred_greeting:
    print(preferred_greeting)  # Outputs: "Hello"@en
else:
    print("No greeting found for the preferred language.")
```

### Comparison and Hashing

Both the `LangString` and the `MultiLangString` classes support comparison and hashing operations, making it easier to compare and manage these objects in data structures like sets and dictionaries.

#### LangString

##### Equality and Inequality

- `__eq__`: Checks if two `LangString` objects are equal (both `text` and `lang` attributes are the same).
- `__ne__`: Checks if two `LangString` objects are not equal.

```python
from langstring import LangString

ls1 = LangString("Hello", "en")
ls2 = LangString("Hello", "en")
ls3 = LangString("Hola", "es")

# Equality
print(ls1 == ls2)  # Output: True
print(ls1 == ls3)  # Output: False

# Inequality
print(ls1 != ls2)  # Output: False
print(ls1 != ls3)  # Output: True
```

##### Hashing

- `__hash__`: Generates a hash value for a `LangString` object, allowing it to be used in sets and as dictionary keys.

```python
from langstring import LangString

ls1 = LangString("Hello", "en")
ls2 = LangString("Hello", "en")
ls3 = LangString("Hola", "es")

# Using LangString objects in a set
lang_strings = {ls1, ls2, ls3}
print(len(lang_strings))  # Output: 2 (since ls1 and ls2 are equal)

# Using LangString as dictionary keys
lang_dict = {ls1: "Greeting in English", ls3: "Greeting in Spanish"}
print(lang_dict[ls1])  # Output: "Greeting in English"
```

#### MultiLangString

##### Equality and Inequality

- `__eq__`: Checks if two `MultiLangString` objects are equal. Equality is determined based on the content of the `langstrings` attribute, which holds the multilingual data. The `preferred_lang` and `control` attributes are not considered in this comparison.

```python
from multilangstring import MultiLangString, LangString

mls1 = MultiLangString(LangString("Hello", "en"), LangString("Hola", "es"))
mls2 = MultiLangString(LangString("Hello", "en"), LangString("Hola", "es"))
mls3 = MultiLangString(LangString("Bonjour", "fr"))

# Equality
print(mls1 == mls2)  # Output: True
print(mls1 == mls3)  # Output: False
```

##### Hashing

- `__hash__`: Generates a hash value for a `MultiLangString` object, allowing it to be used in sets and as dictionary keys. The hash is computed based on the `langstrings` attribute.

```python
from multilangstring import MultiLangString, LangString

mls1 = MultiLangString(LangString("Hello", "en"), LangString("Hola", "es"))
mls2 = MultiLangString(LangString("Hello", "en"), LangString("Hola", "es"))
mls3 = MultiLangString(LangString("Bonjour", "fr"))

# Using MultiLangString objects in a set
multi_lang_strings = {mls1, mls2, mls3}
print(len(multi_lang_strings))  # Output: 2 (since mls1 and mls2 are equal)

# Using MultiLangString as dictionary keys
multi_lang_dict = {mls1: "Greetings in English and Spanish", mls3: "Greeting in French"}
print(multi_lang_dict[mls1])  # Output: "Greetings in English and Spanish"
```

## Code Testing

The code provided has undergone rigorous testing to ensure its reliability and correctness. The tests can be found in the 'tests' directory of the project. To run the tests, navigate to the project root directory and execute the following command:

```bash
langstring> pytest .\tests
```

## Changelog and Future Development

### Version 1.3.0 - [To be developed: Translations for MultiLangString (Expected)]
### Version 1.2.0 - [To be developed: MultiLangStringControl and MultiLangStringFlags (Expected)]

### Version 1.1.0 - [Released: LangStringControl and LangStringFlags]

#### New Features
- **LangStringControl**: A new class introduced to manage the configuration settings for language strings dynamically. This addition allows for global settings that affect the behavior of `LangString` instances throughout your application.

- **LangStringFlags**: An enumeration (`LangStringFlag`) that defines various configuration flags. These flags provide enhanced control over the `LangString` class, enabling behaviors such as:
  - `ENSURE_TEXT`: Ensures that the `text` field in `LangString` is not empty.
  - `ENSURE_ANY_LANG`: Requires a non-empty language tag in `LangString`.
  - `ENSURE_VALID_LANG`: Enforces the use of valid language codes in `LangString`.
  - `VERBOSE_MODE`: Activates verbose logging for operations, aiding in debugging and monitoring.

#### Enhancements
- Improved validation and error handling in `LangString` based on the new control flags.
- Enhanced logging capabilities with the integration of the `VERBOSE_MODE` flag, providing better insights into the library's operations.

#### Usage
These new features can be utilized to fine-tune the behavior of `LangString` objects in various scenarios, making the library more adaptable to specific requirements. For detailed usage examples, refer to the [Control Options for LangString](#control-options-for-langstring) section.


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
