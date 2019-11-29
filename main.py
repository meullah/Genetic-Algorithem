import generatePopulation
import calculateFitness
import selection
import crossover
import mutation
def GA():
    population = generatePopulation.generate(20)
    fitness_of_Population = calculateFitness.fitness(population)
    for i in range(10000):
        selcted_population = selection.selection(population, fitness_of_Population)
        crossover_population = crossover.crossover(selcted_population)
        population = mutation.mutation(crossover_population)
        fitness = calculateFitness.fitness(population)
        print(max(fitness))
        if max(fitness) == 24:
            break


#Call the function
GA()
