# ga.py
# Much of the following implementation is explained at https://deap.readthedocs.io/en/master/tutorials/basic/part1.html

from deap import tools
from tsocli.src.cost_heuristic import CostHeuristic

IND_SIZE = 10


def ga():

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attribute", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attribute, n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
