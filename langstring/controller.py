from typing import Union

from .flags import GlobalFlag
from .flags import LangStringFlag
from .flags import MultiLangStringFlag
from .flags import SetLangStringFlag
from .utils.non_instantiable import NonInstantiable


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
    DEFAULT_FLAGS: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool] = {
        # Default values for GlobalFlags
        GlobalFlag.DEFINED_TEXT: False,
        GlobalFlag.DEFINED_LANG: False,
        GlobalFlag.VALID_LANG: False,
        GlobalFlag.STRIP_TEXT: False,
        GlobalFlag.STRIP_LANG: False,
        GlobalFlag.LOWERCASE_LANG: False,
        # Default values for LangStringFlags
        LangStringFlag.DEFINED_TEXT: False,
        LangStringFlag.DEFINED_LANG: False,
        LangStringFlag.VALID_LANG: False,
        LangStringFlag.STRIP_TEXT: False,
        LangStringFlag.STRIP_LANG: False,
        LangStringFlag.LOWERCASE_LANG: False,
        LangStringFlag.PRINT_WITH_QUOTES: True,
        LangStringFlag.PRINT_WITH_LANG: True,
        # Default values for SetLangStringFlags
        SetLangStringFlag.DEFINED_TEXT: False,
        SetLangStringFlag.DEFINED_LANG: False,
        SetLangStringFlag.VALID_LANG: False,
        SetLangStringFlag.STRIP_TEXT: False,
        SetLangStringFlag.STRIP_LANG: False,
        SetLangStringFlag.LOWERCASE_LANG: False,
        # Default values for MultiLangStringFlags
        MultiLangStringFlag.DEFINED_TEXT: False,
        MultiLangStringFlag.DEFINED_LANG: False,
        MultiLangStringFlag.VALID_LANG: False,
        MultiLangStringFlag.STRIP_TEXT: False,
        MultiLangStringFlag.STRIP_LANG: False,
        MultiLangStringFlag.LOWERCASE_LANG: False,
    }

    # Initialize the flags with the default values
    flags: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool] = DEFAULT_FLAGS.copy()

    @classmethod
    def set_flag(
        cls, flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], state: bool
    ) -> None:
        """Set the state of a specified configuration flag for LangString, SetLangString, or MultiLangString.

        If a GlobalFlag is set, it also sets the corresponding flags in LangStringFlag, SetLangStringFlag,
        and MultiLangStringFlag to the same state.

        :param flag: The flag to be set, either an instance of one of the flag enums.
        :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]
        :param state: Setting this to True or False will enable or disable the flag, respectively.
        :type state: bool
        :raises TypeError: If 'flag' is not an instance of one of the flag enums, or if 'state' is not a Boolean.
        """
        if not isinstance(state, bool):
            raise TypeError("Invalid state received. State must be a boolean new_text.")

        if not isinstance(flag, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)):
            raise TypeError(
                f"Invalid flag type. Expected LangStringFlag or MultiLangStringFlag, got '{type(flag).__name__}'."
            )

        if isinstance(flag, GlobalFlag):
            # Set the state for all flags that match the name of the global flag
            for key in cls.flags:
                if key.name == flag.name:
                    cls.flags[key] = state
        else:
            # Set the state for the specific flag
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
                f"Invalid flag type. Expected LangStringFlag or MultiLangStringFlag, got '{type(flag).__name__}'."
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

    @classmethod
    def reset_flags_type(
        cls, flag_type: type[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]]
    ) -> None:
        """Reset configuration flags of a specific type to their default values.

        This method resets only the flags of the specified type (e.g., LangStringFlag) to their default values.

        :param flag_type: The type of the flags to reset.
        :type flag_type: Type[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]]
        """
        if isinstance(flag_type, GlobalFlag):
            cls.reset_flags_all()
        else:
            for flag, default_value in cls.DEFAULT_FLAGS.items():
                if isinstance(flag, flag_type):
                    cls.flags[flag] = default_value
