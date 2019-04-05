from astropy import units as u
from astropy.coordinates import SkyCoord, Angle
from astroplan import FixedTarget

# TODO: Confirm if this takes coordinates as a tuple of floats or as an already-instantiated SKyCoord object
# ^ SkyCoord is imported but not used

class ObservationRequest:

    def __init__(
        self, observation_id, coordinates, agency_id, priority, remaining_observing_chances, duration
    ):
        self.observation_id = observation_id
        self.coordinates = coordinates
        self.agency_id = agency_id
        self.priority = priority
        self.remaining_observing_chances = remaining_observing_chances
        self.duration = duration
        self.target = FixedTarget(coord=coordinates, name=str(observation_id))

    def __str__(self):
        return str(self.observation_id) + " " + \
               str(self.coordinates.ra.degree) + " " + \
               str(self.coordinates.dec.degree) + " " + \
               str(self.agency_id) + " " +\
               str(self.priority)
