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
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8328/badge)](https://www.bestpractices.dev/projects/8328)
![Static Badge](https://img.shields.io/badge/Test_Coverage-100%25-green)

# LangString Python Library

LangString is a Python library designed to handle multilingual text data with precision and flexibility. Although the need for robust management of multilingual content is critical, existing solutions often lack the necessary features to manage language-tagged strings, sets of strings, and collections of multilingual strings effectively. LangString addresses this gap by providing classes and utilities that enable the creation, manipulation, and validation of multilingual text data consistently and accurately. Inspired by [RDFS's langstrings](https://www.w3.org/TR/rdf-schema/), LangString integrates seamlessly into Python applications, offering familiar methods that mimic those of regular Python types, making it intuitive for developers to adopt and use.

**📦 PyPI Package:**
The library is conveniently [available as a PyPI package](https://pypi.org/project/langstring/), allowing users to easily import it into other Python projects.

**📚 Documentation:**
For detailed documentation and code examples, please refer to the library's [docstring-generated documentation](https://pedropaulofb.github.io/langstring).

## Contents

<!-- TOC -->
* [LangString Python Library](#langstring-python-library)
  * [Contents](#contents)
  * [Installation and Usage](#installation-and-usage)
    * [Dependencies](#dependencies)
      * [Mandatory Dependencies](#mandatory-dependencies)
      * [Optional Dependencies](#optional-dependencies)
      * [Dev Dependencies](#dev-dependencies)
    * [Installation](#installation)
      * [Basic Installation](#basic-installation)
      * [Full Installation](#full-installation)
      * [Dev Installation](#dev-installation)
    * [Importing Elements](#importing-elements)
    * [Basic Usage](#basic-usage)
  * [Library Reference](#library-reference)
    * [Classes](#classes)
      * [LangStrings](#langstrings)
      * [SetLangStrings](#setlangstrings)
      * [MultiLangStrings](#multilangstrings)
      * [Controller](#controller)
      * [Converter](#converter)
    * [Configuration](#configuration)
    * [Elements' Relations](#elements-relations)
  * [Testing](#testing)
    * [Test Organization](#test-organization)
    * [Running the Tests](#running-the-tests)
    * [Continuous Integration](#continuous-integration)
  * [How to Contribute](#how-to-contribute)
    * [Reporting Issues](#reporting-issues)
    * [Code Contributions](#code-contributions)
    * [Test Contributions](#test-contributions)
    * [General Guidelines](#general-guidelines)
  * [Related Libraries and Differences](#related-libraries-and-differences)
  * [License](#license)
  * [Author](#author)
<!-- TOC -->

## Installation and Usage

### Dependencies

The LangString Python Library has been designed to be lightweight and easy to install. It has no mandatory dependencies and a single optional dependency to keep the installation process straightforward and ensure compatibility with various environments.

All dependencies of the LangString library can be found in its [`pyproject.toml` file](https://github.com/pedropaulofb/langstring/blob/main/pyproject.toml).

#### Mandatory Dependencies
The LangString Library does not require mandatory dependencies.

#### Optional Dependencies

The LangString Library has a single optional dependency, the [langcodes package](https://pypi.org/project/langcodes/). It is used  particularly for validating language tags when the `ENSURE_VALID_LANG` flag is enabled. This dependency is crucial for ensuring that language tags used in LangString and `MultiLangString` instances are valid and conform to international standards, thereby maintaining the integrity and reliability of multilingual text processing.

#### Dev Dependencies

For a complete list of development dependencies, please refer to the [Dev Dependencies List](https://github.com/pedropaulofb/langstring/blob/main/documentation/dev_dependencies_md).

### Installation

#### Basic Installation

To install the LangString library using `pip`, which is the package installer for Python, run the following command in your terminal or command prompt:

```sh
pip install langstring
```

This will download and install the latest version of the LangString library from [PyPI (Python Package Index)](https://pypi.org/project/langstring/).

#### Full Installation

For the full functionally of the LangString library, you need to install it together with its [optional dependency](#optional-dependencies) [langcodes](https://github.com/rspeer/langcodes/). To do that, use the following `pip` command:

```sh
pip install langstring[langcodes]
```

This command will install LangString along with the `langcodes` package.

#### Dev Installation

If you are planning to contribute to the development of `langstring`, you should install the [development dependencies](#dev-dependencies). First, you need to clone the repository. Run the following commands:

```sh
git clone https://github.com/pedropaulofb/langstring.git
cd langstring
pip install -r requirements.txt
```

This will clone the repository, navigate into the project directory, and install all the necessary packages needed for development.

### Importing Elements

After installation, you can use the following elements in your project: LangString, SetLangString, MultiLangString, Controller, GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag, and Converter.

To import these elements, use the following import statement:

```python
from langstring import LangString, SetLangString, MultiLangString, Controller, GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag, Converter
```

### Basic Usage

1. **LangString** is used to handle a string in a specific language.

   ```python
   from langstring import LangString

   # Create a LangString object
   lang_str = LangString("Hello, World!", "en")

   # Print the string representation
   print(lang_str)  # Output: "Hello, World!"@en
   ```

2. **SetLangString** allows you to handle a set of strings in a specific language.

   ```python
   from langstring import SetLangString

   # Create a SetLangString object
   set_lang_str = SetLangString({"Hello", "Hi"}, "en")

   # Print the set of strings
   print(set_lang_str)  # Output: {'Hello', 'Hi'}@en
   ```

3. **MultiLangString** manages strings in multiple languages.

   ```python
   from langstring import MultiLangString

   # Create a MultiLangString object
   multi_lang_str = MultiLangString({"en": {"Hello", "Hi"}, "es": {"Hola"}})

   # Print the multilingual string representation
   print(multi_lang_str)  # Output: en: {'Hello', 'Hi'}, es: {'Hola'}
   ```

4. **Controller** and **Flags** are used to manage global and specific language string states.

   ```python
   from langstring import Controller, GlobalFlag

   # Set a flag
   Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)

   # Print the state of a specific flag
   Controller.print_flag(GlobalFlag.LOWERCASE_LANG)  # Output: GlobalFlag.LOWERCASE_LANG = True
   ```

5. **Converter** is used to convert language strings between different formats.

   ```python
   from langstring import Converter, LangString, SetLangString, MultiLangString

   # Convert a string to a LangString using the 'manual' method
   langstring = Converter.from_string_to_langstring("manual", "Hello", "en")
   print(langstring)  # Output: "Hello"@en

   # Convert a list of strings to a list of LangStrings using the 'parse' method
   langstrings = Converter.from_strings_to_langstrings("parse", ["Hello@en", "Bonjour@fr"], separator="@")
   for ls in langstrings:
       print(ls)  # Output: "Hello"@en
                  #         "Bonjour"@fr
   ```


## Library Reference

### Classes

#### LangStrings

The LangString class is a fundamental component of the LangString Library, designed to encapsulate a single string along with its associated language information. It is primarily used in scenarios where the language context of a text string is crucial, such as in multilingual applications, content management systems, or any software that deals with language-specific data. The class provides a structured way to manage text strings, ensuring that each piece of text is correctly associated with its respective language.

In the LangString class, the string representation format varies based on the presence of a language tag. When a language tag is provided, the format is `text`. Without a language tag, it is formatted as `"text"@lang`, where lang is the language code.

- [Methods](https://github.com/pedropaulofb/langstring/blob/main/documentation/methods_langstring_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/langstring/)

#### SetLangStrings

TODO

- [Methods](https://github.com/pedropaulofb/langstring/blob/main/documentation/methods_setlangstring_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/setlangstring/)

#### MultiLangStrings

The `MultiLangString` class is a key component of the LangString Library, designed to manage and manipulate text strings across multiple languages. This class is particularly useful in applications that require handling of text in a multilingual context, such as websites, applications with internationalization support, and data processing tools that deal with multilingual data. The primary purpose of `MultiLangString` is to store, retrieve, and manipulate text entries in various languages, offering a flexible and efficient way to handle multilingual content.

- [Methods](https://github.com/pedropaulofb/langstring/blob/main/documentation/methods_multilangstring_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/multilangstring/)

#### Controller

The Control and Flags system in the LangString Library plays a pivotal role in managing and configuring the behavior of LangString and `MultiLangString` instances.

This system operates at a global, class-level context, meaning that the flags and controls applied have a uniform effect across all instances of these classes. In other words, when a flag is set or reset using the control classes, it impacts every instance of LangString and `MultiLangString` throughout the application. This ensures consistent behavior and validation rules across all instances, as individual instances cannot have differing flag values.

In the following subsections, we will delve into the specifics of the available flags and the control methods. The flags define key aspects of how LangString and `MultiLangString` instances handle multilingual text, including validation rules and representation formats. Understanding these flags is crucial for effectively utilizing the library in various scenarios, especially those involving multilingual content.

The control methods, shared between `Controller` and `MultiLangStringControl`, provide the mechanisms to set, retrieve, and reset these flags. These methods ensure that you can dynamically configure the behavior of the library to suit your application's needs. We will explore each method in detail, providing insights into their usage and impact on the library's functionality.

The LangString and MultiLangString classes use a set of flags to control various aspects of their behavior. These flags are managed by `Controller` and `MultiLangStringControl` respectively. The flags provide a flexible way to customize the behavior of LangString and `MultiLangString` classes according to the specific needs of your application. By adjusting these flags, you can enforce different levels of validation and control over the language data being processed. The available flags and their effects are as follows.

The Control classes, namely `Controller` and `MultiLangStringControl`, act as static managers for the flags. They provide methods to set, retrieve, and reset the states of these flags, ensuring consistent behavior across all instances of LangString and `MultiLangString`.

- [Methods](https://github.com/pedropaulofb/langstring/blob/main/documentation/methods_controller_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/controller/)


#### Converter

- [Methods](https://github.com/pedropaulofb/langstring/blob/main/documentation/methods_converter_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/converter/)

### Configuration

- [Flags' List](https://github.com/pedropaulofb/langstring/blob/main/documentation/flags_list_md)
- [Documentation](https://pedropaulofb.github.io/langstring/autoapi/langstring/flags/)

### Elements' Relations

![](https://raw.githubusercontent.com/pedropaulofb/langstring/main/documentation/import_schema_basic.svg)

## Testing

The LangString Python Library is rigorously tested to ensure robustness and reliability. We have achieved 100% test coverage, with tests implemented for each method provided by the library. This ensures that every aspect of the library is thoroughly validated and any potential issues are caught early.

### Test Organization

The tests are organized into [several directories](https://github.com/pedropaulofb/langstring/tree/main/tests), each focusing on different components of the library:

- `tests_langstring`: Tests for the core LangString functionalities.
- `tests_utils`: Utility tests to ensure the correctness of helper functions.
- `tests_setlangstring`: Tests for SetLangString functionalities.
- `tests_multilangstring`: Tests for MultiLangString functionalities.
- `tests_converter`: Tests for Conversor functionalities.
- `tests_controller`: Tests for Controller functionalities.

### Running the Tests

To run the tests, you can use the following command in the command line within the test directory of the project:

```sh
pytest
```

This command will execute all the tests and provide a detailed report on the coverage and any potential issues.

### Continuous Integration

We use GitHub Actions to automatically run our tests on every push to the repository. The [Action's workflow](https://github.com/pedropaulofb/langstring/blob/main/.github/workflows/code_testing.yml) execute the tests across multiple operating systems and Python versions to ensure compatibility and reliability.

- **Operating Systems**: Windows, Linux, and macOS.
- **Python Versions**: 3.11 and 3.12.

## How to Contribute

We welcome and appreciate contributions from the community! Whether you want to report a bug, suggest a new feature, or improve our codebase, your input is valuable.

### Reporting Issues

- If you find a bug or wish to suggest a feature, please [open a new issue](https://github.com/pedropaulofb/langstring/issues/new).
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

## Related Libraries and Differences

The LangString Library offers unique functionalities for handling multilingual text in Python applications. While there are several libraries and tools available for internationalization, localization, and language processing, they differ from the LangString Library in scope and functionality. Below is an overview of related work and how they compare to the LangString library:

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

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/pedropaulofb/langstring/blob/main/LICENSE) file for details.

## Author

The LangString library is developed and maintained by:

- Pedro Paulo Favato Barcelos [[GitHub](https://github.com/pedropaulofb)] [[LinkedIn](https://www.linkedin.com/in/pedro-paulo-favato-barcelos/)]

Feel free to reach out using the provided links. For inquiries, contributions, or to report any issues, you can [open a new issue](https://github.com/pedropaulofb/langstring/issues/new) on this repository.
