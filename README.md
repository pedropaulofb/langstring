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
    * [Installation and Use](#installation-and-use)
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
      * [`ENSURE_TEXT`](#ensuretext)
      * [`ENSURE_ANY_LANG`](#ensureanylang)
      * [`ENSURE_VALID_LANG`](#ensurevalidlang)
    * [Example Usage of Flags](#example-usage-of-flags)
    * [Control](#control)
      * [`set_flag` Method](#setflag-method)
      * [`get_flag` Method](#getflag-method)
      * [`reset_flags` Method](#resetflags-method)
      * [`print_flags` Method](#printflags-method)
    * [LangString Control Examples](#langstring-control-examples)
    * [MultiLangString Control Examples](#multilangstring-control-examples)
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

In the LangString class, the string representation format varies based on the presence of a language tag. When a language tag is provided, the format is `text`. Without a language tag, it is formatted as `"text"@lang`, where lang is the language code.

### LangStrings’ Methods

The `LangString` class offers a range of methods to efficiently handle language-specific text. These methods enable the initialization, representation, comparison, and validation of text strings in their language context.

#### `__init__`

Initializes a new LangString object, encapsulating a given text string with an associated language tag. The `text` parameter is the string to be encapsulated, and `lang` is an optional parameter specifying the language tag (e.g., 'en' for English). This method forms the core of the LangString class, allowing for the creation of language-aware string objects.

Example:

```python
# Import necessary class
from langstring import LangString

# Creating a LangString instance without a language tag
greeting = LangString("Hello")
print(greeting)  # Expected Output: Hello

# Creating a LangString instance with a language tag
french_greeting = LangString("Bonjour", "fr")
print(french_greeting)  # Expected Output: "Bonjour"@fr
```

#### `to_string`

Converts the LangString object into a human-readable string representation, including the language tag if present. This method is particularly useful for displaying or logging LangString objects, providing a clear and concise view of their content and associated language.

Example:

```python
# Import necessary class
from langstring import LangString

# Creating and printing a LangString instance
greeting = LangString("Hello", "en")
print(greeting.to_string())  # Expected Output: "Hello"@en
```

#### `__str__`

Defines how the LangString object is represented as a string when printed or converted to a string. This method returns the encapsulated text, optionally followed by the language tag, providing a standard way to view and understand the LangString's content.

Example:

```python
# Import necessary class
from langstring import LangString

# Creating and printing a LangString instance
greeting = LangString("Hello", "en")
print(greeting)  # Expected Output: "Hello"@en
```

#### `__eq__`

Determines whether two LangString objects are equal by comparing both their text and language tags. This method is essential for identifying identical language-specific strings, ensuring accurate comparisons in contexts like sorting, filtering, or deduplication.

Example:

```python
# Import necessary class
from langstring import LangString

# Comparing two LangString instances
greeting_en1 = LangString("Hello", "en")
greeting_en2 = LangString("Hello", "en")
print(greeting_en1 == greeting_en2)  # Expected Output: True

# Comparing LangString instances with different texts or languages
greeting_es = LangString("Hola", "es")
print(greeting_en1 == greeting_es)  # Expected Output: False
```

#### `__hash__`

Generates a unique hash value for the LangString object, enabling its use in hash-based collections like sets or dictionaries. This method ensures that LangString objects can be efficiently stored and retrieved in data structures that rely on hashing.

Example:

```python
# Import necessary class
from langstring import LangString

# Creating a LangString instance and printing its hash value
greeting = LangString("Hello", "en")
print(hash(greeting))  # Output: (hash value, e.g., 224086809330009634)
```

## MultiLangStrings

The `MultiLangString` class is a key component of the LangString Library, designed to manage and manipulate text strings across multiple languages. This class is particularly useful in applications that require handling of text in a multilingual context, such as websites, applications with internationalization support, and data processing tools that deal with multilingual data. The primary purpose of `MultiLangString` is to store, retrieve, and manipulate text entries in various languages, offering a flexible and efficient way to handle multilingual content.

### MultiLangStrings’ Methods

The `MultiLangString` class provides a suite of methods to facilitate the management of multilingual text. These methods enable the addition, removal, retrieval, and manipulation of text entries in multiple languages, as well as setting and getting a preferred language for default text retrieval.

For MultiLangString instances, the string representation also depends on whether a language tag is associated with each text entry. Entries without a language tag are simply displayed as `text`. Entries with a language tag are presented in the format `"text"@lang`, clearly indicating their language context.

#### `__init__`

Initializes a new MultiLangString object, optionally accepting a dictionary (`mls_dict`) representing the internal structure, where keys are language codes and values are sets of text entries. The `pref_lang` parameter sets the preferred language for default text retrieval. This method lays the foundation for managing and manipulating multilingual text strings.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initializing with a dictionary
mls = MultiLangString({"en": {"Hello", "Good morning"}})
print(mls)  # Expected Output: "Good morning"@en, "Hello"@en

# Initializing with a preferred language
mls = MultiLangString(pref_lang="en")
print(mls)  # Expected Output: nothing, as the created MultiLangString is empty.

# Initializing MultiLangString with a dictionary and a preferred language
mls = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}}, pref_lang="en")
print(mls)  # Expected Output: "Hello"@en, "Good morning"@en, "Hola"@es, "Buenos días"@es

# Printing the preferred language
print("Preferred language:", mls.preferred_lang)  # Expected Output: Preferred language: en
```

#### `add_entry`

Adds a new text entry to the MultiLangString under a specified language code. This method ensures that the added text complies with the set control flags, such as non-empty strings or valid language tags, facilitating the dynamic and controlled addition of multilingual content.

Example:

```python
# Import necessary classes
from langstring import MultiLangString

# Initialize MultiLangString with multiple languages
mls = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}})

# Add a new entry in French
mls.add_entry("Bonjour", "fr")
print(mls.get_strings_all())  # Expected Output: ['Hello', 'Good morning', 'Hola', 'Buenos días', 'Bonjour']

```

#### `add_langstring`

Incorporates a LangString object directly into the MultiLangString, allowing for the seamless integration of pre-existing LangString instances. This method enhances the flexibility of MultiLangString by enabling the addition of language-specific strings already encapsulated in LangString objects.

Example:


```python
# Import necessary classes
from langstring import MultiLangString, LangString

# Initialize MultiLangString and add a LangString
mls = MultiLangString()
mls.add_langstring(LangString("Hola", "es"))
print(mls)  # Expected Output: "Hola"@es
```

#### `remove_entry`

Removes a specified text entry from the set associated with a given language in the MultiLangString. If the removal results in an empty set for that language, the language key is also removed from the internal dictionary, maintaining the integrity of the multilingual data.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString with multiple languages
mls = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}})

# Remove an entry in English
mls.remove_entry("Good morning", "en")
print(mls)  # Expected Output: "Hello"@en, "Hola"@es, "Buenos días"@es

# Remove the last entry in English
mls.remove_entry("Hello", "en")
print(mls)  # Expected Output: "Hola"@es, "Buenos días"@es

# Check if the 'en' key is still present in the dictionary
print("en" in mls.mls_dict)  # Expected Output: False (The key 'en' is no longer in the dictionary)
```

#### `remove_lang`

Eliminates all text entries associated with a specific language from the MultiLangString. This method is useful for scenarios where an entire language's content needs to be cleared, ensuring that the MultiLangString only contains relevant and active language data.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and remove a language
mls = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}})
mls.remove_lang("en")
print(mls)  # Expected Output: "Hola"@es, "Buenos días"@es
```

#### `get_langstring`

Retrieves a LangString object representing a specific text and language combination from the MultiLangString. This method is crucial for accessing individual language-specific strings within the MultiLangString, allowing users to work with or manipulate these strings as separate LangString instances.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve a LangString
mls = MultiLangString({"en": {"Hello", "Good morning"}})
lang_str = mls.get_langstring("Hello", "en")
print(lang_str)  # Expected Output: "Hello"@en
```

#### `get_langstrings_lang`

Generates a list of LangString objects for all text entries associated with a specified language in the MultiLangString. This method is ideal for extracting all language-specific strings as separate LangString instances, facilitating operations like language-based filtering or processing.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve LangStrings for a language
mls = MultiLangString({"en": {"Hello", "Good morning"}})
lang_strings = mls.get_langstrings_lang("en")
print(', '.join(str(elem) for elem in lang_strings)) # Expected Output: "Hello"@en, "Good morning"@en
```

#### `get_langstrings_all`

Compiles a comprehensive list of all LangString objects contained within the MultiLangString, covering every language and text entry. This method provides a complete overview of the multilingual content, useful for scenarios requiring a full audit or export of the stored data.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve all LangStrings
mls = MultiLangString({"en": {"Hello", "Good morning"}})
all_lang_strings = mls.get_langstrings_all()
print(', '.join(str(elem) for elem in all_lang_strings))  # Expected Output: "Hello"@en, "Good morning"@en
```

#### `get_langstrings_pref_lang`

Fetches all LangString objects corresponding to the preferred language set in the MultiLangString. This method streamlines access to the most relevant or frequently used language, simplifying tasks like default content display or language-specific analyses.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve LangStrings for the preferred language
mls = MultiLangString({"en": {"Hello", "Good morning"}}, pref_lang="en")
pref_lang_strings = mls.get_langstrings_pref_lang()
print(', '.join(str(elem) for elem in pref_lang_strings))  # Expected Output: "Hello"@en, "Good morning"@en
```

#### `get_strings_lang`

Returns a list of all text strings associated with a particular language code in the MultiLangString. This method is useful for scenarios where only the text content (without language tags) is needed for a specific language, such as generating language-specific reports or content.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve text entries for a language
mls = MultiLangString({"en": {"Hello", "Good morning"}})
texts = mls.get_strings_lang("en")
print(texts)  # Expected Output: ['Hello', 'Good morning']
```

#### `get_strings_pref_lang`

Gathers all text entries corresponding to the preferred language in the MultiLangString. This method is particularly beneficial for applications where a default language is frequently accessed, providing quick retrieval of all relevant text content.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve text entries for the preferred language
mls = MultiLangString({"en": {"Hello", "Good morning"}}, pref_lang="en")
pref_texts = mls.get_strings_pref_lang()
print(pref_texts)  # Expected Output: ['Hello', 'Good morning']
```

#### `get_strings_all`

Collects every text entry from every language present in the MultiLangString. This method offers a complete aggregation of the multilingual content, ideal for comprehensive data analysis or creating a full backup of the text data.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve all text entries
mls = MultiLangString({"en": {"Hello", "Good morning"}})
all_texts = mls.get_strings_all()
print(all_texts)  # Expected Output: ['Hello', 'Good morning']
```

#### `get_strings_langstring_lang`

Produces a list of formatted text entries for a specified language, with each entry followed by its language tag. This method is valuable for presenting or exporting language-specific data in a format that explicitly includes the language context.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve formatted text entries for a language
mls = MultiLangString({"en": {"Hello", "Good morning"}})
formatted_texts = mls.get_strings_langstring_lang("en")
print(formatted_texts)  # Expected Output: ['"Good morning"@en', '"Hello"@en']
```

#### `get_strings_langstring_pref_lang`

Generates a list of formatted text entries for the preferred language, each accompanied by the language tag. This method simplifies the process of accessing and displaying the default language content in a format that maintains language awareness.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve formatted text entries for the preferred language
mls = MultiLangString({"en": {"Hello", "Good morning"}}, pref_lang="en")
formatted_pref_texts = mls.get_strings_langstring_pref_lang()
print(formatted_pref_texts)  # Expected Output: ['"Hello"@en', '"Good morning"@en']
```

#### `get_strings_langstring_all`

Compiles a comprehensive list of all text entries from the MultiLangString, each formatted with its respective language tag. This method is ideal for creating detailed reports or exports where maintaining the association between text and language is crucial.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and retrieve all formatted text entries
mls = MultiLangString({"en": {"Hello", "Good morning"}})
all_formatted_texts = mls.get_strings_langstring_all()
print(all_formatted_texts)  # Expected Output: ['"Hello"@en', '"Good morning"@en']
```

#### `len_entries_all`

Calculates the total number of text entries across all languages within the MultiLangString. This method provides a quick way to assess the volume of multilingual content stored, useful for data management and analysis purposes.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and get the total number of entries
mls = MultiLangString({"en": {"Hello", "Good morning"}})
total_entries = mls.len_entries_all()
print(total_entries)  # Expected Output: 2
```

#### `len_entries_lang`

Determines the number of text entries associated with a specific language in the MultiLangString. This method is useful for evaluating the extent of content available in a particular language, aiding in language-specific content planning and analysis.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and get the number of entries for a language
mls = MultiLangString({"en": {"Hello", "Good morning"}})
num_entries = mls.len_entries_lang("en")
print(num_entries)  # Expected Output: 2
```

#### `len_langs`

Counts the number of distinct languages represented in the MultiLangString. This method is essential for understanding the linguistic diversity of the stored content, providing insights into the range of languages covered in the multilingual data.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and get the number of languages
mls = MultiLangString({"en": {"Hello", "Good morning"}})
num_languages = mls.len_langs()
print(num_languages)  # Expected Output: 1
```

#### `__repr__`

Provides a detailed and unambiguous string representation of the MultiLangString object, including its internal dictionary structure and the preferred language. This method is particularly useful for debugging and logging purposes, as it gives a clear snapshot of the object's current state, showing all its contents and configurations in a format that is helpful for developers.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and print its representation
mls = MultiLangString({"en": {"Hello", "Good morning"}})
print(mls.__repr__())  # Expected Output: MultiLangString({'en': {'Hello', 'Good morning'}}, pref_lang='en')
```

#### `__str__`

Generates a user-friendly string representation of the MultiLangString object, listing each text entry along with its associated language tag. This method is designed for readability and ease of understanding, making it suitable for displaying the multilingual content in a concise and clear format. It's particularly useful for user interfaces, reports, or any scenario where a straightforward overview of the multilingual data is needed.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and print it
mls = MultiLangString({"en": {"Hello", "Good morning"}})
print(mls)  # Expected Output: "Good morning"@en, "Hello"@en
# Adding new entry without language tag and printing the result
mls.add_entry("Olá")
print(mls)  # Expected Output: "Good morning"@en, "Hello"@en, Olá
```

#### `__eq__`

Determines whether two MultiLangString objects are equal by comparing their internal dictionaries (`mls_dict`). This method is crucial for assessing the equivalence of multilingual content, ignoring the preferred language settings. It ensures that two MultiLangString instances are considered equal only if they contain the same set of language strings, making it a vital tool for data comparison and deduplication processes.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Create two MultiLangString instances with the same content but different preferred languages
mls1 = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}}, pref_lang="en")
mls2 = MultiLangString({"en": {"Hello", "Good morning"}, "es": {"Hola", "Buenos días"}}, pref_lang="es")

