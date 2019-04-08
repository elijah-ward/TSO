"""
constraint_aggregator.py

Aggregated Constraints from Astroplan as well as our own user-defined constraints.

In our architecture we define the concept of a "Static Constraint" as one that always applies no matter
how far we are scheduling into the future

"Dynamic Constraints" are those that only apply if our total schedule window does not exceed some preset
time in the future
"""

from astroplan.constraints import AtNightConstraint, AirmassConstraint
from tso.scheduler.weather_constraint import WeatherConstraint


def initialize_constraints(start_datetime, end_datetime):
    global_constraints = [AirmassConstraint(max=3, boolean_constraint=False),
                          AtNightConstraint.twilight_civil(), WeatherConstraint(start_datetime, end_datetime)]

    return global_constraints
