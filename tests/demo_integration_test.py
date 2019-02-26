from tso.observation import observation_request
from tso.importer import transformer


class TestDemoIntegration:

    def test_observation_and_transform(self):
        c = (123, 123)

        block = observation_request.ObservationRequest(
            22, c, 123, 123, 123, 123
        )

        print(
            "Observation block: ",
            block
        )

        new_block = transformer.transform("testing")
