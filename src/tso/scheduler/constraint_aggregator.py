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


def create_unmapped_constraint(*values):
    return None


def create_air_mass_constraint(values):
    return AirmassConstraint(
        max=values.get("max"),
        boolean_constraint=values.get("boolean_constraint")
    )


def create_at_night_constraint(*values):
    return AtNightConstraint.twilight_civil()


def create_tso_outage_constraint(values):
    return TsoOutageConstraint(outage_config=values)


constraint_map = {
    "AirmassConstraint": create_air_mass_constraint,
    "AtNightConstraint": create_at_night_constraint,
    "TsoOutageConstraint": create_tso_outage_constraint

    # TODO: Add more...?
}


def initialize_constraints(constraint_configuration):
    global_constraints = []
    for key, value in constraint_configuration.items():
        mapped_c = constraint_map.get(key, create_unmapped_constraint)(value)
        if mapped_c is not None:
            global_constraints.append(mapped_c)

    return global_constraints
