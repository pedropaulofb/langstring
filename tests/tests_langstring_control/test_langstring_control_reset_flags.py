from langstring import Controller
from langstring import LangStringFlag


def test_reset_flags_to_default() -> None:
    """Test resetting all flags to their default values.

    This test ensures that the reset_flags method sets all flags to their default state, which is False.
    """
    # Set all flags to True for testing
    for flag in LangStringFlag:
        Controller.set_flag(flag, True)

    # Reset all flags
    Controller.reset_flags_all()

    # Assert that all flags are reset to False
    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)


def test_reset_flags_idempotence() -> None:
    """Test the idempotence of the reset_flags method.

    This test ensures that calling reset_flags multiple times does not change the outcome, i.e., all flags
    should remain in their default state (False) after multiple resets.
    """
    # Reset flags twice
    Controller.reset_flags_all()
    Controller.reset_flags_all()

    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)


def test_reset_flags_effectiveness() -> None:
    """Test the effectiveness of the reset_flags method in resetting all flags to False.

    This test ensures that after modifying the flags, calling reset_flags resets them all to their default state (False).

    :raises AssertionError: If any flag does not reset to False after calling reset_flags.
    """
    # Inverting the values of all flags
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, False)
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    Controller.reset_flags_all()

    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)


def test_reset_flags_changes_state() -> None:
    """
    Test that the reset_flags method changes the state of flags from a modified state back to the default state.

    This test first modifies the state of the flags, then calls reset_flags, and finally checks if the flags have been
    reset to their default values.
    """
    # Modify the state of the flags
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, False)
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    # Ensure flags are modified
    assert not Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)

    # Reset flags
    Controller.reset_flags_all()

    # Check if flags are reset to default
    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)
