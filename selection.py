def selection(population,FitnessList):
    selected = []
    for i in range(10):
        temp = max(FitnessList)
        selected.append(population[FitnessList.index(temp)])
        FitnessList[FitnessList.index(temp)] = 0
    return selected

