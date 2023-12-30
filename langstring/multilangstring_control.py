"""This module defines the MultiLangStringFlag enumeration and MultiLangStringControl class.

These classes are used for managing configuration flags related to the behavior of MultiLangString instances.

The MultiLangStringFlag enumeration contains flags that influence how MultiLangString objects handle multilingual text,
such as ensuring non-empty text or valid language codes. The MultiLangStringControl class, inheriting from ControlBase,
provides methods to set, retrieve, and manage these flags globally, ensuring consistent behavior across all instances
of MultiLangString.

Classes:
    MultiLangStringFlag: An enumeration defining flags for configuring MultiLangString behavior.
    MultiLangStringControl: A control class for managing MultiLangString configuration flags.

Usage:
    The MultiLangStringControl class is used to set and retrieve the state of configuration flags defined in
    MultiLangStringFlag. These flags determine how MultiLangString instances validate and handle multilingual text data.

Example:
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, True)
    if MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_TEXT):
        print("ENSURE_TEXT flag is enabled.")

Note:
    The MultiLangStringControl class is designed to be non-instantiable and acts as a static configuration manager.
    It should not be instantiated but used through its class methods.
"""
from enum import auto
from enum import Enum

from .utils.controls_base import ControlBase


class MultiLangStringFlag(Enum):
    """Enumeration for LangString control flags.

    This enum defines various flags that can be used to configure the behavior of the LangString class.

    :cvar ENSURE_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of a LangString.
    :vartype ENSURE_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of a LangString.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar ENSURE_VALID_LANG: Makes mandatory the use of a valid language code string for the LangString's field 'lang'.
    :vartype ENSURE_VALID_LANG: Enum
    """

    ENSURE_TEXT = auto()
    ENSURE_ANY_LANG = auto()
    ENSURE_VALID_LANG = auto()


class MultiLangStringControl(ControlBase):
    """A control class for managing the configuration flags of MultiLangString instances.

    Inherits from ControlBase and utilizes a static approach to manage global settings that influence the behavior
    of MultiLangString objects. This class is non-instantiable and operates through class methods to ensure a
    consistent configuration state across all MultiLangString instances.

    The class manages flags defined in the MultiLangStringFlag enumeration, allowing for dynamic control over
    various aspects of MultiLangString behavior, such as text validation and language code enforcement.

    Usage:
        MultiLangStringControl is used to configure global settings for MultiLangString instances. It affects how
        these instances validate and process multilingual text data based on the set flags.

    Example:
        MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_VALID_LANG, True)
        is_valid_lang_enforced = MultiLangStringControl.get_flag(MultiLangStringFlag.ENSURE_VALID_LANG)
        print(f"ENSURE_VALID_LANG flag is set to {is_valid_lang_enforced}.")

    Note:
        As a static configuration manager, MultiLangStringControl should not be instantiated. It is designed to
        provide a centralized way to manage settings for all MultiLangString instances.

    :cvar _flags: A class-level dictionary storing the state of each configuration flag for MultiLangString instances.
    :vartype _flags: dict[MultiLangStringFlag, bool]
    """

    _flags = {
        MultiLangStringFlag.ENSURE_TEXT: True,
        MultiLangStringFlag.ENSURE_ANY_LANG: False,
        MultiLangStringFlag.ENSURE_VALID_LANG: False,
    }

    @classmethod
    def _get_flags_type(cls) -> type[MultiLangStringFlag]:
        """Retrieve the control class and its corresponding flags enumeration used in the LangString class.

        This method provides the specific control class (LangStringControl) and the flags enumeration (LangStringFlag)
        that are used for configuring and validating the LangString instances. It is essential for the functioning of
        the ValidationBase methods, which rely on these control settings.

        :return: The LangStringFlag enumeration.
        :rtype: type[MultiLangStringFlag]
        """
        return MultiLangStringFlag
