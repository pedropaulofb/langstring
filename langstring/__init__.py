"""This package contains modules related to handling language-specific strings using the LangString and \
MultiLangString classes."""

from .langstring import LangString  # noqa:F401 (flake8)
from .langstring_control import ls_print_control_flags, ls_ensure_any_lang, ls_ensure_valid_lang, ls_ensure_text, \
    ls_enable_verbose_mode
from .multilangstring import MultiLangString  # noqa:F401 (flake8)

__all__ = ['LangString', 'MultiLangString', 'ls_print_control_flags', 'ls_ensure_any_lang', 'ls_ensure_valid_lang',
           'ls_ensure_text', 'ls_enable_verbose_mode']
