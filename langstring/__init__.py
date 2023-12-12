"""This package contains modules related to handling language-specific strings using the LangString and \
MultiLangString classes."""
from .langstring import LangString
from .langstring_control import LangStringControl
from .langstring_control import LangStringFlag
from .multilangstring import MultiLangString

__all__ = ["LangString", "MultiLangString", "LangStringFlag", "LangStringControl"]
