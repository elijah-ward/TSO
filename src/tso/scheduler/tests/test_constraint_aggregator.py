from tso.scheduler import constraint_aggregator
import pytest
from unittest.mock import patch, MagicMock, mock_open

mock_constraint_config = {
    "AirmassConstraint": {
        "max": 3,
        "boolean_constraint": False
    },
    "AtNightConstraint": {}
}

mock_invalid_constraint_config = {
    "Potato": {
        "spud": True,
        "irish": "yes!"
    }
}


class TestConstraintAggregator:

    def test_should_map_correct_(self):

        mapped_constraints = constraint_aggregator.initialize_constraints(mock_constraint_config)

        assert len(mapped_constraints) is 2

    def test_should_handle_invalid_names(self):

        mapped_constraints = constraint_aggregator.initialize_constraints(mock_invalid_constraint_config)

        assert len(mapped_constraints) is 0
