"""
ga.py

Much of the following implementation is explained at https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
"""

from deap import base
from deap import creator
from deap import tools

from cost_heuristic import CostHeuristic

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

    pop = toolbox.population(n=n_pop)
    best = pop[0]
    fitnesses = list(map(toolbox.evaluate, pop))

    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
        if ind.fitness.values > best.fitness.values:
            best = toolbox.clone(ind)

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


