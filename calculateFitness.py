import numpy as np
def fitness(population):
    list = []
    for i in population:
        grid = np.zeros((6, 6), dtype=int)
        temp1 = makeGrid(grid,i)
        array = np.array(temp1)
        list += [np.sum(array)]
    return list
def makeGrid(grid,array):
    for i in range(5):
        temp2 = array[i]
        grid[temp2[0],temp2[1]] = 1
        # up
        if((temp2[0]-1) >= 0):
            grid[(temp2[0]-1),temp2[1]] = 1
        # down
        if((temp2[0]+1) <=5 ): 
            grid[(temp2[0]+1),temp2[1]]  =1
        # left
        if ((temp2[1]-1) >= 0):  
            grid[temp2[0],(temp2[1]-1)] = 1
        # right
        if ((temp2[1]+1) <= 5):  
            grid[temp2[0],(temp2[1]+1)] = 1
    return grid


