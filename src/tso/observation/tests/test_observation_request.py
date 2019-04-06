import pytest
import astroplan
from tso.observation import observation_request
from astropy import units as u
from astropy.coordinates import SkyCoord
from astroplan import FixedTarget


@pytest.fixture(scope="module")
def req():
    c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
    observation_id = 69
    coordinates = c
    agency_id = 2
    priority = 8
    remaining_observing_chances = 3
    observation_duration = 6000
    req = observation_request.ObservationRequest(
        observation_id, coordinates, agency_id, priority, remaining_observing_chances, observation_duration
    )
    return req

@pytest.fixture(scope="module")
def variables():
    return {
        "observation_id": 69,
        "coordinates": SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs'),
        "agency_id": 2,
        "priority": 8,
        "remaining_observing_chances": 3,
        "duration": 6000
    }


class TestObservationRequest:
    def test_dummy_test(self):
        # Shows the limitsof a SkyCoord
        # a) declination < -90
        with pytest.raises(ValueError):
            c = SkyCoord(ra=90.625*u.degree, dec=-90.1*u.degree, frame='icrs')

        # b) declination > 90
        with pytest.raises(ValueError):
            c = SkyCoord(ra=90.625*u.degree, dec=90.1*u.degree, frame='icrs')

        #  c) ra above 360
        c = SkyCoord(ra=360.625*u.degree, dec=70.2*u.degree, frame='icrs')
        assert c.ra.degree == 0.625

        c = SkyCoord(ra=-0.625*u.degree, dec=71.2*u.degree, frame='icrs')
        assert c.ra.degree == 359.375

    def test_observation_request_init(self, req):
        assert hasattr(req, 'observation_id')
        assert hasattr(req, 'coordinates')
        assert hasattr(req, 'agency_id')
        assert hasattr(req, 'priority')
        assert hasattr(req, 'remaining_observing_chances')
        assert hasattr(req, 'duration')
        assert hasattr(req, 'target')

    def test_observation_request_get_target(self, req):
        target = req.target
        assert isinstance(target, FixedTarget)

    def test_observation_request_to_string(self, req):
        assert str(req) == "69 10.625 41.2 2 8"

    def test_invalid_observation_request_init(self, variables):

        with pytest.raises(RuntimeError) as validation_error:
            observation_request.ObservationRequest(
                variables["observation_id"],
                "potato",
                variables["agency_id"],
                variables["priority"],
                variables["remaining_observing_chances"],
                variables["duration"]
            )