# Despite having different preferred languages, they are considered equal because their content (mls_dict) is the same
print(mls1 == mls2)  # Expected Output: True

# Change the content of mls2
mls2.add_entry("Bonjour", "fr")

# Now mls1 and mls2 are not equal because their content differs
print(mls1 == mls2)  # Expected Output: False
```

#### `__hash__`

Computes a unique hash value for the MultiLangString object based on its internal dictionary of language strings. This method enables the use of MultiLangString instances in hash-based data structures like sets and dictionaries. By providing a consistent hash value, it ensures that MultiLangString objects can be efficiently used as keys or stored in collections that rely on hashing mechanisms.

Example:

```python
# Import necessary class
from langstring import MultiLangString

# Initialize MultiLangString and generate a hash value
mls = MultiLangString({"en": {"Hello", "Good morning"}})
print(hash(mls))  # Expected Output: (hash value, e.g., 3786478500744739392)
```

## Control and Flags

The Control and Flags system in the LangString Library plays a pivotal role in managing and configuring the behavior of `LangString` and `MultiLangString` instances.

This system operates at a global, class-level context, meaning that the flags and controls applied have a uniform effect across all instances of these classes. In other words, when a flag is set or reset using the control classes, it impacts every instance of `LangString` and `MultiLangString` throughout the application. This ensures consistent behavior and validation rules across all instances, as individual instances cannot have differing flag values.

In the following subsections, we will delve into the specifics of the available flags and the control methods. The flags define key aspects of how `LangString` and `MultiLangString` instances handle multilingual text, including validation rules and representation formats. Understanding these flags is crucial for effectively utilizing the library in various scenarios, especially those involving multilingual content.

The control methods, shared between `LangStringControl` and `MultiLangStringControl`, provide the mechanisms to set, retrieve, and reset these flags. These methods ensure that you can dynamically configure the behavior of the library to suit your application's needs. We will explore each method in detail, providing insights into their usage and impact on the library's functionality.

### Flags

The LangString and MultiLangString classes use a set of flags to control various aspects of their behavior. These flags are managed by `LangStringControl` and `MultiLangStringControl` respectively. The available flags and their effects are as follows:

#### `ENSURE_TEXT`
- **Description**: This flag ensures that the text provided to `LangString` or `MultiLangString` is not empty.
- **Effect**: When set to `True`, attempting to create a `LangString` or add an entry to `MultiLangString` with an empty string will raise a `ValueError`. This is useful for enforcing the presence of meaningful content.
- **Default Value**: `True`. By default, the library requires that text strings are not empty.


#### `ENSURE_ANY_LANG`
- **Description**: This flag mandates the presence of a language tag in `LangString` or `MultiLangString`.
- **Effect**: If `True`, a `ValueError` is raised when a `LangString` is created or an entry is added to `MultiLangString` without a language tag. This flag is beneficial for scenarios where language context is crucial.
- **Default Value**: `False`. By default, the library does not require a language tag to be present.


#### `ENSURE_VALID_LANG`
- **Description**: This flag ensures that the language tags used in `LangString` or `MultiLangString` are valid according to standard language codes (e.g., ISO 639-1).
- **Effect**: When enabled, creating a `LangString` or adding an entry to `MultiLangString` with an invalid language tag results in a `ValueError`. This flag is essential for maintaining consistency and accuracy in language-specific data.
- **Default Value**: `False`. By default, the library does not enforce the validity of language tags.

These flags provide a flexible way to customize the behavior of `LangString` and `MultiLangString` classes according to the specific needs of your application. By adjusting these flags, you can enforce different levels of validation and control over the language data being processed.

### Example Usage of Flags

```python
from langstring import LangString, LangStringControl, LangStringFlag

