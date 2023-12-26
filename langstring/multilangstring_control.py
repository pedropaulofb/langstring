"""This module provides tools for managing global control strategies in handling multilingual strings.

It defines an enumeration `MultiLangStringStrategy` for specifying different control strategies and a control class
`MultiLangStringControl` for setting and retrieving these strategies at a global level. The module is designed to
offer a centralized way to manage how duplicate language tags are handled across all instances of a class that
manages multilingual strings.

The `MultiLangStringStrategy` enumeration includes strategies like OVERWRITE, ALLOW, BLOCK_WARN, and BLOCK_ERROR,
each dictating a different approach to handling duplicate language tags in multilingual string instances.

The `MultiLangStringControl` class provides class methods to set, retrieve, log, and reset the global control strategy
and configuration flags. This allows for a consistent and centralized management of control strategies and flags,
which is particularly useful in applications where consistent handling of multilingual strings is critical.

The module utilizes the `loguru` library for logging and the `icecream` library for debugging purposes, enhancing
the development and maintenance experience.

Example Usage:
    # Set a global control strategy
    MultiLangStringControl.set_strategy(MultiLangStringStrategy.BLOCK_WARN)

    # Retrieve the current global control strategy
    current_strategy = MultiLangStringControl.get_strategy()

    # Reset to the default global control strategy
    MultiLangStringControl.reset_strategy()

    # Set a configuration flag
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, True)

    # Retrieve the current state of a specific flag
    flag_state = MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_TEXT)

    # Log the current state of all flags
    MultiLangStringControl.log_flags()

    # Reset all flags to their default states
    MultiLangStringControl.reset_flags()

Classes:
    MultiLangStringStrategy (Enum): Defines control strategies for handling duplicate language tags.
    MultiLangStringControl: Manages the global control strategy and configuration flags for handling duplicate
                            language tags.

Note:
    Changes made using `MultiLangStringControl` affect the behavior of multilingual string handling globally
    within the application and are intended to be used where consistent behavior across all instances is required.
"""

from enum import Enum
from enum import auto

from loguru import logger


class MultiLangStringFlag(Enum):
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

class MultiLangStringStrategy(Enum):
    """Enumeration for control strategies in MultiLangString.

    This enum defines the control strategies used for handling duplicate language tags in a MultiLangString instance.
    Each member of this enum represents a specific strategy for managing duplicates.

    :cvar OVERWRITE: Overwrites existing entries with the same language tag.
    :cvar ALLOW: Allows multiple entries with the same language tag, preventing duplication of identical texts.
    :cvar BLOCK_WARN: Blocks and logs a warning for duplicate language tags.
    :cvar BLOCK_ERROR: Block and raises an error for duplicate language tags.
    """

    OVERWRITE = auto()
    ALLOW = auto()
    BLOCK_WARN = auto()
    BLOCK_ERROR = auto()

    def __str__(self) -> str:
        """Return the string representation of the enum member.

        Overrides the default string representation to return the name of the enum member, making it more readable
        and suitable for user-facing contexts.

        :return: The name of the enum member.
        :rtype: str
        """
        return self.name


