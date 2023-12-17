import pytest

from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags():
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
