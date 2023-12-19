"""This module contains pytest fixtures and configurations used across various test modules in the application.

The fixtures defined here are automatically discovered and utilized by pytest in all test modules. This allows for
consistent setup and teardown processes across multiple tests, ensuring a clean testing environment.
"""
import pytest
from multilangstring_control import MultiLangStringControl

from langstring import LangStringControl


@pytest.fixture(autouse=True)
def reset_langstrings_flags() -> None:
    """Reset automatically all flags in the LangStringControl to False before each test.

    This fixture ensures that each test starts with a clean state regarding the flags used in the LangString module.
    It is applied to all tests automatically due to the 'autouse=True' setting.
    """
    # Reset all LangString's flags to False before each test
    LangStringControl.reset_flags()


@pytest.fixture(autouse=True)
def reset_multilangstring_strategy() -> None:
    """Reset automatically all flags in the LangStringControl to False before each test.

    This fixture ensures that each test starts with a clean state regarding the flags used in the LangString module.
    It is applied to all tests automatically due to the 'autouse=True' setting.
    """
    # Reset MultiLangString's strategy before each test
    MultiLangStringControl.reset_strategy()
