"""Define the control mechanism for the LangString class, providing a way to configure and manage its behavior.

The module consists of two main components: the LangStringFlag enumeration and the LangStringControl class. These
components work together to offer a flexible and robust way to control the behavior of LangString instances,
particularly in terms of validation and representation.

Classes:
    LangStringFlag (Enum): An enumeration that defines various flags for controlling the behavior of LangString
                           instances.
    LangStringControl (ControlBase): A control class responsible for managing the state of LangStringFlags across the
                                     application.

The LangStringFlag enumeration includes flags such as ENSURE_TEXT, ENSURE_ANY_LANG, and ENSURE_VALID_LANG, each serving
a specific purpose in controlling how LangString instances handle text and language tag validation. The VERBOSE_MODE
flag can be used for debugging or logging purposes, providing additional information during operations.

The LangStringControl class, inheriting from ControlBase, acts as a static configuration manager. It is designed to be
non-instantiable, emphasizing its role in managing global configuration states rather than being used as an object. This
class provides class methods to set and retrieve the states of LangStringFlags, ensuring consistent behavior across all
LangString instances. It plays a crucial role in the functioning of the ValidationBase methods by providing necessary
control settings.

Key Components:
    - LangStringFlag: Defines control flags for LangString behavior.
    - LangStringControl: Manages and retrieves the states of LangStringFlags.

Usage:
    The LangStringControl class can be used to enable or disable specific behaviors in LangString instances by setting
    the appropriate flags. For example, enabling the ENSURE_TEXT flag will enforce that all LangString instances have
    non-empty text.

Example:
    ```python
    from langstring_module import LangStringControl, LangStringFlag

    # Enabling the ENSURE_TEXT flag
    LangStringControl.set_flag(LangStringFlag.ENSURE_TEXT, True)

    # Retrieving the current state of the ENSURE_TEXT flag
    is_ensure_text_enabled = LangStringControl.get_flag(LangStringFlag.ENSURE_TEXT)
    ```

Note:
    The LangStringControl class should not be instantiated directly. Instead, its class methods should be used to
    interact with the control flags.
"""
from enum import auto
from enum import Enum

from utils.controls_base import ControlBase


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


class LangStringControl(ControlBase):
    """Control class for managing LangString configuration flags, designed to be non-instantiable.

    This class uses class methods to set and retrieve configuration flags for LangString behavior, ensuring a
    consistent global configuration state. It is made non-instantiable by using the NonInstantiable metaclass,
    emphasizing its role as a static configuration manager rather than an object to be instantiated.

    :cvar _flags: Stores the state of each LangStringFlag.
    :vartype _flags: dict[LangStringFlag, bool]
    """

    _flags = {
        LangStringFlag.ENSURE_TEXT: True,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
    }

    @classmethod
    def _get_flags_type(cls) -> type[LangStringFlag]:
        """Retrieve the control class and its corresponding flags enumeration used in the LangString class.

        This method provides the specific control class (LangStringControl) and the flags enumeration (LangStringFlag)
        that are used for configuring and validating the LangString instances. It is essential for the functioning of
        the ValidationBase methods, which rely on these control settings.

        :return: The LangStringFlag enumeration.
        :rtype: type[LangStringFlag]
        """
        return LangStringFlag
