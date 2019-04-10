"""
constraint_aggregator.py

Aggregated Constraints from Astroplan as well as our own user-defined constraints.

In our architecture we define the concept of a "Static Constraint" as one that always applies no matter
how far we are scheduling into the future

"Dynamic Constraints" are those that only apply if our total schedule window does not exceed some preset
time in the future
"""

from .constraints import TsoOutageConstraint
from astroplan.constraints import AtNightConstraint, AirmassConstraint
from tso.scheduler.weather_constraint import WeatherConstraint


def create_unmapped_constraint(*values):
    return None


def create_air_mass_constraint(values):
    return AirmassConstraint(
        max=values.get("max"),
        boolean_constraint=values.get("boolean_constraint")
    )


def create_at_night_constraint(*values):
    return AtNightConstraint.twilight_civil()


def create_weather_constraint(values):
    return WeatherConstraint(
        start_time=values.get("start_datetime"),
        end_time=values.get("end_datetime"),
        cloud_threshold=values.get("cloud_threshold"),
        cloud_average_threshold=values.get("cloud_average_threshold"),
        rain_threshold=values.get("rain_threshold")
    )


def create_tso_outage_constraint(values):
    return TsoOutageConstraint(outage_config=values)


constraint_map = {
    "AirmassConstraint": create_air_mass_constraint,
    "AtNightConstraint": create_at_night_constraint,
    "TsoOutageConstraint": create_tso_outage_constraint,
    "WeatherConstraint": create_weather_constraint
}


def initialize_constraints(constraint_configuration, start_datetime, end_datetime, no_weather_constraints):
    if not no_weather_constraints:
        if 'WeatherConstraint' in constraint_configuration:
            constraint_configuration['WeatherConstraint']['start_datetime'] = start_datetime
            constraint_configuration['WeatherConstraint']['end_datetime'] = end_datetime
    global_constraints = []
    for key, value in constraint_configuration.items():
        mapped_c = constraint_map.get(key, create_unmapped_constraint)(value)
        if mapped_c is not None:
            global_constraints.append(mapped_c)

    return global_constraints
