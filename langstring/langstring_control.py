"""Module providing control flags for the LangString class behavior.

This module contains flags to control various aspects of LangString behavior, including text validation,
language validation, and verbose mode for detailed logging. It provides functions to set the state of these flags.

Constants:
 _ENSURE_TEXT (bool): Flag to ensure that a LangString 'text' field content is not empty. Default is False.
_ENSURE_ANY_LANG (bool): Flag to ensure that a LangString 'text' field content is not empty. Default is False.
_ENSURE_VALID_LANG (bool): Flag to ensure that a LangString 'text' field content is not empty and that it corresponds
to a valid language. Default is False.
_VERBOSE_MODE (bool): Flag to enable verbose mode for detailed logging. Default is False.
"""
_ENSURE_TEXT = False
_ENSURE_ANY_LANG = False
_ENSURE_VALID_LANG = False
_VERBOSE_MODE = False


def ls_ensure_text(state: bool) -> None:  # noqa (vulture)
    """Set the state of the ENSURE_TEXT flag.

    :param state: Desired state of the ENSURE_TEXT flag.
    :type state: bool
    """
    global _ENSURE_TEXT
    _ENSURE_TEXT = state


def ls_ensure_any_lang(state: bool) -> None:  # noqa (vulture)
    """Set the state of the ENSURE_ANY_LANG flag.

    :param state: Desired state of the ENSURE_ANY_LANG flag.
    :type state: bool
    """
    global _ENSURE_ANY_LANG
    _ENSURE_ANY_LANG = state


def ls_ensure_valid_lang(state: bool) -> None:  # noqa (vulture)
    """Set the state of the ENSURE_VALID_LANG flag.

    :param state: Desired state of the ENSURE_VALID_LANG flag.
    :type state: bool
    """
    global _ENSURE_VALID_LANG
    _ENSURE_VALID_LANG = state


def enable_verbose_mode(state: bool) -> None:  # noqa (vulture)
    """Enable or disable verbose mode.

    :param state: True to enable verbose mode, False to disable.
    :type state: bool
    """
    global _VERBOSE_MODE
    _VERBOSE_MODE = state


def ls_print_control_flags() -> None:  # noqa (vulture)
    """Print the current state of all control flags."""
    print(f"ENSURE_TEXT = {_ENSURE_TEXT}")
    print(f"ENSURE_ANY_LANG = {_ENSURE_ANY_LANG}")
    print(f"ENSURE_VALID_LANG = {_ENSURE_VALID_LANG}")
    print(f"VERBOSE_MODE = {_VERBOSE_MODE}")
