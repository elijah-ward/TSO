class ObservationBlock:

    def __init__(self, observation_id, coordinates, agency_id, priority, remaining_observing_chances, observation_duration):
        self.observation_id = observation_id
        self.coordinates = coordinates
        self.agency_id = agency_id
        self.priority = priority
        self.remaining_observing_chances = remaining_observing_chances
        self.observation_duration = observation_duration

    def __str__(self):
        return str(self.observation_id) + " " + self.coordinates + " " + str(self.agency_id) + " " +str(self.priority)

    