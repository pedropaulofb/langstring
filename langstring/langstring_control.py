"""Module for controlling and managing language string settings.

This module provides classes and methods to manage configuration settings for language strings, including a control
class and an enumeration of configuration flags. It is designed for dynamic setting and accessing of language string
properties like text validation and language code verification.

The module also imports and utilizes the NonInstantiable metaclass from the control_metaclass module to ensure that
the LangStringControl class remains non-instantiable, aligning with its intended use as a static configuration manager.

Classes:
    LangStringFlag (Enum): An enumeration defining various configuration flags for language string settings.
    LangStringControl: A control class for managing the state of LangString configuration flags.

The LangStringFlag enumeration includes flags for ensuring text presence, validating language codes, and enabling
verbose mode. The LangStringControl class uses class methods and variables to set and retrieve these flags,
allowing for a global configuration state that persists throughout the application's runtime.

Classes:
    LangStringFlag (Enum): Defines configuration flags for language string settings.
    LangStringControl (NonInstantiable): Manages the state of LangString configuration flags.

Example:
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
    if LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT):
        # Actions based on the ENSURE_TEXT flag

This module utilizes the loguru library for logging flag states, offering an easy way to track configuration changes.

Note:
    This module is part of a larger library focused on language string processing and manipulation. Settings changed
    via LangStringControl will affect the LangString class behavior globally and can be modified at runtime.

"""
from enum import auto
from enum import Enum

from loguru import logger
from utils.control_metaclass import NonInstantiable


class LangStringFlag(Enum):
    """Enumeration for LangString control flags.

    This enum defines various flags that can be used to configure the behavior of the LangString class.

    :cvar ENSURE_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of a LangString.
    :vartype ENSURE_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of a LangString.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar ENSURE_VALID_LANG: Makes mandatory the use of a valid language code string for the LangString's field 'lang'.
    :vartype ENSURE_VALID_LANG: Enum
    :cvar VERBOSE_MODE: Enables verbose mode for additional information during operations.
    :vartype VERBOSE_MODE: Enum
    """

    ENSURE_TEXT = auto()
    ENSURE_ANY_LANG = auto()
    ENSURE_VALID_LANG = auto()
    VERBOSE_MODE = auto()


class LangStringControl(metaclass=NonInstantiable):
    """Control class for managing LangString configuration flags, designed to be non-instantiable.

    This class uses class methods to set and retrieve configuration flags for LangString behavior, ensuring a
    consistent global configuration state. It is made non-instantiable by using the NonInstantiable metaclass,
    emphasizing its role as a static configuration manager rather than an object to be instantiated.

    :cvar _flags: Stores the state of each LangStringFlag.
    :vartype _flags: dict[LangStringFlag, bool]
    """

    _flags = {
        LangStringFlag.ENSURE_TEXT: False,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
        LangStringFlag.VERBOSE_MODE: False,
    }

    @classmethod
    def set_flag(cls, flag: LangStringFlag, state: bool) -> None:
        """Set the state of a specified configuration flag.

        This class method allows setting the state of a flag globally for the LangString class.

        :param flag: The LangStringFlag to be set.
        :type flag: LangStringFlag
        :param state: True or False to enable or disable the flag, respectively.
        :type state: bool
        :raises TypeError: If an invalid LangStringFlag is provided or if 'state' is not a boolean.
        """
        if not isinstance(state, bool):
            raise TypeError("Invalid state received. State must be a boolean value.")

        if not isinstance(flag, LangStringFlag):
            valid_flags = ", ".join(f"LangStringFlag.{f.name}" for f in LangStringFlag)
            raise TypeError(f"Invalid flag received. Valid flags are: {valid_flags}.")

        cls._flags[flag] = state

    @classmethod
    def get_flag(cls, flag: LangStringFlag) -> bool:
        """Retrieve the current state of a specified configuration flag.

        This class method provides a way to access the state of a flag globally for the LangString class.

        :param flag: The LangStringFlag whose state is to be retrieved.
        :type flag: LangStringFlag
        :return: The current state of the flag.
        :rtype: bool
        :raises TypeError: If an invalid LangStringFlag is provided.
        """
        if not isinstance(flag, LangStringFlag):
            valid_flags = ", ".join(f"LangStringFlag.{f.name}" for f in LangStringFlag)
            raise TypeError(f"Invalid flag received. Valid flags are: {valid_flags}.")

        return cls._flags.get(flag, False)

    @classmethod
    def get_flags(cls) -> dict[LangStringFlag, bool]:
        """Retrieve the current state of all configuration flags.

        This class method provides a way to access the states of all flags globally for the LangString class.
        It returns a copy of the flags dictionary, ensuring that the original data is not modified.

        :return: A dictionary with LangStringFlag as keys and their boolean states as values.
        :rtype: dict[LangStringFlag, bool]
        """
        return cls._flags.copy()

    @classmethod
    def log_flags(cls) -> None:
        """Log the current state of all configuration flags using the loguru logger."""
        for flag, state in cls._flags.items():
            logger.info(f"{flag.name} = {state}")

    @classmethod
    def reset_flags(cls) -> None:
        """Reset all configuration flags for LangString to their default values.

        This class method resets the states of all flags in the LangStringControl to their default values. This is
        particularly useful for restoring the default behavior of the LangString class after temporary changes to
        the configuration flags. After calling this method, all flags will be set to False, their default state.

        :example:
            # Change and then reset the flags
            LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)
            LangStringControl.reset_flags()  # Resets ENSURE_TEXT and all other flags to False

        Note:
            This reset affects all instances where LangString flags are checked, as the flags are managed globally.
        """
        cls._flags = {
            LangStringFlag.ENSURE_TEXT: False,
            LangStringFlag.ENSURE_ANY_LANG: False,
            LangStringFlag.ENSURE_VALID_LANG: False,
            LangStringFlag.VERBOSE_MODE: False,
        }