# Enabling the ENSURE_TEXT flag
LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

# Attempting to create a LangString with an empty string will now raise an error
try:
    lang_str = LangString("")
except ValueError as e:
    print(f"Error: {e}")  # Outputs an error message
```

These flags provide a flexible way to customize the behavior of `LangString` and `MultiLangString` classes according to the specific needs of your application. By adjusting these flags, you can enforce different levels of validation and control over the language data being processed.

### Control

The Control classes, namely `LangStringControl` and `MultiLangStringControl`, act as static managers for the flags. They provide methods to set, retrieve, and reset the states of these flags, ensuring consistent behavior across all instances of `LangString` and `MultiLangString`.

#### Control Methods

##### `set_flag`

The `set_flag` method is used to enable or disable a specific flag for either LangString or MultiLangString. This method allows for dynamic configuration of behavior, such as enforcing non-empty text or valid language tags.

Example:

- Enabling the ENSURE_TEXT flag for LangString:
  ```python
  LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
  ```
- Disabling the ENSURE_VALID_LANG flag for MultiLangString:
  ```python
  MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, False)
  ```

##### `get_flag`

The `get_flag` method retrieves the current state (enabled or disabled) of a specified flag. It is useful for checking the configuration status of LangString or MultiLangString instances.

Example:

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

##### `reset_flags`

The `reset_flags` method resets all flags to their default values. This is particularly useful for restoring the default behavior after temporary changes to the configuration flags.

Example:

- Resetting all flags for LangString:
  ```python
  LangStringControl.reset_flags()
  ```
- Resetting all flags for MultiLangString:
  ```python
  MultiLangStringControl.reset_flags()
  ```

##### `print_flags`

The `print_flags` method prints the current state of all configuration flags to the console. It is a convenient tool for debugging or monitoring the current flag settings.

Example:

- Printing all flags for LangString:
  ```python
  LangStringControl.print_flags()
  ```
- Printing all flags for MultiLangString:
  ```python
  MultiLangStringControl.print_flags()
  ```

This section provides an overview of the control and flag system in the LangString Library, including how to use the control classes and their methods to manage the behavior of LangString and MultiLangString instances. The examples illustrate practical use cases for these methods.

### LangString Control Examples

```python
from langstring import LangString, LangStringControl, LangStringFlag

