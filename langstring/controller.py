from typing import Union

from .flags import GlobalFlag
from .flags import LangStringFlag
from .flags import MultiLangStringFlag
from .flags import SetLangStringFlag


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


class Controller(metaclass=NonInstantiable):
    """Control class for managing configuration flags, designed to be non-instantiable.

    This class uses class methods to set and retrieve configuration flags for language classes' behavior, ensuring a
    consistent global configuration state. It is made non-instantiable by using the NonInstantiable metaclass,
    emphasizing its role as a static configuration manager rather than an object to be instantiated.

    :cvar DEFAULT_FLAGS: The default state of each flag.
    :vartype DEFAULT_FLAGS: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]
    :cvar flags: Stores the current state of each flag.
    :vartype flags: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]
    """
    # Define the default values as a class-level constant
    DEFAULT_FLAGS = {  # type: ignore
        # Default values for GlobalFlags
        GlobalFlag.ENSURE_TEXT: True,
        GlobalFlag.ENSURE_VALID_LANG: False,
        GlobalFlag.ENSURE_STRIP_TEXT: False,
        GlobalFlag.ENSURE_STRIP_LANG: False,
        GlobalFlag.ENSURE_LOWER_LANG: False,
        # Default values for LangStringFlags
        LangStringFlag.ENSURE_TEXT: True,
        LangStringFlag.ENSURE_VALID_LANG: False,
        LangStringFlag.ENSURE_STRIP_TEXT: False,
        LangStringFlag.ENSURE_STRIP_LANG: False,
        LangStringFlag.ENSURE_LOWER_LANG: False,
        # Default values for SetLangStringFlags
        SetLangStringFlag.ENSURE_TEXT: True,
        SetLangStringFlag.ENSURE_VALID_LANG: False,
        SetLangStringFlag.ENSURE_STRIP_TEXT: False,
        SetLangStringFlag.ENSURE_STRIP_LANG: False,
        SetLangStringFlag.ENSURE_LOWER_LANG: False,
        # Default values for MultiLangStringFlags
        MultiLangStringFlag.ENSURE_TEXT: True,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
        MultiLangStringFlag.ENSURE_STRIP_TEXT: False,
        MultiLangStringFlag.ENSURE_STRIP_LANG: False,
        MultiLangStringFlag.ENSURE_LOWER_LANG: False,
    }

    # TODO (@pedropaulofb): GlobalFlag behavior still to be implemented.

    # Initialize the flags with the default values
    flags: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool] = DEFAULT_FLAGS.copy()

    @classmethod
    def set_flag(
        cls, flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], state: bool
    ) -> None:
        """Set the state of a specified configuration flag for LangString, SetLangString, or MultiLangString.

        This class method allows setting the state of a flag globally, affecting the behavior of LangString,
        SetLangString, and MultiLangString instances. It is used to configure aspects of these classes that are
        controlled by the flags defined in the respective flag enums.

        :param flag: The flag to be set, either an instance of one of the flag enums.
        :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
        :param state: Setting this to True or False will enable or disable the flag, respectively.
        :type state: bool
        :raises TypeError: If 'flag' is not an instance of one of the flag enums, or if 'state' is not a Boolean.
        """
        if not isinstance(state, bool):
            raise TypeError("Invalid state received. State must be a boolean value.")

        if not isinstance(flag, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)):
            raise TypeError(
                f"Invalid flag type. Expected LangStringFlag or MultiLangStringFlag, got {type(flag).__name__}."
            )

        cls.flags[flag] = state

    @classmethod
    def get_flag(cls, flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]) -> bool:
        """Retrieve the current state of a specified configuration flag for LangString or MultiLangString.

        This class method provides a way to access the state of a flag globally for both LangString and
        MultiLangString classes.

        :param flag: The flag whose state is to be retrieved,
        either an instance of LangStringFlag or MultiLangStringFlag.
        :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
        :return: The current state of the flag.
        :rtype: bool
        :raises TypeError: If 'flag' is not a member of LangStringFlag or MultiLangStringFlag.
        """

        if not isinstance(flag, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)):
            raise TypeError(
                f"Invalid flag type. Expected LangStringFlag or MultiLangStringFlag, got {type(flag).__name__}."
            )

        return cls.flags.get(flag, False)

    @classmethod
    def get_flags(cls) -> dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]:
        """Retrieve the current state of all configuration flags for LangString or MultiLangString.

        This class method provides a way to access the states of all flags globally for both LangString and
        MultiLangString classes. It returns a copy of the flags dictionary, ensuring that the original data is not
        modified.

        :return: A dictionary mapping each flag to its boolean state, either for LangStringFlag or MultiLangStringFlag.
        :rtype: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]
        """
        return cls.flags.copy()

    @classmethod
    def print_flags(cls) -> None:
        """Print the current state of all configuration flags for LangString or MultiLangString.

        This class method prints the state of each flag in the flags dictionary to the console. It provides a quick
        way to view the current configuration settings for both LangString and MultiLangString classes.

        Note:
            This method is typically used for debugging or quick monitoring purposes to display the current flag info.
        """
        for flag, state in cls.flags.items():
            flag_class_name = flag.__class__.__name__
            print(f"{flag_class_name}.{flag.name} = {state}")

    @classmethod
    def reset_flags_all(cls) -> None:
        """Reset all configuration flags for LangString or MultiLangString to their default values.

        This class method resets the states of all flags to their default values. This is particularly useful for
        restoring the default behavior of the LangString and MultiLangString classes after temporary changes to the
        configuration flags.

        Note:
            After calling this method, all flags will be set to their default state, as defined in the respective
            flag enums. Flags are managed globally.
        """

        cls.flags = cls.DEFAULT_FLAGS.copy()
