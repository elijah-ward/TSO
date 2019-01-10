# cost_heuristic.py
from . import constraint_analyzer as ca


class CostHeuristic:

    def __init__(self, constraints):
        self.constraints = [ca.analyze(constraint) for constraint in constraints]

