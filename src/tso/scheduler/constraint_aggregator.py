"""
constraint_aggregator.py

Aggregated Constraints from Astroplan as well as our own user-defined constraints.
"""

from astroplan.constraints import AtNightConstraint, AirmassConstraint


def initialize_constraints():
    global_constraints = [AirmassConstraint(max=3, boolean_constraint=False),
                          AtNightConstraint.twilight_civil()]

    return global_constraints
