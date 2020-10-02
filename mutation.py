import random
def mutation(population):
    for i in population:
        p = random.randint(0,4)
        value1 = random.randint(0,5)
        value2 = random.randint(0,5)
        i[p] = [value1,value2]
    return population
