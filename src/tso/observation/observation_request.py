from astropy import units as u
from astropy.coordinates import SkyCoord
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

    def getTarget(self):
        skycoord = SkyCoord(ra=self.coordinates[0]*u.deg, dec=self.coordinates[1]*u.deg)
        target = FixedTarget(skycoord, self.observation_id)
        return target

    def __str__(self):
        return str(self.observation_id) + " " + \
               str(self.coordinates[0]) + " " + \
               str(self.coordinates[1]) + " " + \
               str(self.agency_id) + " " +\
               str(self.priority)
