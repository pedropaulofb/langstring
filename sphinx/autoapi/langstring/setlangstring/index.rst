langstring.setlangstring
========================

.. py:module:: langstring.setlangstring

.. autoapi-nested-parse::

   The setlangstring module provides the SetLangString class to encapsulate a set of strings with a common language tag.

   This module is designed to work with sets of text strings and their associated language tags, offering functionalities
   such as validation of language tags, handling of empty strings and language tags based on control flags. It optionally
   utilizes the langcodes library for validating language tags, enhancing the robustness of the language tag validation
   process.

   Control flags from the controller module are used to enforce certain behaviors like ensuring non-empty text and valid
   language tags. These flags can be set externally to alter the behavior of the SetLangString class.

   The SetLangString class aims to make user interaction as similar as possible to working with regular sets. To achieve
   this, many of the standard set methods have been overridden to return SetLangString objects, allowing seamless
   integration and extended functionality. Additionally, the class provides mechanisms for validating input types,
   matching language tags, and merging SetLangString objects.

   **Example**::

       # Create a SetLangString object
       set_lang_str = SetLangString({"Hello", "World"}, "en")

       # Print the set representation
       print(set_lang_str)  # Output: {'Hello', 'World'}@en

       # Add a new string
       set_lang_str.add("New String")
       print(set_lang_str)  # Output: {'Hello', 'New String', 'World'}@en

       # Remove a string
       set_lang_str.remove("World")
       print(set_lang_str)  # Output: {'Hello', 'New String'}@en

       # Check if a string is in the set
       contains_hello = "Hello" in set_lang_str
       print(contains_hello)  # Output: True

   Modules:
       controller: Provides control flags that influence the behavior of the SetLangString class.
       flags: Defines the SetLangStringFlag class with various control flags for the SetLangString class.
       langstring: Provides the LangString class used within the SetLangString class.
       utils.validators: Provides validation methods used within the SetLangString class.



Classes
-------

.. autoapisummary::

   langstring.setlangstring.SetLangString


Module Contents
---------------

