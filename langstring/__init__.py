"""The langstring package provides classes and utilities for handling multilingual text.

It includes classes for single and multiple language strings, along with their control and validation mechanisms.
"""

from .controller import Controller
from .converter import Converter
from .flags import GlobalFlag
from .flags import LangStringFlag
from .flags import MultiLangStringFlag
from .flags import SetLangStringFlag
from .langstring import LangString
from .multilangstring import MultiLangString
from .setlangstring import SetLangString

__all__ = [
    "LangString",
    "SetLangString",
    "MultiLangString",
    "Controller",
    "GlobalFlag",
    "LangStringFlag",
    "SetLangStringFlag",
    "MultiLangStringFlag",
    "Converter",
]
