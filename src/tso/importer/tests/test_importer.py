from tso.importer import data_importer
from sys import maxsize as MAX_SIZE
from tso.observation.cfht_observation_block import CFHTObservationBlock


class TestDataImporter:

    def test_observation_get_all(self):
        observations = data_importer.get_all_observations()

        assert len(observations) > 0

    def test_observation_get_with_constraint(self):
        observations = data_importer.get_observations(
            min_priority=0,
            remaining_observing_chances=MAX_SIZE/2,
            observation_duration_min=-1,
            observation_duration_max=MAX_SIZE
        )
        all_observations = data_importer.get_all_observations()

        assert len(observations) <= len(all_observations)

    def test_observation_get_with_constraint_with_default_values(self):
        observations = data_importer.get_observations()
        all_observations = data_importer.get_all_observations()

        assert len(observations) == len(all_observations)
