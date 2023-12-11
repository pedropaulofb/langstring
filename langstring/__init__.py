"""This package contains modules related to handling language-specific strings using the LangString and \
MultiLangString classes."""
from .langstring import LangString  # noqa:F401 (flake8)
from .langstring_control import LangStringControl
from .langstring_control import LangStringFlag
from .multilangstring import MultiLangString  # noqa:F401 (flake8)

__all__ = ["LangString", "MultiLangString", "LangStringFlag", "LangStringControl"]
