"""This module contains pytest fixtures and configurations used across various test modules in the application.

The fixtures defined here are automatically discovered and utilized by pytest in all test modules. This allows for
consistent setup and teardown processes across multiple tests, ensuring a clean testing environment.
"""
import pytest

from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags() -> None:
    """Reset automatically all flags in the LangStringControl to False before each test.

    This fixture ensures that each test starts with a clean state regarding the flags used in the LangString module.
    It is applied to all tests automatically due to the 'autouse=True' setting.
    """
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
