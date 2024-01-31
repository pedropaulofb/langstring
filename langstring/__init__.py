"""The langstring package provides classes and utilities for handling multilingual text.

It includes classes for single and multiple language strings, along with their control and validation mechanisms.
"""

from .langstring import LangString
from .langstring_control import LangStringControl
from .langstring_control import LangStringFlag
from .multilangstring import MultiLangString
from .multilangstring_control import MultiLangStringControl
from .multilangstring_control import MultiLangStringFlag

__all__ = [
    "LangString",
    "MultiLangString",
    "LangStringFlag",
    "LangStringControl",
    "MultiLangStringFlag",
    "MultiLangStringControl",
]
