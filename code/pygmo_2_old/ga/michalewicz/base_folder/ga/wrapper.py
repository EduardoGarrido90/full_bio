from PyGMO import *

def main (job_id, params):
	prob = problem.michalewicz(dim = 50)
	algo = algorithm.sga(gen=1000, cr=float(params['cr']), m=float(params['m']), elitism=1, mutation=algorithm._algorithm._sga_mutation_type.GAUSSIAN, width=0.1, selection=algorithm._algorithm._sga_selection_type.ROULETTE, crossover=algorithm._algorithm._sga_crossover_type.EXPONENTIAL)

	#Simple evaluation based in 40 individuals evolving through algo criterion in algo problem.
	isl = island(algo,prob,1000)
	isl.evolve(100)
	return float(str(isl.population.champion.f).replace("(","").replace(")","").replace(",",""))
