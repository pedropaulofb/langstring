from enum import auto
from enum import Enum


class GlobalFlag(Enum):
    """Enumeration for global control flags.

    This enum defines various flags that can be used to configure the behavior of all classes.

    :cvar DEFINED_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of all classes.
    :vartype DEFINED_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of all classes.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar VALID_LANG: Makes mandatory the use of a valid language code string for all classes' field 'lang'.
    :vartype VALID_LANG: Enum
    """

    DEFINED_TEXT = auto()
    DEFINED_LANG = auto()
    STRIP_TEXT = auto()
    STRIP_LANG = auto()
    LOWERCASE_LANG = auto()
    VALID_LANG = auto()


class LangStringFlag(Enum):
    """Enumeration for LangString control flags.

    This enum defines various flags that can be used to configure the behavior of the LangString class.

    :cvar DEFINED_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of a LangString.
    :vartype DEFINED_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of a LangString.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar VALID_LANG: Makes mandatory the use of a valid language code string for the LangString's field 'lang'.
    :vartype VALID_LANG: Enum
    """

    DEFINED_TEXT = auto()
    DEFINED_LANG = auto()
    STRIP_TEXT = auto()
    STRIP_LANG = auto()
    LOWERCASE_LANG = auto()
    VALID_LANG = auto()
    PRINT_WITH_QUOTES = auto()
    PRINT_WITH_LANG = auto()


class SetLangStringFlag(Enum):
    """Enumeration for SetLangString control flags.

    This enum defines various flags that can be used to configure the behavior of the SetLangString class.

    :cvar DEFINED_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of a SetLangString.
    :vartype DEFINED_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of a SetLangString.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar VALID_LANG: Makes mandatory the use of a valid language code string for the SetLangString's field 'lang'.
    :vartype VALID_LANG: Enum
    """

    DEFINED_TEXT = auto()
    DEFINED_LANG = auto()
    STRIP_TEXT = auto()
    STRIP_LANG = auto()
    LOWERCASE_LANG = auto()
    VALID_LANG = auto()


class MultiLangStringFlag(Enum):
    """Enumeration for MultiLangString control flags.

    This enum defines various flags that can be used to configure the behavior of the MultiLangString class.

    :cvar DEFINED_TEXT: Makes mandatory the use of a non-empty string for the field 'text' of a MultiLangString.
    :vartype DEFINED_TEXT: Enum
    :cvar ENSURE_ANY_LANG: Makes mandatory the use of a non-empty string for the field 'lang' of a MultiLangString.
    :vartype ENSURE_ANY_LANG: Enum
    :cvar VALID_LANG: Makes mandatory the use of a valid language code string for the MultiLangString's field 'lang'.
    :vartype VALID_LANG: Enum
    """

    # Applied to both lang and pref_lang attributes.

    DEFINED_TEXT = auto()
    DEFINED_LANG = auto()
    STRIP_TEXT = auto()
    STRIP_LANG = auto()
    LOWERCASE_LANG = auto()
    VALID_LANG = auto()
