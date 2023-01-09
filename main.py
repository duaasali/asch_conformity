# functions to create actors
import random
from asch_conformity import ModuleRunner


class Main:
    times_to_run = 10
    num_of_actors = 5
    # create_actors(num_of_actors)
    propensityToLieDistribution = round(random.random(), 1)
    propensityToConform = round(random.random(), 1)

    M = ModuleRunner(propensityToLieDistribution, propensityToConform, num_of_actors)
    M.runModel()
    M.outputCsv()
    # M.visualize_data()


