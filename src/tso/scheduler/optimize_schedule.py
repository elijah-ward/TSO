"""
optimize_schedule.py

Much of the following implementation is explained at https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
"""

from deap import base
from deap import creator
from deap import tools

from tso.scheduler.cost_heuristic import CostHeuristic

import random

def test_eval(ind):
    return sum(ind),

def print_result(ind, n_pop, n_gen):
    print('=================== Results Of Optimization ===================')
    print('Number of Generations: {}'.format(n_gen))
    print('Population Size: {}'.format(n_pop))
    print('Raw Best Individual: {}'.format(ind))
    print('Best Individual Fitness Values: {}'.format(ind.fitness.values))
    print('===============================================================')

def optimize_schedule(n_timeslots, n_pop, n_gen, cxpb, mutpb, observation_blocks, eval_func=test_eval):

    random.seed(64)

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_timeslot", random.randint, 0, n_timeslots - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_timeslot, len(observation_blocks))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Genetic Operators
    toolbox.register("evaluate", eval_func)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=n_pop)
    fitnesses = list(map(toolbox.evaluate, pop))

    # Begin Evolution through subsequent generations
    for generation in range(n_gen):
        # Create new generation
        offspring = toolbox.select(pop, len(pop))
        # Clone selected individuals
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < cxpb:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < mutpb:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    best_ind = tools.selBest(pop, k=1)[0]
    print_result(best_ind, n_pop, n_gen)
    return best_ind


if __name__ == '__main__':
    optimize_schedule(1000, 1000, 10, 0.5, 0.2, [1,2,3,4,5,6,7,8,9,10])
