"""This package contains modules related to handling language-specific strings using the LangString and \
MultiLangString classes."""
from .langstring import LangString  # noqa:F401 (flake8)
from .multilangstring import MultiLangString  # noqa:F401 (flake8)
from .control_flags import LangStringFlag, LangStringControl

__all__ = [
    "LangString",
    "MultiLangString",
    "LangStringFlag",
    "LangStringControl"
]
