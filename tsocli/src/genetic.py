# genetic.py
import deap
from tsocli.src.cost_heuristic import CostHeuristic

class Genetic:

    def __init__(self, population=100):
        self.population = population
