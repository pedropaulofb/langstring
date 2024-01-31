"""Define the foundational structure for managing configuration flags in LangString and MultiLangString classes.

Overview:
---------
The module introduces a metaclass, `NonInstantiable`, to prevent instantiation of certain classes, and a base class,
`ControlBase`, which serves as a template for managing configuration flags in LangString and MultiLangString classes.
These flags are crucial for controlling various behaviors and features of LangString and MultiLangString instances,
enabling flexible and dynamic configuration.

Classes:
- NonInstantiable: A metaclass used to create classes that are intended to serve as static utility containers or
  namespaces, rather than as entities for instantiation. This is particularly useful for defining classes that
  encapsulate static methods and class variables.

- ControlBase: An abstract base class designed to be the foundation for LangStringControl and MultiLangStringControl.
  It provides abstract and concrete class methods for managing configuration flags, ensuring consistent and global
  configuration across LangString and MultiLangString instances. As a non-instantiable class, it underscores its role
  as a static manager rather than an object-oriented entity.

Key Features:
- Unified Flag Management: Offers a centralized approach to control configuration flags for both LangString and
  MultiLangString, ensuring uniformity and consistency in behavior.
- Extensibility and Flexibility: The abstract method `_get_flags_type` in `ControlBase` allows subclasses to define
  their own flag enumeration types, catering to specific configuration needs.
- Debugging and Monitoring Tools: Methods like `print_flags` and `get_flags` in `ControlBase` provide essential tools
  for debugging and monitoring the current state of configuration flags, aiding in development and troubleshooting.

Usage:
This module is integral to systems where LangString and MultiLangString classes are used, requiring dynamic
configuration and behavior modification. It is particularly beneficial in environments where global settings for
these classes need to be programmatically adjusted or inspected.

Note:
The module is structured with the expectation that it will be extended by concrete implementations for LangString and
MultiLangString classes, which will define their specific sets of flags and associated behaviors.

Example:
    # Setting a flag in LangStringControl
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

    # Resetting all flags to default in MultiLangStringControl
    MultiLangStringControl.reset_flags()
"""

from abc import abstractmethod
from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    from ..langstring_control import LangStringFlag
    from ..multilangstring_control import MultiLangStringFlag


class NonInstantiable(type):
    """A metaclass that prevents the instantiation of any class that uses it.

    When a class is defined with NonInstantiable as its metaclass, any attempt to instantiate that class will result
    in a TypeError. This is useful for creating classes that are meant to be used as namespaces or containers for
    static methods and class variables, without the intention of creating instances.

    Methods:
        __call__: Overrides the default call behavior to prevent instantiation.
    """

    def __call__(cls) -> None:
        """Override the default call behavior to prevent instantiation of the class.

        When this method is called, it raises a TypeError, effectively preventing the creation of an instance of the
        class that uses NonInstantiable as its metaclass.

        :raises TypeError: Always, to indicate that the class cannot be instantiated.
        """
        raise TypeError(f"{cls.__name__} class cannot be instantiated.")


