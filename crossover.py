import random
def crossover(Selectedpopulation):
    array  = []
    for i in range(10):
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,5)
        array.append(Selectedpopulation[a][:c]+Selectedpopulation[b][c:])
        array.append(Selectedpopulation[b][:c]+Selectedpopulation[a][c:])
    return array

