"""
constraint_aggregator.py

Aggregated Constraints from Astroplan as well as our own user-defined constraints.
"""

from astroplan.constraint import AtNightConstraint, AirmassConstraint


def initialize_constraints():
    global_constraints = [AirmassConstraint(max=3, booleanConstraint=False),
                          AtNightConstraint.twilight_civil()]
