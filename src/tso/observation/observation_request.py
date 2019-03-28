from astropy import units as u
from astropy.coordinates import SkyCoord, Angle
from astroplan import FixedTarget


class ObservationRequest:

    def __init__(
        self, observation_id, coordinates, agency_id, priority, remaining_observing_chances, observation_duration
    ):
        self.observation_id = observation_id
        self.coordinates = coordinates
        self.agency_id = agency_id
        self.priority = priority
        self.remaining_observing_chances = remaining_observing_chances
        self.observation_duration = observation_duration

    def get_target(self):
        target = FixedTarget(coord=self.coordinates, name=str(self.observation_id))
        return target

    def __str__(self):
        return str(self.observation_id) + " " + \
               str(self.coordinates.ra.degree) + " " + \
               str(self.coordinates.dec.degree) + " " + \
               str(self.agency_id) + " " +\
               str(self.priority)
