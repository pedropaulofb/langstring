import pytest

from multilangstring_control import MultiLangStringFlag, MultiLangStringControl


@pytest.mark.parametrize(
    "flag, state",
    [
        (MultiLangStringFlag.ENSURE_TEXT, True),
        (MultiLangStringFlag.ENSURE_ANY_LANG, False),
        (MultiLangStringFlag.ENSURE_VALID_LANG, True),
        (MultiLangStringFlag.VERBOSE_MODE, False),
    ],
)
def test_set_flag_valid(flag: MultiLangStringFlag, state: bool):
    """Test setting a flag with valid inputs."""
    MultiLangStringControl.set_flag(flag, state)
    assert MultiLangStringControl.get_flag(flag) == state, f"Failed to set {flag.name} to {state}"


@pytest.mark.parametrize("flag, state", [("invalid_flag", True), (MultiLangStringFlag.ENSURE_TEXT, "not_a_boolean")])
def test_set_flag_invalid(flag, state):
    """Test setting a flag with invalid inputs."""
    with pytest.raises(TypeError, match="Invalid flag received|State must be a boolean value"):
        MultiLangStringControl.set_flag(flag, state)


@pytest.mark.parametrize(
    "flag, expected_state",
    [
        (MultiLangStringFlag.ENSURE_TEXT, False),
        (MultiLangStringFlag.ENSURE_ANY_LANG, False),
        (MultiLangStringFlag.ENSURE_VALID_LANG, False),
        (MultiLangStringFlag.VERBOSE_MODE, False),
    ],
)
def test_get_flag_default_state(flag: MultiLangStringFlag, expected_state: bool):
    """Test retrieving the default state of a flag."""
    MultiLangStringControl.reset_flags()
    assert MultiLangStringControl.get_flag(flag) == expected_state, f"{flag.name} should be {expected_state} by default"


def test_get_flag_invalid():
    """Test retrieving the state of an invalid flag."""
    with pytest.raises(TypeError, match="Invalid flag received"):
        MultiLangStringControl.get_flag("invalid_flag")


def test_get_flags():
    """Test retrieving the current state of all flags."""
    flags = MultiLangStringControl.get_flags()
    assert isinstance(flags, dict), "get_flags should return a dictionary"
    for flag in MultiLangStringFlag:
        assert flag in flags, f"{flag.name} should be in the flags dictionary"


def test_reset_flags():
    """Test resetting all flags to their default values."""
    # Set a flag to a non-default value
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_TEXT, True)
    MultiLangStringControl.reset_flags()
    for flag in MultiLangStringFlag:
        assert MultiLangStringControl.get_flag(flag) is False, f"{flag.name} should be reset to False"
