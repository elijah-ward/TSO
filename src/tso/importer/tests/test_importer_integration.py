from tso.importer import data_importer
from sys import maxsize as MAX_SIZE
from tso.observation.cfht_observation_block import CFHTObservationBlock
from configuration import configuration_parser


def get_db_config():
    return {
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "DB": "tso",
        "USER": "tsouser",
        "PASSWORD": "password"
    }


class TestDataImporterIntegration:

    def test_observation_get_all(self):
        observations = data_importer.get_all_observations(get_db_config())

        assert len(observations) > 0

    def test_observation_get_with_constraint(self):
        observations = data_importer.get_observations(
            db_config=get_db_config(),
            min_priority=0,
            remaining_observing_chances=MAX_SIZE/2,
            observation_duration_min=-1,
            observation_duration_max=MAX_SIZE
        )
        all_observations = data_importer.get_all_observations(get_db_config())

        assert len(observations) <= len(all_observations)

    def test_observation_get_with_constraint_with_default_values(self):
        observations = data_importer.get_observations(get_db_config())
        all_observations = data_importer.get_all_observations(get_db_config())

        assert len(observations) == len(all_observations)

    def test_getting_exposure_counts_per_id(self):
        exposures_count_by_id = data_importer.get_exposure_counts_per_observation_id(get_db_config())
        print(exposures_count_by_id)

    def test_observation_blocks_should_have_their_exposure_set(self):
        result_from_all = data_importer.get_all_observations(get_db_config())
        result_from_filters = data_importer.get_observations(get_db_config())

        for o in (result_from_all + result_from_filters):
            assert o.exposure_count is not -1
