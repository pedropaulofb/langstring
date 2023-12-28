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
