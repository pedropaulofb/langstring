"""This module provides tools for managing global control strategies in handling multilingual strings.

It defines an enumeration `MultiLangStringStrategy` for specifying different control strategies and a control class
`MultiLangStringControl` for setting and retrieving these strategies at a global level. The module is designed to
offer a centralized way to manage how duplicate language tags are handled across all instances of a class that
manages multilingual strings.

The `MultiLangStringStrategy` enumeration includes strategies like OVERWRITE, ALLOW, BLOCK_WARN, and BLOCK_ERROR,
each dictating a different approach to handling duplicate language tags in multilingual string instances.

The `MultiLangStringControl` class provides class methods to set, retrieve, log, and reset the global control strategy.
This allows for a consistent and centralized management of control strategies, which is particularly useful in
applications where consistent handling of multilingual strings is critical.

The module utilizes the `loguru` library for logging and the `icecream` library for debugging purposes, enhancing
the development and maintenance experience.

Example Usage:
    # Set a global control strategy
    MultiLangStringControl.set_strategy(MultiLangStringStrategy.BLOCK_WARN)

    # Retrieve the current global control strategy
    current_strategy = MultiLangStringControl.get_strategy()

    # Reset to the default global control strategy
    MultiLangStringControl.reset_strategy()

Classes:
    MultiLangStringStrategy (Enum): Defines control strategies for handling duplicate language tags.
    MultiLangStringControl: Manages the global control strategy for handling duplicate language tags.

Note:
    Changes made using `MultiLangStringControl` affect the behavior of multilingual string handling globally
    within the application and are intended to be used where consistent behavior across all instances is required.
"""


from enum import Enum, auto

from loguru import logger


class MultiLangStringStrategy(Enum):
    """Enumeration for control strategies in MultiLangString.

    This enum defines the control strategies used for handling duplicate language tags in a MultiLangString instance.
    Each member of this enum represents a specific strategy for managing duplicates.

    :cvar OVERWRITE: Enum member to overwrite existing entries with the same language tag.
    :cvar ALLOW: Enum member to allow multiple entries with the same language tag, preventing duplication of identical texts.
    :cvar BLOCK_WARN: Enum member to block and log a warning for duplicate language tags.
    :cvar BLOCK_ERROR: Enum member to block and raise an error for duplicate language tags.
    """

    OVERWRITE = auto()
    ALLOW = auto()
    BLOCK_WARN = auto()
    BLOCK_ERROR = auto()

    def __str__(self) -> None:
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
    """

    _strategy = MultiLangStringStrategy.ALLOW

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
