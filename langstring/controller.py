from typing import Optional
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
        GlobalFlag.DEFINED_LANG: False,
        GlobalFlag.DEFINED_TEXT: False,
        GlobalFlag.ENFORCE_EXTRA_DEPEND: False,
        GlobalFlag.LOWERCASE_LANG: False,
        GlobalFlag.METHODS_MATCH_TYPES: False,
        GlobalFlag.PRINT_WITH_LANG: True,
        GlobalFlag.PRINT_WITH_QUOTES: True,
        GlobalFlag.STRIP_LANG: False,
        GlobalFlag.STRIP_TEXT: False,
        GlobalFlag.VALID_LANG: False,
        # Default values for LangStringFlags
        LangStringFlag.DEFINED_LANG: False,
        LangStringFlag.DEFINED_TEXT: False,
        LangStringFlag.LOWERCASE_LANG: False,
        LangStringFlag.METHODS_MATCH_TYPES: False,
        LangStringFlag.PRINT_WITH_LANG: True,
        LangStringFlag.PRINT_WITH_QUOTES: True,
        LangStringFlag.STRIP_LANG: False,
        LangStringFlag.STRIP_TEXT: False,
        LangStringFlag.VALID_LANG: False,
        # Default values for SetLangStringFlags
        SetLangStringFlag.DEFINED_LANG: False,
        SetLangStringFlag.DEFINED_TEXT: False,
        SetLangStringFlag.LOWERCASE_LANG: False,
        SetLangStringFlag.METHODS_MATCH_TYPES: False,
        SetLangStringFlag.PRINT_WITH_LANG: True,
        SetLangStringFlag.PRINT_WITH_QUOTES: True,
        SetLangStringFlag.STRIP_LANG: False,
        SetLangStringFlag.STRIP_TEXT: False,
        SetLangStringFlag.VALID_LANG: False,
        # Default values for MultiLangStringFlags
        MultiLangStringFlag.DEFINED_LANG: False,
        MultiLangStringFlag.DEFINED_TEXT: False,
        MultiLangStringFlag.LOWERCASE_LANG: False,
        MultiLangStringFlag.STRIP_LANG: False,
        MultiLangStringFlag.STRIP_TEXT: False,
        MultiLangStringFlag.VALID_LANG: False,
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
                f"Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag, "
                f"got '{type(flag).__name__}'."
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
        """Retrieve the current state of a specified configuration flag.

        Available for GlobalFlag, LangString, SetLangString, or MultiLangString.

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
                f"Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag, "
                f"got '{type(flag).__name__}'."
            )

        return cls.flags.get(flag, False)

    @classmethod
    def get_flags(cls) -> dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]:
        """Retrieve the current state of all configuration flags.

        Available for GlobalFlag, LangString, SetLangString, or MultiLangString.

        This class method provides a way to access the states of all flags globally for both LangString and
        MultiLangString classes. It returns a copy of the flags dictionary, ensuring that the original data is not
        modified.

        :return: A dictionary mapping each flag to its boolean state, either for LangStringFlag or MultiLangStringFlag.
        :rtype: dict[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag], bool]
        """
        return cls.flags.copy()

    @classmethod
    def print_flag(cls, flag: type[Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]]) -> None:
        """Print the current state of a specific configuration flag.

        This class method prints the state of the specified flag to the console. It is useful for checking the state of
        an individual flag for LangString, SetLangString, MultiLangString, or GlobalFlag.

        :param flag: The flag whose state is to be printed.
        :type flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]

        Note:
            This method is typically used for debugging or quick monitoring, to display the state of a specific flag.
        """
        if not isinstance(flag, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)):
            raise TypeError(
                f"Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag, "
                f"got '{type(flag).__name__}'."
            )

        flag_state = cls.flags.get(flag, False)
        print(f"{flag.__class__.__name__}.{flag.name} = {flag_state}")

    @classmethod
    def print_flags(cls, flag_type: Optional[type] = None) -> None:
        """
        Print the current state of configuration flags in alphabetical order.

        If a flag type is specified, only flags of that type are printed.
        If no flag type is specified, all flags are printed.

        :param flag_type: The type of flags to print (e.g., GlobalFlag, LangStringFlag).
                          If None, all flags are printed.
        :type flag_type: Optional[Type]
        """
        if flag_type:
            if not isinstance(flag_type, type):
                raise TypeError(f"Invalid flag type. Expected a class type, got '{type(flag_type).__name__}'.")
            if not issubclass(flag_type, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)):
                raise TypeError(
                    f"Invalid flag type. "
                    f"Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag, "
                    f"got '{flag_type.__name__}'."
                )

        sorted_flags = sorted(cls.flags.items(), key=lambda item: item[0].__class__.__name__ + "." + item[0].name)
        for flag, state in sorted_flags:
            if flag_type is None or isinstance(flag, flag_type):
                print(f"{flag.__class__.__name__}.{flag.name} = {state}")

    @classmethod
    def reset_flag(cls, flag: Union[GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag]) -> None:
        """Reset a specific flag to its default value.

        If the flag is of type GlobalFlag, reset all equivalent flags of other types.
        E.g., reset_flag(GlobalFlag.VALID_TEXT) will reset GlobalFlag.VALID_TEXT,
        LangStringFlag.VALID_TEXT, SetLangStringFlag.VALID_TEXT, and MultiLangStringFlag.VALID_TEXT.
        """
        all_flag_types = (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)

        if not isinstance(flag, all_flag_types):
            raise TypeError(
                f"Invalid flag. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, "
                f"or MultiLangStringFlag, but got {type(flag).__name__}."
            )

        if isinstance(flag, GlobalFlag):
            flag_name = flag.name
            for flag_type in all_flag_types:
                # Check if the flag_type has an attribute with the name of the GlobalFlag
                if hasattr(flag_type, flag_name):
                    # Access the specific member of the flag_type using its name
                    matching_flag = getattr(flag_type, flag_name)
                    cls.flags[matching_flag] = cls.DEFAULT_FLAGS[matching_flag]
        else:
            cls.flags[flag] = cls.DEFAULT_FLAGS[flag]

    @classmethod
    def reset_flags(cls, flag_type: Optional[type] = GlobalFlag) -> None:
        """Reset all flags of a specific type to their default values."""
        if flag_type is not None and not isinstance(flag_type, type):
            raise TypeError("Invalid flag type. Expected a class type.")

        if not flag_type or not issubclass(
            flag_type, (GlobalFlag, LangStringFlag, SetLangStringFlag, MultiLangStringFlag)
        ):
            raise TypeError(
                "Invalid flag type. Expected GlobalFlag, LangStringFlag, SetLangStringFlag, or MultiLangStringFlag."
            )

        if flag_type == GlobalFlag:
            cls.flags = cls.DEFAULT_FLAGS.copy()
        else:
            for flag, default_value in cls.DEFAULT_FLAGS.items():
                if isinstance(flag, flag_type):
                    cls.flags[flag] = default_value
