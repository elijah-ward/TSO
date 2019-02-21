# cost_heuristic.py
from tso.scheduler import constraint_analyzer as ca

class CostHeuristic:

    def __init__(self, constraints):
        self.constraints = [ca.analyze(constraint) for constraint in constraints]

