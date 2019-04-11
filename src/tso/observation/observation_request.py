from astropy.coordinates import SkyCoord, Angle
from astroplan import FixedTarget

"""
Observation Request

Creates an observation request, that follows the internal TSO model
"""

class ObservationRequest:

    def __init__(
        self,
        observation_id,
        coordinates,
        agency_id,
        priority,
        remaining_observing_chances,
        duration,
        exposure_count,
        constraint_meta
    ):
        if not isinstance(coordinates, SkyCoord):
            raise RuntimeError("Constructor Error :: Coordinates have not been mapped to Astropy SkyCoord Class")

        self.observation_id = observation_id
        self.coordinates = coordinates
        self.agency_id = agency_id
        self.priority = priority
        self.remaining_observing_chances = remaining_observing_chances
        self.duration = duration
        self.exposure_count = exposure_count
        self.constraint_meta = constraint_meta

        self.target = FixedTarget(coord=coordinates, name=str(observation_id))

    def __str__(self):
        return str(self.observation_id) + " " + \
               str(self.coordinates.ra.degree) + " " + \
               str(self.coordinates.dec.degree) + " " + \
               str(self.agency_id) + " " +\
               str(self.priority)
