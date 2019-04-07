from tso.observation.observation_request import ObservationRequest
from astropy.coordinates import SkyCoord
from astropy import units as u
import random


def generate_mock_requests(n_requests):
    reqs = []
    for i in range(n_requests):
        # Build a request and append to reqs list
        obs_id = i
        coordinates = SkyCoord(ra=random.uniform(1,360), dec=random.uniform(-90,90), unit=(u.degree, u.degree), frame='icrs')
        agency_id = 1
        priority = i+1
        remaining_chances = 1
        duration = 60.0 * u.second
        exposure_count = 5
        meta_constraint = {}
        req = ObservationRequest(
            obs_id,
            coordinates,
            agency_id,
            priority,
            remaining_chances,
            duration,
            exposure_count,
            meta_constraint
        )

        reqs.append(req)

    return reqs
