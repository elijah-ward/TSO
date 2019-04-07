"""
constraint_aggregator.py

Aggregated Constraints from Astroplan as well as our own user-defined constraints.

In our architecture we define the concept of a "Static Constraint" as one that always applies no matter
how far we are scheduling into the future

"Dynamic Constraints" are those that only apply if our total schedule window does not exceed some preset
time in the future
"""

from astroplan.constraints import AtNightConstraint, AirmassConstraint


def initialize_constraints():
    global_constraints = [AirmassConstraint(max=3, boolean_constraint=False),
                          AtNightConstraint.twilight_civil()]

    return global_constraints
