from unittest.mock import patch

import pytest
from loguru import logger

from langstring.langstring_control import LangStringControl
from langstring.langstring_control import LangStringFlag


@pytest.fixture(autouse=True)
def reset_flags():
    # Reset all flags to False before each test
    for flag in LangStringFlag:
        LangStringControl.set_flag(flag, False)
    yield


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
        (LangStringFlag.ENSURE_VALID_LANG, True),
        (LangStringFlag.VERBOSE_MODE, False),
    ],
)
def test_set_flag_valid(flag: LangStringFlag, state: bool):
    """Test setting a flag with valid values."""
    LangStringControl.set_flag(flag, state)
    assert LangStringControl.get_flag(flag) == state, "Flag state should be updated correctly"


@pytest.mark.parametrize("flag, state", [("InvalidFlag", True), (123, False)])
def test_set_flag_invalid(flag, state):
    """Test setting a flag with invalid flag values."""
    with pytest.raises(TypeError, match="Invalid flag received. Valid flags are:"):
        LangStringControl.set_flag(flag, state)


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
        LangStringFlag.VERBOSE_MODE,
    ],
)
def test_get_flag_valid(flag: LangStringFlag):
    """Test retrieving the state of a valid flag."""
    LangStringControl.set_flag(flag, True)  # Set flag to True for testing
    assert LangStringControl.get_flag(flag) is True, "Flag state should be retrievable"


def test_get_flag_invalid():
    """Test retrieving the state of an invalid flag."""
    with pytest.raises(TypeError, match="Invalid flag received. Valid flags are:"):
        LangStringControl.get_flag("InvalidFlag")


def test_get_flags():
    """Test retrieving the states of all flags."""
    expected_flags = {
        LangStringFlag.ENSURE_TEXT: False,
        LangStringFlag.ENSURE_ANY_LANG: False,
        LangStringFlag.ENSURE_VALID_LANG: False,
        LangStringFlag.VERBOSE_MODE: False,
    }
    assert LangStringControl.get_flags() == expected_flags, "All flags should be retrieved correctly"


def test_log_flags():
    """Test logging the state of all flags."""
    with patch.object(logger, "info") as mock_logger:
        LangStringControl.log_flags()
        for flag in LangStringFlag:
            mock_logger.assert_any_call(f"{flag.name} = {LangStringControl.get_flag(flag)}")
