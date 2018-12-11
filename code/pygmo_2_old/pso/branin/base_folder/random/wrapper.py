from PyGMO import *

def main (job_id,params):
	prob = problem.branin()
	algo = algorithm.pso(gen=1000, omega=float(params['omega']), eta1=float(params['eta']), eta2=float(params['eta2']), vcoeff=0.5, variant=5, neighb_type=2, neighb_param=4) #Default.

	#Simple evaluation based in 40 individuals evolving through algo criterion in algo problem.
	isl = island(algo,prob,1000)
	isl.evolve(100)
	return float(str(isl.population.champion.f).replace("(","").replace(")","").replace(",",""))