# Example: Enabling the ENSURE_TEXT flag
LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

# Trying to create a LangString with an empty string (will raise ValueError due to ENSURE_TEXT)
try:
    empty_string_lang = LangString("")
except ValueError as e:
    print(f"Error: {e}")

# Checking if the ENSURE_TEXT flag is enabled
is_ensure_text_enabled = LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT)
print(f"ENSURE_TEXT flag is enabled: {is_ensure_text_enabled}")

# Resetting all flags to default
LangStringControl.reset_flags()
```

### MultiLangString Control Examples

```python
from langstring import MultiLangString, MultiLangStringControl, MultiLangStringFlag

# Example: Disabling the ENSURE_VALID_LANG flag
MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, False)

# Creating a MultiLangString instance with an invalid language code (no error due to flag being disabled)
mls = MultiLangString({"xx": {"Hello"}})
print(f"Created MultiLangString: {mls}")

# Checking the current state of the ENSURE_VALID_LANG flag
is_valid_lang_enforced = MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_VALID_LANG)
print(f"ENSURE_VALID_LANG flag is set to: {is_valid_lang_enforced}")

# Resetting all flags to default for MultiLangString
MultiLangStringControl.reset_flags()
```

## Code Testing

The code provided has undergone rigorous testing to ensure its reliability and correctness. The tests can be found in the 'tests' directory of the project. To run the tests, navigate to the project root directory and execute the following command:

```bash
langstring> pytest .\tests
```

## Version 2: Key Differences and Improvements

The LangString Library has undergone significant enhancements from Version 1 (V1) to Version 2 (V2). These changes have improved the library's functionality and usability, particularly in terms of control mechanisms and handling multilingual strings. Below are the key differences and improvements:

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
