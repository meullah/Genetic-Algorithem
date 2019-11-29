import random
def mutation(population):
    for i in population:
        p = random.randint(0,4)
        value = random.randint(0,5)
        value1 = random.randint(0,5)
        i[p] = [value,value1]
    return population
