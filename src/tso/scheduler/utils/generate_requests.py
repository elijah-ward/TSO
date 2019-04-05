from tso.observation.observation_request import ObservationRequest
from astropy.coordinates import SkyCoord, Angle
from astropy import units as u
import random

def generate_requests(n_requests):
    reqs = []
    for i in range(n_requests):
        # Build a request and append to reqs list
        obs_id = i
        coordinates = SkyCoord(ra=250.0*u.deg, dec=-16.0*u.deg)
        agency_id = 1
        priority = i
        remaining_chances = 1
        duration = 60.0 * u.second
        req = ObservationRequest(obs_id, coordinates, agency_id, priority, remaining_chances, duration)

        reqs.append(req)

    return reqs