class MultiLangStringControl:
    """Control class for managing the global control strategy of MultiLangString instances.

    This class uses class methods and class variables to set and retrieve the global control strategy for handling
    duplicate language tags in MultiLangString instances.

    :cvar _strategy: The global control strategy for all MultiLangString instances.
    :vartype _global_control: MultiLangStringStrategy
    :cvar _flags: Dictionary holding the state of configuration flags for LangString.
    :vartype _flags: Dict[MultiLangStringFlag, bool]
    """

    _strategy = MultiLangStringStrategy.ALLOW

    _flags = {
        MultiLangStringFlag.ENSURE_TEXT: False,
        MultiLangStringFlag.ENSURE_ANY_LANG: False,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
        MultiLangStringFlag.VERBOSE_MODE: False,
    }

    @classmethod
    def set_flag(cls, flag: MultiLangStringFlag, state: bool) -> None:
        """Set the state of a specified configuration flag.

        This class method allows setting the state of a flag globally for the LangString class.

        :param flag: The MultiLangStringFlag to be set.
        :type flag: MultiLangStringFlag
        :param state: Setting this to True or False will enable or disable the flag, respectively.
        :type state: bool
        :raises TypeError: If an invalid 'MultiLangStringFlag' is provided or if 'state' is not a Boolean.
        """
        if not isinstance(state, bool):
            raise TypeError("Invalid state received. State must be a boolean value.")

        if not isinstance(flag, MultiLangStringFlag):
            valid_flags = ", ".join(f"MultiLangStringFlag.{f.name}" for f in MultiLangStringFlag)
            raise TypeError(f"Invalid flag received. Valid flags are: {valid_flags}.")

        cls._flags[flag] = state

    @classmethod
    def get_flag(cls, flag: MultiLangStringFlag) -> bool:
        """Retrieve the current state of a specified configuration flag.

        This class method provides a way to access the state of a flag globally for the LangString class.

        :param flag: The MultiLangStringFlag whose state is to be retrieved.
        :type flag: MultiLangStringFlag
        :return: The current state of the flag.
        :rtype: bool
        :raises TypeError: If an invalid MultiLangStringFlag is provided.
        """
        if not isinstance(flag, MultiLangStringFlag):
            valid_flags = ", ".join(f"MultiLangStringFlag.{f.name}" for f in MultiLangStringFlag)
            raise TypeError(f"Invalid flag received. Valid flags are: {valid_flags}.")

        return cls._flags.get(flag, False)

    @classmethod
    def get_flags(cls) -> dict[MultiLangStringFlag, bool]:
        """Retrieve the current state of all configuration flags.

        This class method provides a way to access the states of all flags globally for the LangString class.
        It returns a copy of the flags dictionary, ensuring that the original data is not modified.

        :return: A dictionary mapping each MultiLangStringFlag to its boolean state.
        :rtype: Dict[MultiLangStringFlag, bool]
        """
        return cls._flags.copy()

    @classmethod
    def log_flags(cls) -> None:
        """Log the current state of all configuration flags.

        This class method uses the loguru logger to log the state of each flag in the _flags dictionary.
        """
        for flag, state in cls._flags.items():
            logger.info(f"{flag.name} = {state}")

    @classmethod
    def reset_flags(cls) -> None:
        """Reset all configuration flags for LangString to their default values.

        This class method resets the states of all flags in the LangStringControl to their default values. This is
        particularly useful for restoring the default behavior of the LangString class after temporary changes to
        the configuration flags.

        After calling this method, all flags will be set to False, which is their default state. This includes flags
        for ensuring text presence, validating language codes, and enabling verbose mode.

        :example:
            # Change and then reset the flags
            LangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, True)
            LangStringControl.reset_flags()  # Resets ENSURE_TEXT and all other flags to False

        Note:
            This reset affects all instances where LangString flags are checked, as the flags are managed globally.
        """
        cls._flags = {
            MultiLangStringFlag.ENSURE_TEXT: False,
            MultiLangStringFlag.ENSURE_ANY_LANG: False,
            MultiLangStringFlag.ENSURE_VALID_LANG: False,
            MultiLangStringFlag.VERBOSE_MODE: False,
        }

    @classmethod
    def set_strategy(cls, control: MultiLangStringStrategy) -> None:
        """Set the global control strategy for all MultiLangString instances.

        :param control: The control strategy to be set globally.
        :type control: MultiLangStringStrategy
        :raises TypeError: If an invalid MultiLangStringStrategy is provided.
        """
        if not isinstance(control, MultiLangStringStrategy):
            valid_controls = ", ".join(f"MultiLangStringStrategy.{c.name}" for c in MultiLangStringStrategy)
            raise TypeError(f"Invalid control received. Valid controls are: {valid_controls}.")

        cls._strategy = control

    @classmethod
    def get_strategy(cls) -> MultiLangStringStrategy:
        """Retrieve the current global control strategy for MultiLangString instances.

        :return: The current global control strategy.
        :rtype: MultiLangStringStrategy
        """
        return cls._strategy

    @classmethod
    def log_strategy(cls) -> None:
        """Log the current global control strategy for MultiLangString instances.

        This class method uses the loguru logger to log the current global control strategy.
        """
        logger.info(f"Global MultiLangString control strategy: {cls._strategy}")

    @classmethod
    def reset_strategy(cls) -> None:
        """Reset the global control strategy for MultiLangString instances to the default value.

        This class method resets the global control strategy to `MultiLangStringStrategy.ALLOW`, which is the default
        behavior for handling duplicate language tags in MultiLangString instances. This can be useful for restoring
        default behavior after temporary changes to the global strategy.

        :example:
            # Set a new global strategy
            MultiLangStringControl.set_strategy(MultiLangStringStrategy.BLOCK_ERROR)

            # Reset to the default strategy
            MultiLangStringControl.reset_strategy()
        """
        cls._strategy = MultiLangStringStrategy.ALLOW
