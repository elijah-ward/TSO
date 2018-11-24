# cost_heuristic.py
import tsocli.src.constraint_analyzer as ca

class CostHeuristic:

    def __init__(self, constraints):
        self.constraints = [ ca.analyze(constraint) for constraint in constraints ]

