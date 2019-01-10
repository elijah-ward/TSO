class FixedConstraint:
    type = "Fixed"

    def __init__(self, weight, time_horizon):
        self.weight = weight
        self.timeHorizon = time_horizon