.. py:class:: SetLangString(texts = None, lang = '')

   A class to encapsulate a set of strings with a common language tag.

   This class provides functionality to associate a set of text strings with a single language tag, offering methods
   for set representation, element addition, removal, and various set operations. The behavior of this class is
   influenced by control flags from the Controller class, which can enforce non-empty text, valid language tags,
   and other constraints.

   Many standard set methods are overridden to return SetLangString objects, allowing seamless integration and
   extended functionality. This design ensures that users can work with SetLangString instances similarly to
   regular sets.

   :ivar texts: The set of text strings.
   :vartype texts: set[str]
   :ivar lang: The language tag for the set of texts.
   :vartype lang: str
   :raises ValueError: If control flags enforce non-empty text and any text in the set is empty.
   :raises TypeError: If the types of parameters are incorrect based on validation.


   .. py:property:: texts
      :type: set[str]

      Get the set of text strings.

      :return: The set of text strings.
      :rtype: set[str]



   .. py:property:: lang
      :type: str

      Get the language tag.

      :return: The language tag.
      :rtype: str



   .. py:method:: add_langstring(langstring)

      Add a LangString object to the set of texts.

      This method validates the type and language of the LangString object and adds its text to the set.
      The behavior is influenced by control flags set in the Controller.

      :param langstring: The LangString object to add.
      :type langstring: LangString
      :raises TypeError: If the provided langstring is not of type LangString.
      :raises ValueError: If the control flags enforce valid language tags and the langstring's language tag is
                          invalid, or if the language tag of the langstring does not match the set's language tag.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello"}, "en")
          >>> lang_str = LangString("World", "en")
          >>> set_lang_str.add_langstring(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello', 'World'}@en



   .. py:method:: add_text(text)

      Add a text string to the set of texts.

      This method validates the type of the text string and adds it to the set.
      The behavior is influenced by control flags set in the Controller.

      :param text: The text string to add.
      :type text: str
      :raises TypeError: If the provided text is not of type str.
      :raises ValueError: If the control flags enforce non-empty text and the text string is empty.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello"}, "en")
          >>> set_lang_str.add_text("World")
          >>> print(set_lang_str)  # Output: {'Hello', 'World'}@en



   .. py:method:: discard_text(text)

      Discard a text string from the set of texts.

      This method removes the text string from the set if it is present. If the text string is not present,
      the set remains unchanged. The method does not raise an error if the text is not found.

      :param text: The text string to discard.
      :type text: str
      :raises TypeError: If the provided text is not of type str.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str.discard_text("World")
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> set_lang_str.discard_text("Python")
          >>> print(set_lang_str)  # Output: {'Hello'}@en



   .. py:method:: discard_langstring(langstring)

      Discard a LangString object from the set of texts.

      This method validates the type and language of the LangString object and removes its text from the set if it
      is present. If the text is not present, the set remains unchanged. The method does not raise an error if the
      text is not found.

      :param langstring: The LangString object to discard.
      :type langstring: LangString
      :raises TypeError: If the provided langstring is not of type LangString.
      :raises ValueError: If the language tag of the langstring does not match the set's language tag.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> lang_str = LangString("World", "en")
          >>> set_lang_str.discard_langstring(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> lang_str = LangString("Python", "en")
          >>> set_lang_str.discard_langstring(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello'}@en



   .. py:method:: remove_langstring(langstring)

      Remove a text string from the set of texts.

      This method removes the text string from the set. If the text string is not present, a KeyError is raised.

      :param text: The text string to remove.
      :type text: str
      :raises TypeError: If the provided text is not of type str.
      :raises KeyError: If the text string is not found in the set.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str.remove_text("World")
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> set_lang_str.remove_text("Python")  # Raises KeyError



   .. py:method:: remove_text(text)

      Remove a LangString object from the set of texts.

      This method validates the type and language of the LangString object and removes its text from the set. If the
      text is not present, a KeyError is raised.

      :param langstring: The LangString object to remove.
      :type langstring: LangString
      :raises TypeError: If the provided langstring is not of type LangString.
      :raises ValueError: If the language tag of the langstring does not match the set's language tag.
      :raises KeyError: If the text string is not found in the set.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> lang_str = LangString("World", "en")
          >>> set_lang_str.remove_langstring(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> lang_str = LangString("Python", "en")
          >>> set_lang_str.remove_langstring(lang_str)  # Raises KeyError



   .. py:method:: to_langstrings()

      Convert the set of texts to a list of LangString objects.

      This method creates a LangString object for each text in the set, associating it with the set's language tag.

      :return: A list of LangString objects.
      :rtype: list[LangString]

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> langstrings = set_lang_str.to_langstrings()
          >>> for lang_str in langstrings:
          ...     print(lang_str)
          ...
          # Output:
          # "Hello"@en
          # "World"en



   .. py:method:: to_strings(print_quotes = None, separator = '@', print_lang = None)

      Convert the set of texts to a list of formatted strings.

      Converts each text in the set to a formatted string, optionally including quotes and the language tag.
      The behavior is influenced by control flags set in the Controller.
      The resulting list of strings is sorted to generate a deterministic output.

      :param print_quotes: If True, wrap the text in quotes. If None, use the default setting from the Controller.
      :type print_quotes: Optional[bool]
      :param separator: The separator to use between the text and language tag.
      :type separator: str
      :param print_lang: If True, include the language tag. If None, use the default setting from the Controller.
      :type print_lang: Optional[bool]
      :return: A sorted list of formatted strings.
      :rtype: list[str]

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> strings = set_lang_str.to_strings()
          >>> for s in strings:
          ...     print(s)
          ...
          # Output:
          # "Hello"@en
          # "World"@en
          >>> strings = set_lang_str.to_strings(print_quotes=False, print_lang=False)
          >>> for s in strings:
          ...     print(s)
          ...
          # Output:
          # Hello
          # World



   .. py:method:: add(new_element)

      Add a new element to the set of texts.

      This method adds a new element, which can be a string or a LangString object, to the set. It mimics the behavior
      of the standard set's add method, allowing for seamless integration and extended functionality. The behavior is
      influenced by control flags set in the Controller.

      :param new_element: The element to add, either a text string or a LangString object.
      :type new_element: Union[str, LangString]
      :raises TypeError: If the provided new_element is neither a str nor a LangString.
      :raises ValueError: If the control flags enforce valid language tags and the new_element's language tag is
                          invalid, or if the language tag of the new_element does not match the set's language tag.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello"}, "en")
          >>> set_lang_str.add("World")
          >>> print(set_lang_str)  # Output: {'Hello', 'World'}@en
          >>> lang_str = LangString("New String", "en")
          >>> set_lang_str.add(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello', 'New String', 'World'}@en



   .. py:method:: clear()

      Remove all elements from the set of texts.

      This method clears all elements from the set, mimicking the behavior of the standard set's clear method,
      resulting in an empty set.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str.clear()
          >>> print(set_lang_str)  # Output: {}@en



   .. py:method:: copy()

      Create a shallow copy of the SetLangString.

      This method returns a new SetLangString object that is a shallow copy of the original, mimicking the behavior
      of the standard set's copy method.

      :return: A shallow copy of the SetLangString.
      :rtype: SetLangString

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> copied_set_lang_str = set_lang_str.copy()
          >>> print(copied_set_lang_str)  # Output: {'Hello', 'World'}@en



   .. py:method:: discard(element)

      Discard an element from the set of texts.

      This method removes the element from the set if it is present. If the element is not present, the set remains
      unchanged. It mimics the behavior of the standard set's discard method and does not raise an error if the
      element is not found.

      :param element: The element to discard, either a text string or a LangString object.
      :type element: Union[str, LangString]
      :raises TypeError: If the provided element is neither a str nor a LangString.
      :raises ValueError: If the language tag of the LangString does not match the set's language tag.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str.discard("World")
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> lang_str = LangString("Python", "en")
          >>> set_lang_str.discard(lang_str)
          >>> print(set_lang_str)  # Output: {'Hello'}@en



   .. py:method:: pop()

      Remove and return an arbitrary element from the set of texts.

      This method removes and returns an arbitrary element from the set, mimicking the behavior of the standard set's
      pop method. If the set is empty, a KeyError is raised.

      :return: An arbitrary element from the set.
      :rtype: str
      :raises KeyError: If the set is empty.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> element = set_lang_str.pop()
          >>> print(element)  # Output: 'Hello' or 'World'
          >>> print(set_lang_str)  # Output: {'World'}@en or {'Hello'}@en



   .. py:method:: remove(element)

      Remove an element from the set of texts.

      This method removes the specified element from the set. If the element is not present, a KeyError is raised.
      It mimics the behavior of the standard set's remove method.

      :param element: The element to remove, either a text string or a LangString object.
      :type element: Union[str, LangString]
      :raises TypeError: If the provided element is neither a str nor a LangString.
      :raises ValueError: If the language tag of the LangString does not match the set's language tag.
      :raises KeyError: If the element is not found in the set.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str.remove("World")
          >>> print(set_lang_str)  # Output: {'Hello'}@en
          >>> lang_str = LangString("Python", "en")
          >>> set_lang_str.remove(lang_str)  # Raises KeyError



   .. py:method:: difference(*others)

      Return the difference of the set and another set or sets.

      This method returns a new SetLangString containing elements that are in the set but not in the others. It
      mimics the behavior of the standard set's difference method.

      :param others: One or more sets or SetLangString objects to compute the difference with.
      :type others: Union[set[str], SetLangString]
      :return: A new SetLangString containing the difference of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> diff_set_lang_str = set_lang_str1.difference(set_lang_str2)
          >>> print(diff_set_lang_str)  # Output: {'Hello'}@en



   .. py:method:: difference_update(*others)

      Update the set, removing elements found in others.

      This method updates the set, removing all elements that are also in another set or sets. It mimics the behavior
      of the standard set's difference_update method.

      :param others: One or more sets or SetLangString objects to compute the difference with.
      :type others: Union[set[str], SetLangString]
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> set_lang_str1.difference_update(set_lang_str2)
          >>> print(set_lang_str1)  # Output: {'Hello'}@en



   .. py:method:: isdisjoint(other)

      Return True if the set has no elements in common with another set.

      This method checks if the set has no elements in common with another set or SetLangString,
      mimicking the behavior of the standard set's isdisjoint method.

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the sets are disjoint, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"Python", "Java"}, "en")
          >>> disjoint = set_lang_str1.isdisjoint(set_lang_str2)
          >>> print(disjoint)  # Output: True



   .. py:method:: issubset(other)

      Return True if the set is a subset of another set.

      This method checks if the set is a subset of another set or SetLangString, mimicking the behavior of the
      standard set's issubset method.

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a subset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello", "World"}, "en")
          >>> subset = set_lang_str1.issubset(set_lang_str2)
          >>> print(subset)  # Output: True



   .. py:method:: issuperset(other)

      Return True if the set is a superset of another set.

      This method checks if the set is a superset of another set or SetLangString, mimicking the behavior of the
      standard set's issuperset method.

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a superset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello"}, "en")
          >>> superset = set_lang_str1.issuperset(set_lang_str2)
          >>> print(superset)  # Output: True



   .. py:method:: intersection(*others)

      Return the intersection of the set and other sets.

      This method returns a new SetLangString containing elements that are common to the set and all of the others.
      It mimics the behavior of the standard set's intersection method.

      :param others: One or more sets or SetLangString objects to compute the intersection with.
      :type others: Union[set[str], SetLangString]
      :return: A new SetLangString containing the intersection of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> intersect_set_lang_str = set_lang_str1.intersection(set_lang_str2)
          >>> print(intersect_set_lang_str)  # Output: {'World'}@en



   .. py:method:: intersection_update(*others)

      Update the set, keeping only elements found in it and all others.

      This method updates the set, keeping only elements that are common to the set and all of the others. It mimics
      the behavior of the standard set's intersection_update method.

      :param others: One or more sets or SetLangString objects to compute the intersection with.
      :type others: Union[set[str], SetLangString]
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> set_lang_str1.intersection_update(set_lang_str2)
          >>> print(set_lang_str1)  # Output: {'World'}@en



   .. py:method:: symmetric_difference(other)

      Return the symmetric difference of the set and another set.

      This method returns a new SetLangString containing elements that are in either the set or the other set, but not
      in both. It mimics the behavior of the standard set's symmetric_difference method.

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: A new SetLangString containing the symmetric difference of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> sym_diff_set_lang_str = set_lang_str1.symmetric_difference(set_lang_str2)
          >>> print(sym_diff_set_lang_str)  # Output: {'Hello', 'Python'}@en



   .. py:method:: symmetric_difference_update(other)

      Update the set, keeping only elements found in either set, but not in both.

      This method updates the set, keeping only elements that are in either the set or the other set, but not in both.
      It mimics the behavior of the standard set's symmetric_difference_update method.

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> set_lang_str1.symmetric_difference_update(set_lang_str2)
          >>> print(set_lang_str1)  # Output: {'Hello', 'Python'}@en



   .. py:method:: union(*others)

      Return the union of the set and other sets.

      This method returns a new SetLangString containing all elements that are in the set, in others, or in both. It
      mimics the behavior of the standard set's union method.

      :param others: One or more sets or SetLangString objects to compute the union with.
      :type others: Union[set[str], SetLangString]
      :return: A new SetLangString containing the union of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"World"}, "en")
          >>> union_set_lang_str = set_lang_str1.union(set_lang_str2)
          >>> print(union_set_lang_str)  # Output: {'Hello', 'World'}@en



   .. py:method:: update(*others)

      Update the set, adding elements from all others.

      This method updates the set, adding all elements that are in others. It mimics the behavior of the standard
      set's update method.

      :param others: One or more sets or SetLangString objects to update the set with.
      :type others: Union[set[str], SetLangString]
      :raises ValueError: If the language tag of any SetLangString in others does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"World"}, "en")
          >>> set_lang_str1.update(set_lang_str2)
          >>> print(set_lang_str1)  # Output: {'Hello', 'World'}@en



   .. py:method:: __and__(other)

      Return the intersection of the set and another set.

      This method returns a new SetLangString containing elements that are common to the set and the other set. It
      mimics the behavior of the standard set's __and__ method (set intersection operator `&`).

      :param other: The other set or SetLangString to intersect with.
      :type other: Union[set[str], SetLangString]
      :return: A new SetLangString containing the intersection of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> intersect_set_lang_str = set_lang_str1 & set_lang_str2
          >>> print(intersect_set_lang_str)  # Output: {'World'}@en



   .. py:method:: __contains__(element)

      Return True if the set contains the specified element.

      This method checks if the specified element is in the set, mimicking the behavior of the standard set's
      __contains__ method (membership test operator `in`).

      :param element: The element to check for membership, either a text string or a LangString object.
      :type element: Union[str, LangString]
      :return: True if the element is in the set, False otherwise.
      :rtype: bool
      :raises TypeError: If the provided element is neither a str nor a LangString.
      :raises ValueError: If the language tag of the LangString does not match the set's language tag.

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> contains_hello = "Hello" in set_lang_str
          >>> print(contains_hello)  # Output: True
          >>> lang_str = LangString("Python", "en")
          >>> contains_python = lang_str in set_lang_str
          >>> print(contains_python)  # Output: False



   .. py:method:: __eq__(other)

      Return True if the set is equal to another set.

      This method checks if the set is equal to another SetLangString, mimicking the behavior of the standard set's
      __eq__ method (equality operator `==`).

      :param other: The other SetLangString to compare with.
      :type other: object
      :return: True if the sets are equal, False otherwise.
      :rtype: bool
      :raises NotImplementedError: If the other object is not a SetLangString.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Hello"}, "en")
          >>> is_equal = set_lang_str1 == set_lang_str2
          >>> print(is_equal)  # Output: True



   .. py:method:: __ge__(other)

      Return True if the set is a superset of another set.

      This method checks if the set is a superset of another set or SetLangString, mimicking the behavior of the
      standard set's __ge__ method (superset operator `>=`).

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a superset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello"}, "en")
          >>> is_superset = set_lang_str1 >= set_lang_str2
          >>> print(is_superset)  # Output: True



   .. py:method:: __gt__(other)

      Return True if the set is a proper superset of another set.

      This method checks if the set is a proper superset of another set or SetLangString, mimicking the behavior
      of the standard set's __gt__ method (proper superset operator `>`).

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a proper superset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello"}, "en")
          >>> is_proper_superset = set_lang_str1 > set_lang_str2
          >>> print(is_proper_superset)  # Output: True



   .. py:method:: __hash__()

      Generate a hash for a SetLangString object.

      This method generates a hash value for the SetLangString object, mimicking the behavior of the standard set's
      __hash__ method. The set of texts is converted to a frozenset for hashing, as sets are mutable and unhashable.

      :return: The hash value of the SetLangString object.
      :rtype: int

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> hash_value = hash(set_lang_str)
          >>> print(hash_value)  # Output: A unique integer representing the hash value



   .. py:method:: __iand__(other)

      Update the set, keeping only elements found in it and another set.

      This method updates the set, keeping only elements that are common to the set and the other set, mimicking the
      behavior of the standard set's __iand__ method (in-place intersection operator `&=`).

      :param other: The other set or SetLangString to intersect with.
      :type other: Union[set[str], SetLangString]
      :return: The updated SetLangString.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> set_lang_str1 &= set_lang_str2
          >>> print(set_lang_str1)  # Output: {'World'}@en



   .. py:method:: __ior__(other)

      Update the set, adding elements from another set.

      This method updates the set, adding all elements that are in the other set, mimicking the behavior of the
      standard set's __ior__ method (in-place union operator `|=`).

      :param other: The other set or SetLangString to union with.
      :type other: Union[set[str], SetLangString]
      :return: The updated SetLangString.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"World"}, "en")
          >>> set_lang_str1 |= set_lang_str2
          >>> print(set_lang_str1)  # Output: {'Hello', 'World'}@en



   .. py:method:: __isub__(other)

      Update the set, removing elements found in another set.

      This method updates the set, removing all elements that are also in the other set, mimicking the behavior of the
      standard set's __isub__ method (in-place difference operator `-=`).

      :param other: The other set or SetLangString to difference with.
      :type other: Union[set[str], SetLangString]
      :return: The updated SetLangString.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World"}, "en")
          >>> set_lang_str1 -= set_lang_str2
          >>> print(set_lang_str1)  # Output: {'Hello'}@en



   .. py:method:: __iter__()

      Return an iterator over the elements of the set.

      This method returns an iterator over the elements of the set, mimicking the behavior of the standard set's
      __iter__ method.

      :return: An iterator over the elements of the set.
      :rtype: Iterator[str]

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> for text in set_lang_str:
          ...     print(text)
          ...
          # Output: 'Hello'
          #         'World'



   .. py:method:: __ixor__(other)

      Update the set, keeping only elements found in either set, but not in both.

      This method updates the set, keeping only elements that are in either the set or the other set, but not in both,
      mimicking the behavior of the standard set's __ixor__ method (in-place symmetric difference operator `^=`).

      :param other: The other set or SetLangString to symmetric difference with.
      :type other: Union[set[str], SetLangString]
      :return: The updated SetLangString.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> set_lang_str1 ^= set_lang_str2
          >>> print(set_lang_str1)  # Output: {'Hello', 'Python'}@en



   .. py:method:: __le__(other)

      Return True if the set is a subset of another set.

      This method checks if the set is a subset of another set or SetLangString, mimicking the behavior of the
      standard set's __le__ method (subset operator `<=`).

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a subset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello", "World"}, "en")
          >>> is_subset = set_lang_str1 <= set_lang_str2
          >>> print(is_subset)  # Output: True



   .. py:method:: __len__()

      Return the number of elements in the set.

      This method returns the number of elements in the set,
      mimicking the behavior of the standard set's __len__ method.

      :return: The number of elements in the set.
      :rtype: int

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> length = len(set_lang_str)
          >>> print(length)  # Output: 2



   .. py:method:: __lt__(other)

      Return True if the set is a proper subset of another set.

      This method checks if the set is a proper subset of another set or SetLangString, mimicking the behavior of the
      standard set's __lt__ method (proper subset operator `<`).

      :param other: The other set or SetLangString to compare with.
      :type other: Union[set[str], SetLangString]
      :return: True if the set is a proper subset, False otherwise.
      :rtype: bool
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"Hello", "World"}, "en")
          >>> is_proper_subset = set_lang_str1 < set_lang_str2
          >>> print(is_proper_subset)  # Output: True



   .. py:method:: __or__(other)

      Return the union of the set and another set.

      This method returns a new SetLangString containing all elements that are in the set,
      in the other set, or in both. It mimics the behavior of the standard set's __or__ method (union operator `|`).

      :param other: The other set or SetLangString to union with.
      :type other: Union[set[str], SetLangString]
      :return: A new SetLangString containing the union of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello"}, "en")
          >>> set_lang_str2 = SetLangString({"World"}, "en")
          >>> union_set_lang_str = set_lang_str1 | set_lang_str2
          >>> print(union_set_lang_str)  # Output: {'Hello', 'World'}@en



   .. py:method:: __repr__()

      Return the official string representation of the SetLangString object.

      This method returns an official string representation of the SetLangString object, mimicking the behavior of the
      standard set's __repr__ method. This representation can be used for debugging and logging.

      :return: The official string representation of the SetLangString object.
      :rtype: str

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> repr_str = repr(set_lang_str)
          >>> print(repr_str)  # Output: SetLangString(texts={'Hello', 'World'}, lang='en')



   .. py:method:: __str__()

      Return the string representation of the SetLangString object.

      This method provides a concise string representation of the SetLangString, listing each text entry with its
      associated language tag if the corresponding flags are set. It mimics the behavior of the standard set's
      __str__ method.
      The method provide a deterministic output by sorting the elements before printing.

      :return: The string representation of the SetLangString object.
      :rtype: str

      **Example**::

          >>> set_lang_str = SetLangString({"Hello", "World"}, "en")
          >>> print(str(set_lang_str))  # Output: {'Hello', 'World'}@en



   .. py:method:: __sub__(other)

      Return the difference of the set and another set.

      This method returns a new SetLangString containing elements that are in the set but not in the other set. It
      mimics the behavior of the standard set's __sub__ method (difference operator `-`).

      :param other: The other set or SetLangString to difference with.
      :type other: Union[set[str], SetLangString]
      :return: A new SetLangString containing the difference of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> diff_set_lang_str = set_lang_str1 - set_lang_str2
          >>> print(diff_set_lang_str)  # Output: {'Hello'}@en



   .. py:method:: __xor__(other)

      Return the symmetric difference of the set and another set.

      This method returns a new SetLangString containing elements that are in either the set or the other set, but not
      in both. It mimics the behavior of the standard set's __xor__ method (symmetric difference operator `^`).

      :param other: The other set or SetLangString to symmetric difference with.
      :type other: Union[set[str], SetLangString]
      :return: A new SetLangString containing the symmetric difference of the sets.
      :rtype: SetLangString
      :raises ValueError: If the language tag of the SetLangString in other does not match the set's language tag.

      **Example**::

          >>> set_lang_str1 = SetLangString({"Hello", "World"}, "en")
          >>> set_lang_str2 = SetLangString({"World", "Python"}, "en")
          >>> sym_diff_set_lang_str = set_lang_str1 ^ set_lang_str2
          >>> print(sym_diff_set_lang_str)  # Output: {'Hello', 'Python'}@en



   .. py:method:: merge_setlangstrings(setlangstrings)
      :staticmethod:


      Merge duplicated SetLangStrings based on their language tags using the union method.

      This method processes a list of SetLangString instances, identifying and merging duplicates based on their
      language tags.
      If there's no case variation in the language tags among duplicates, the original casing is preserved.
      If case variations are found, the casefolded version of the language tag is used in the merged SetLangString.

      :param setlangstrings: The list of SetLangString instances to be merged.
      :type setlangstrings: list[SetLangString]
      :return: A list of merged SetLangString instances without duplicates.
      :rtype: list[SetLangString]
      :raises TypeError: If the input is not a list of SetLangString instances.

      **Example**::

          >>> setlangstr1 = SetLangString({"Hello"}, "en")
          >>> setlangstr2 = SetLangString({"World"}, "en")
          >>> setlangstr3 = SetLangString({"Bonjour"}, "fr")
          >>> setlangstr4 = SetLangString({"Hello"}, "EN")
          >>> merged_list = SetLangString.merge_setlangstrings([setlangstr1, setlangstr2, setlangstr3, setlangstr4])
          >>> for s in merged_list:
          ...     print(s)
          ...
          # Output: {'Hello', 'World'}@en
          #         {'Bonjour'}@fr



