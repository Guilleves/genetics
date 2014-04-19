from random import randrange, random

def newPopulation(popSize, gens, range = 2):
	'''This function returns a matrix of popSize x gens filled up with random 
	numbers from 0 to range - 1'''
	
	population = []

	for x in xrange(0, popSize):
		population.append([])
		for y in xrange(0, gens):
			population[x].append(randrange(range))
	return population

def chrToString(chr):
	'''Receive a chromesome (a list of int) and return a string representation'''

	return str(chr).strip('[]').replace(', ', '')

def binToDec(population):
	'''Receive a list of lists of 0 and 1 and return a single list with the 
	decimal value of he binary list'''

	dec = []

	for x in population:
		aux = chrToString(x)
		dec.append(int(aux, 2))
	return dec

def objetiveFunc(population, coef = 2. ** 30. - 1.):
	'''Receive a population the coef param and return a list with the objetive 
	function values'''

	decPopulation = binToDec(population)
	ofValues = []
	for x in decPopulation:
		ofValues.append(float('%.3f'%((x / coef) ** 2)))
	return ofValues

def fitness(population):
	'''Receive a population and return a list of floats with the fitness 
	function values. To do that the objetiveFunc() function is needed '''

	ofValues = objetiveFunc(population)
	ffValues = []
	sumOF = sum(ofValues)
	for x in ofValues:
		ffValues.append(float('%.3f'%(x / sumOF)))
	return ffValues

def newRoulette(population):
	'''Receive a population and return a roulette, a list where the index of 
	each chromesome appears proportionaly to its fitness function values'''
	
	roulette = []
	ffValues = fitness(population)
	for chrIndex in xrange(0, len(ffValues)):
		for x in xrange(0, int(ffValues[chrIndex] * 100)):
			roulette.append(chrIndex)
	return roulette

def selector(population):
	'''Return a list with the indexes of the chromesomes that will parents of
	the next generation'''

	roulette = newRoulette(population)
	parents = []
	for x in xrange(0, len(population)):
		parents.append(roulette[randrange(len(roulette) - 1)])
	return parents

def crossover(population, coChance):
	'''Receive a population and the chance of cross-over and return a population
	with the (unmutated) chromesomes for the next generation'''

	parents = selector(population)
	chrLen = len(population[0])
	nextPopulation = []
	for x in xrange(0, len(population) - 1, 2):
		if (random() <= coChance):
			cutPoint = randrange(chrLen)
			aux = population[parents[x + 1]][cutPoint - chrLen:]
			nextPopulation.append(population[parents[x + 1]][:cutPoint] + 
				population[parents[x]][cutPoint - chrLen:])
			nextPopulation.append(population[parents[x]][:cutPoint] + aux)
		else:
			nextPopulation.append(population[parents[x]])
			nextPopulation.append(population[parents[x + 1]])
	return nextPopulation

def mutation(population, mChance):

	chrLen = len(population[0])
	nextPopulation = []
	for x in population:
		if (random() <= mChance):
			i = randrange(chrLen)
			if (x[i] == 1):
				x[i] = 0
			else:
				x[i] = 1
		nextPopulation.append(x)

	return nextPopulation
