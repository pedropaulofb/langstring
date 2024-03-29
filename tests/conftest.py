"""This module contains pytest fixtures and configurations used across various test modules in the application.

The fixtures defined here are automatically discovered and utilized by pytest in all test modules. This allows for
consistent setup and teardown processes across multiple tests, ensuring a clean testing environment.
"""

import pytest

from langstring import LangStringControl
from langstring import MultiLangStringControl


@pytest.fixture(autouse=True)
def reset_configurations() -> None:
    """Reset automatically all controllable configurations before each test.

    Resets configurations in the LangStringControl and MultiLangStringControl to False before each test.

    This fixture ensures that each test starts with a clean state regarding the flags used in the
    LangString and MultiLangString modules. It is applied to all tests automatically due to the 'autouse=True' setting.
    """
    # Reset all LangString's flags to False before each test
    LangStringControl.reset_flags()
    # Reset all LangString's flags to False before each test
    MultiLangStringControl.reset_flags()
