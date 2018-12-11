from __future__ import division, print_function
import pygmo as pg
import logging
from smac.facade.func_facade import fmin_smac

def rosenbrock_2d(x):

    generations = x[0]
    prob = pg.problem(pg.rosenbrock(2))

    # 2 - Instantiate a pagmo algorithm
    algo = pg.algorithm(pg.sga(gen=generations, cr = .90, eta_c = 1., m = 0.02, param_m = 1., param_s = 2, crossover = "exponential", mutation = "polynomial", selection = "tournament", seed = 3))

    # 3 - Instantiate an archipelago with 16 islands having each 20 individuals
    archi = pg.archipelago(16, algo=algo, prob=prob, pop_size=20)

    # 4 - Run the evolution in parallel on the 16 separate islands 10 times.
    archi.evolve(10)

    # 5 - Wait for the evolutions to be finished
    archi.wait()

    # 6 - Print the fitness of the best solution in each island
    res = [isl.get_population().champion_f for isl in archi]
    import pdb; pdb.set_trace();
    return res

# debug output
logging.basicConfig(level=20)
logger = logging.getLogger("Optimizer") # Enable to show Debug outputs
x, cost, _ = fmin_smac(func=rosenbrock_2d,
                       x0=[51],
                       bounds=[(50, 100)],
                       maxfun=5,
                       rng=3)  # Passing a seed makes fmin_smac determistic

print("Best x: %s; with cost: %f"% (str(x), cost))