class ControlBase(metaclass=NonInstantiable):
    """Base class for LangStringControl and MultiLangStringControl, providing common flag management functionalities.

    This class serves as a base for both LangStringControl and MultiLangStringControl, offering methods to manage
    configuration flags that affect the behavior of LangString and MultiLangString instances. It is designed to be
    non-instantiable, acting as a utility class for flag management.

    The class uses an "abstract" class variable `_flags` to store the state of each configuration flag. Subclasses are
    expected to initialize this variable with a dictionary mapping flag types to their boolean states. This design
    allows for a flexible yet consistent approach to managing configuration flags across different classes.

    :cvar _flags: An "abstract" class variable that stores the state of each configuration flag.
    :vartype _flags: dict[Union[type[LangStringFlag], type[MultiLangStringFlag]], bool]
    """

    # "Abstract" variable: must be implemented by ControlBase's subclasses
    _flags: dict[Union["LangStringFlag", "MultiLangStringFlag"], bool] = {}

    @classmethod
    @abstractmethod
    def _get_flags_type(cls) -> type[Union["LangStringFlag", "MultiLangStringFlag"]]:
        """Retrieve the type of the enumeration used for configuration flags.

        This abstract method should be implemented in subclasses to return the specific enumeration type
        used for managing configuration flags for either LangString or MultiLangString.

        :return: The type of the enumeration used for flags, either LangStringFlag or MultiLangStringFlag.
        :rtype: type["LangStringFlag", "MultiLangStringFlag"]
        """

    @classmethod
    def set_flag(cls, flag: Union["LangStringFlag", "MultiLangStringFlag"], state: bool) -> None:
        """Set the state of a specified configuration flag for LangString or MultiLangString.

        This class method allows setting the state of a flag globally, affecting the behavior of both LangString and
        MultiLangString instances. It is used to configure aspects of these classes that are controlled by the flags
        defined in LangStringFlag and MultiLangStringFlag enums.

        :param flag: The flag to be set, either an instance of LangStringFlag or MultiLangStringFlag.
        :type flag: Union[LangStringFlag, MultiLangStringFlag]
        :param state: Setting this to True or False will enable or disable the flag, respectively.
        :type state: bool
        :raises TypeError: If 'flag' is not an instance of LangStringFlag or MultiLangStringFlag,
        or if 'state' is not a Boolean.
        """
        flags = cls._get_flags_type()

        if not isinstance(state, bool):
            raise TypeError("Invalid state received. State must be a boolean value.")

        if not any(flag == member for member in flags.__members__.values()):
            raise TypeError(f"Invalid flag {flag} received. Valid flags are members of {flags.__name__}.")

        cls._flags[flag] = state

    @classmethod
    def get_flag(cls, flag: Union["LangStringFlag", "MultiLangStringFlag"]) -> bool:
        """Retrieve the current state of a specified configuration flag for LangString or MultiLangString.

        This class method provides a way to access the state of a flag globally for both LangString and
        MultiLangString classes.

        :param flag: The flag whose state is to be retrieved,
        either an instance of LangStringFlag or MultiLangStringFlag.
        :type flag: Union[LangStringFlag, MultiLangStringFlag]
        :return: The current state of the flag.
        :rtype: bool
        :raises TypeError: If 'flag' is not a member of LangStringFlag or MultiLangStringFlag.
        """
        flags = cls._get_flags_type()

        if not any(flag == member for member in flags.__members__.values()):
            raise TypeError(f"Invalid flag {flag} received. Valid flags are members of {flags.__name__}.")

        return cls._flags.get(flag, False)

    @classmethod
    def get_flags(cls) -> dict[Union["LangStringFlag", "MultiLangStringFlag"], bool]:
        """Retrieve the current state of all configuration flags for LangString or MultiLangString.

        This class method provides a way to access the states of all flags globally for both LangString and
        MultiLangString classes. It returns a copy of the flags dictionary, ensuring that the original data is not
        modified.

        :return: A dictionary mapping each flag to its boolean state, either for LangStringFlag or MultiLangStringFlag.
        :rtype: dict[Union[LangStringFlag, MultiLangStringFlag], bool]
        """
        return cls._flags.copy()

    @classmethod
    def print_flags(cls) -> None:
        """Print the current state of all configuration flags for LangString or MultiLangString.

        This class method prints the state of each flag in the _flags dictionary to the console. It provides a quick
        way to view the current configuration settings for both LangString and MultiLangString classes.

        Note:
            This method is typically used for debugging or quick monitoring purposes to display the current flag info.
        """
        flags = cls._get_flags_type()
        for flag, state in cls._flags.items():
            print(f"{flags.__name__}.{flag.name} = {state}")

    @classmethod
    def reset_flags(cls) -> None:
        """Reset all configuration flags for LangString or MultiLangString to their default values.

        This class method resets the states of all flags to their default values. This is particularly useful for
        restoring the default behavior of the LangString and MultiLangString classes after temporary changes to the
        configuration flags.

        Note:
            After calling this method, all flags will be set to their default state, as defined in the respective
            flag enums. Flags are managed globally.
        """
        flags = cls._get_flags_type()
        cls._flags = {
            flags.ENSURE_TEXT: True,
            flags.ENSURE_ANY_LANG: False,
            flags.ENSURE_VALID_LANG: False,
        }
