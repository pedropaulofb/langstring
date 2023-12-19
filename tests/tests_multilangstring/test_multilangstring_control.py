from unittest.mock import patch

import pytest
from loguru import logger
from multilangstring_control import MultiLangStringControl
from multilangstring_control import MultiLangStringStrategy


@pytest.mark.parametrize(
    "strategy",
    [
        MultiLangStringStrategy.OVERWRITE,
        MultiLangStringStrategy.ALLOW,
        MultiLangStringStrategy.BLOCK_WARN,
        MultiLangStringStrategy.BLOCK_ERROR,
    ],
)
def test_set_strategy_valid(strategy: MultiLangStringStrategy) -> None:
    """Test setting a valid global control strategy."""
    MultiLangStringControl.set_strategy(strategy)
    assert MultiLangStringControl.get_strategy() == strategy, f"Global control strategy should be set to {strategy}"


def test_set_strategy_invalid() -> None:
    """Test setting an invalid global control strategy."""
    with pytest.raises(TypeError, match="Invalid control received. Valid controls are:"):
        MultiLangStringControl.set_strategy("InvalidStrategy")


def test_get_strategy() -> None:
    """Test retrieving the current global control strategy."""
    default_strategy = MultiLangStringStrategy.ALLOW
    MultiLangStringControl.set_strategy(default_strategy)
    assert (
        MultiLangStringControl.get_strategy() == default_strategy
    ), "Should retrieve the current global control strategy"


def test_log_strategy() -> None:
    """Test logging the current global control strategy."""
    with patch.object(logger, "info") as mock_logger:
        MultiLangStringControl.log_strategy()
        mock_logger.assert_called_once_with(
            f"Global MultiLangString control strategy: {MultiLangStringControl.get_strategy()}"
        )


def test_reset_strategy() -> None:
    """Test resetting the global control strategy to the default value."""
    # Set to a non-default strategy for testing
    MultiLangStringControl.set_strategy(MultiLangStringStrategy.BLOCK_ERROR)
    MultiLangStringControl.reset_strategy()
    assert (
        MultiLangStringControl.get_strategy() == MultiLangStringStrategy.ALLOW
    ), "Global control strategy should be reset to default (ALLOW)"
