"""
ga.py

Much of the following implementation is explained at https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
"""

from deap import base
from deap import creator
from deap import tools

from .cost_heuristic import CostHeuristic

def ga(n_timeslots, n_pop, n_gen, cxpb, mutpb, eval_func, time_assignment, observation_blocks):

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_timeslot", random.randint, 0, n_timeslots - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_timeslot, len(observation_blocks))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Genetic Operators
    toolbox.register("evaluate", evalOneMax)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
