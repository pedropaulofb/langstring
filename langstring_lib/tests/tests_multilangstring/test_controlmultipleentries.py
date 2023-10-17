import pytest

from langstring_lib.multilangstring import ControlMultipleEntries


def test_enum_iteration() -> None:
    """Test enumeration of ControlMultipleEntries."""
    enum_members = list(ControlMultipleEntries)
    assert len(enum_members) == 4, "Expected 4 enum members"
    assert ControlMultipleEntries.OVERWRITE in enum_members, "OVERWRITE should be in enum_members"
    assert ControlMultipleEntries.ALLOW in enum_members, "ALLOW should be in enum_members"
    assert ControlMultipleEntries.BLOCK_WARN in enum_members, "BLOCK_WARN should be in enum_members"
    assert ControlMultipleEntries.BLOCK_ERROR in enum_members, "BLOCK_ERROR should be in enum_members"


def test_enum_names() -> None:
    """Test enum names of ControlMultipleEntries."""
    assert (ControlMultipleEntries.OVERWRITE.name) == "OVERWRITE", "Unexpected name for OVERWRITE"
    assert (ControlMultipleEntries.ALLOW.name) == "ALLOW", "Unexpected name for ALLOW"
    assert (ControlMultipleEntries.BLOCK_WARN.name) == "BLOCK_WARN", "Unexpected name for BLOCK_WARN"
    assert (ControlMultipleEntries.BLOCK_ERROR.name) == "BLOCK_ERROR", "Unexpected name for BLOCK_ERROR"


def test_enum_values() -> None:
    """Test enum values of ControlMultipleEntries."""
    assert (ControlMultipleEntries.OVERWRITE.value) == "OVERWRITE", "Unexpected value for OVERWRITE"
    assert (ControlMultipleEntries.ALLOW.value) == "ALLOW", "Unexpected value for ALLOW"
    assert (ControlMultipleEntries.BLOCK_WARN.value) == "BLOCK_WARN", "Unexpected value for BLOCK_WARN"
    assert (ControlMultipleEntries.BLOCK_ERROR.value) == "BLOCK_ERROR", "Unexpected value for BLOCK_ERROR"


def test_enum_types() -> None:
    """Test enum types of ControlMultipleEntries."""
    assert isinstance(ControlMultipleEntries.OVERWRITE, ControlMultipleEntries), "Unexpected type for OVERWRITE"
    assert isinstance(ControlMultipleEntries.OVERWRITE.name, str), "Unexpected type for OVERWRITE.name"
    assert isinstance(ControlMultipleEntries.OVERWRITE.value, str), "Unexpected type for OVERWRITE.value"


def test_invalid_enum_value() -> None:
    """Test handling of invalid enum value."""
    # Check that an invalid enum value raises a ValueError
    with pytest.raises(AttributeError, match=".*INVALID_VALUE.*"):
        ControlMultipleEntries.INVALID_VALUE
