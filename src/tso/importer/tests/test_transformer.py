from tso.importer import transformer
from tso.observation import observation_request, cfht_observation_block
from unittest.mock import patch


def cfht_values():
    return {
        'id': -1,
        'token': -1,
        'observing_groups_id': -1,
        'observing_block_data': -1,
        'candidate': -1,
        'sky_address': "0.11,0.11",
        'public': -1,
        'active_runid': -1,
        'min_qrun_millis': -1,
        'max_qrun_millis': -1,
        'contiguous_exposure_time_millis': -1,
        'priority': -1,
        'next_observable_at': -1,
        'unobservable_at': -1,
        'remaining_observing_chances': -1,
        'created_at': -1,
        'updated_at': -1,
        'dirty': -1,
        'version': -1,
        'label': -1,
        'program_id': -1
    }


def invalid_values():
    values = cfht_values()
    values["sky_address"] = "potato"
    return values


def valid_values():
    return cfht_values()


class TestTransformer:
    """
    Test Transformer

    As opposed to the sibling tests, these are just unit tests
    """

    def test_transformer_should_validate_invalid_blocks(self):
        invalid_block = cfht_observation_block.CFHTObservationBlock(
            **invalid_values()
        )

        invalid_block_wrong_class = "potato"

        assert transformer.validate_block(invalid_block) is False
        assert transformer.validate_block(invalid_block_wrong_class) is False

    def test_transformer_should_validate_valid_blocks(self):
        valid_block = cfht_observation_block.CFHTObservationBlock(
            **valid_values()
        )

        assert transformer.validate_block(valid_block) is True

    @patch('tso.importer.transformer.block_to_request')
    def test_transformer_should_only_map_valid_blocks(self, mock_transformer_mapping_function):

        transformer.transform_cfht_observing_blocks([
            cfht_observation_block.CFHTObservationBlock(**invalid_values()),    # One invalid block
            cfht_observation_block.CFHTObservationBlock(**valid_values()),      # ....
            cfht_observation_block.CFHTObservationBlock(**valid_values())       # And 2 valid ones
        ])

        assert mock_transformer_mapping_function.call_count is 2
