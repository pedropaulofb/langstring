import pytest

from langstring import LangStringControl
from langstring import LangStringFlag


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
        (LangStringFlag.ENSURE_VALID_LANG, True),
    ],
)
def test_set_flag_valid(flag: LangStringFlag, state: bool) -> None:
    """Test setting a flag with valid values."""
    LangStringControl.set_flag(flag, state)
    assert LangStringControl.get_flag(flag) == state, "Flag state should be updated correctly"


@pytest.mark.parametrize("flag, state", [("InvalidFlag", True), (123, False)])
def test_set_flag_invalid(flag, state) -> None:
    """Test setting a flag with invalid flag values."""
    with pytest.raises(TypeError, match="received. Valid flags are members of"):
        LangStringControl.set_flag(flag, state)


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, None),
        (LangStringFlag.ENSURE_ANY_LANG, "True"),
        (LangStringFlag.ENSURE_VALID_LANG, 1),
    ],
)
def test_set_flag_invalid_state_type(flag: LangStringFlag, state) -> None:
    """Test setting a flag with invalid state types.

    :param flag: The LangStringFlag to be set.
    :param state: The invalid state type to set for the flag.
    """
    with pytest.raises(TypeError, match="State must be a boolean"):
        LangStringControl.set_flag(flag, state)


@pytest.mark.parametrize(
    "flag, initial_state, new_state",
    [
        (LangStringFlag.ENSURE_TEXT, False, True),
        (LangStringFlag.ENSURE_ANY_LANG, True, False),
        (LangStringFlag.ENSURE_VALID_LANG, False, True),
    ],
)
def test_toggle_flag_state(flag: LangStringFlag, initial_state: bool, new_state: bool) -> None:
    """Test toggling the state of a flag.

    :param flag: The LangStringFlag to be toggled.
    :param initial_state: The initial state to set for the flag.
    :param new_state: The new state to set for the flag.
    """
    LangStringControl.set_flag(flag, initial_state)
    assert LangStringControl.get_flag(flag) == initial_state, "Initial flag state should be set correctly"
    LangStringControl.set_flag(flag, new_state)
    assert LangStringControl.get_flag(flag) == new_state, "Flag state should be toggled correctly"


@pytest.mark.parametrize(
    "flag_sequence, state_sequence",
    [
        ([LangStringFlag.ENSURE_TEXT, LangStringFlag.ENSURE_ANY_LANG], [True, False]),
        ([LangStringFlag.ENSURE_VALID_LANG, LangStringFlag.ENSURE_TEXT], [True, False]),
    ],
)
def test_set_multiple_flags_sequentially(flag_sequence: list[LangStringFlag], state_sequence: list[bool]) -> None:
    """
    Test setting multiple flags sequentially to ensure each flag is updated correctly without affecting others.

    :param flag_sequence: A sequence of LangStringFlags to be set.
    :param state_sequence: A sequence of states corresponding to the flags in flag_sequence.
    """
    for flag, state in zip(flag_sequence, state_sequence):
        LangStringControl.set_flag(flag, state)
    for flag, state in zip(flag_sequence, state_sequence):
        assert LangStringControl.get_flag(flag) == state, f"Flag {flag.name} should be set to {state}"


@pytest.mark.parametrize(
    "flag, state",
    [
        (LangStringFlag.ENSURE_TEXT, True),
        (LangStringFlag.ENSURE_ANY_LANG, False),
    ],
)
def test_set_flag_same_value_multiple_times(flag: LangStringFlag, state: bool) -> None:
    """
    Test setting a flag to the same value multiple times to ensure it does not cause any issues.

    :param flag: The LangStringFlag to be set.
    :param state: The state to set for the flag.
    """
    for _ in range(3):  # Set the same state multiple times
        LangStringControl.set_flag(flag, state)
    assert LangStringControl.get_flag(flag) == state, f"Flag {flag.name} should remain {state} after multiple settings"
