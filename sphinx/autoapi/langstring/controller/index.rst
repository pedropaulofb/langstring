langstring.controller
=====================

.. py:module:: langstring.controller

.. autoapi-nested-parse::

   The `controller` module provides the `Controller` class.

   This class is a non-instantiable class designed to manage and manipulate configuration flags for the `LangString`,
   `SetLangString`, and `MultiLangString` classes.

   This module defines the `Controller` class, which offers class methods to set, retrieve, print, and reset configuration
   flags. These flags influence the behavior and validation rules of the multilingual text handling classes within the
   application. By centralizing flag management, the `Controller` ensures consistent configuration and behavior across
   the system.

   Key Features:
       - **Global Configuration**: The `Controller` manages flags globally, allowing uniform behavior across different
         multilingual text classes.
       - **Non-Instantiable Design**: The `Controller` class uses the `NonInstantiable` metaclass to prevent instantiation,
         emphasizing its role as a static configuration manager.
       - **Flexible Flag Management**: Methods are provided to set, retrieve, print, and reset individual or all flags,
         enabling dynamic configuration during runtime.

   Enums Utilized:
       - **GlobalFlag**: Flags affecting the behavior of all classes.
       - **LangStringFlag**: Flags specific to the `LangString` class.
       - **SetLangStringFlag**: Flags specific to the `SetLangString` class.
       - **MultiLangStringFlag**: Flags specific to the `MultiLangString` class.

   The `Controller` class ensures that the multilingual text handling classes adhere to specified rules and constraints,
   enhancing the robustness and reliability of multilingual content management.



Classes
-------

.. autoapisummary::

   langstring.controller.Controller


Module Contents
---------------

.. py:class:: Controller

   Control class for managing configuration flags, designed to be non-instantiable.

   This class uses class methods to set and retrieve configuration flags for the behavior of the `LangString`,
   `SetLangString`, and `MultiLangString` classes, ensuring a consistent global configuration state. It is made
   non-instantiable by using the `NonInstantiable` metaclass, emphasizing its role as a static configuration manager
   rather than an object to be instantiated.

   :cvar _DEFAULT_FLAGS: The default state of each flag.
   :vartype DEFAULT_FLAGS: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]
   :cvar flags: Stores the current state of each flag.
   :vartype flags: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]

   **Example**::

       Set a flag:
       >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)

       Get a flag:
       >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))
       # Output: True

       Reset a flag to its default value:
       >>> Controller.reset_flag(GlobalFlag.LOWERCASE_LANG)
       >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))
       # Output: False

       Print the state of a specific flag:
       >>> Controller.print_flag(GlobalFlag.LOWERCASE_LANG)
       # Output: GlobalFlag.LOWERCASE_LANG = False

       Print the states of all flags:
       >>> Controller.print_flags()
       # Output: (Output of all flags with their states)

       Reset all flags to their default values:
       >>> Controller.reset_flags()
       >>> Controller.print_flags()
       # Output: (Output of all flags reset to their default states)


   .. py:attribute:: flags
      :type:  dict[Union[langstring.flags.GlobalFlag, langstring.flags.LangStringFlag, langstring.flags.SetLangStringFlag, langstring.flags.MultiLangStringFlag], bool]


   .. py:method:: set_flag(flag, state)
      :classmethod:


      Set the state of a specified configuration flag for LangString, SetLangString, or MultiLangString.

      If a GlobalFlag is set, it also sets the corresponding flags in LangStringFlag, SetLangStringFlag,
      and MultiLangStringFlag to the same state.

      :param flag: The flag to be set, either an instance of one of the flag enums.
      :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
      :param state: Setting this to True or False will enable or disable the flag, respectively.
      :type state: bool
      :raises TypeError: If 'flag' is not an instance of one of the flag enums, or if 'state' is not a boolean.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))  # Output: True



   .. py:method:: get_flag(flag)
      :classmethod:


      Retrieve the current state of a specified configuration flag.

      Available for GlobalFlag, LangString, SetLangString, or MultiLangString.

      This class method provides a way to access the state of a flag globally for LangString, SetLangString,
      and MultiLangString classes.

      :param flag: The flag whose state is to be retrieved, either an instance of GlobalFlag, LangStringFlag,
                   SetLangStringFlag, or MultiLangStringFlag.
      :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
      :return: The current state of the flag.
      :rtype: bool
      :raises TypeError: If 'flag' is not a member of GlobalFlag, LangStringFlag, SetLangStringFlag,
                         or MultiLangStringFlag.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))  # Output: True



   .. py:method:: get_flags()
      :classmethod:


      Retrieve the current state of all configuration flags.

      This class method provides a way to access the states of all flags globally for LangString, SetLangString,
      and MultiLangString classes.
      It returns a copy of the flags dictionary, ensuring that the original data is not modified.

      :return: A dictionary mapping each flag to its boolean state.
      :rtype: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> flags = Controller.get_flags()
          >>> print(flags[GlobalFlag.LOWERCASE_LANG])  # Output: True



   .. py:method:: print_flag(flag)
      :classmethod:


      Print the current state of a specific configuration flag.

      This class method prints the state of the specified flag to the console. It is useful for checking the state
      of an individual flag for LangString, SetLangString, MultiLangString, or GlobalFlag.

      :param flag: The flag whose state is to be printed.
      :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
      :raises TypeError: If 'flag' is not an instance of one of the flag enums.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> Controller.print_flag(GlobalFlag.LOWERCASE_LANG)  # Output: GlobalFlag.LOWERCASE_LANG = True



   .. py:method:: print_flags(flag_type = None)
      :classmethod:


      Print the current state of configuration flags in alphabetical order.

      If a flag type is specified, only flags of that type are printed.
      If no flag type is specified, all flags are printed.

      :param flag_type: The type of flags to print (e.g., GlobalFlag, LangStringFlag). If None, all flags are printed.
      :type flag_type: Optional[type]
      :raises TypeError: If 'flag_type' is not a valid flag type.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> Controller.print_flags()
          # Output: Prints all flags and their current state.



   .. py:method:: reset_flag(flag)
      :classmethod:


      Reset a specific flag to its default value.

      If the flag is of type GlobalFlag, reset all equivalent flags of other types.
      For example, reset_flag(GlobalFlag.VALID_TEXT) will reset GlobalFlag.VALID_TEXT, LangStringFlag.VALID_TEXT,
      SetLangStringFlag.VALID_TEXT, and MultiLangStringFlag.VALID_TEXT.

      :param flag: The flag to be reset.
      :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
      :raises TypeError: If 'flag' is not an instance of one of the flag enums.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> Controller.reset_flag(GlobalFlag.LOWERCASE_LANG)
          >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))  # Output: False



   .. py:method:: reset_flags(flag_type = GlobalFlag)
      :classmethod:


      Reset all flags of a specific type to their default values.

      :param flag_type: The type of flags to reset (e.g., GlobalFlag, LangStringFlag). If None, all flags are reset.
      :type flag_type: Optional[type]
      :raises TypeError: If 'flag_type' is not a valid flag type.

      **Example**::

          >>> Controller.set_flag(GlobalFlag.LOWERCASE_LANG, True)
          >>> Controller.reset_flags(GlobalFlag)
          >>> print(Controller.get_flag(GlobalFlag.LOWERCASE_LANG))  # Output: False



