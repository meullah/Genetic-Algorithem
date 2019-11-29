def makeGrid(grid,array):
    for i in range(5):
        temp = array[i]
        grid[temp[0],temp[1]] = 1
        if((temp[0]-1) >= 0): # up
            grid[(temp[0]-1),temp[1]] = 1
        if((temp[0]+1) <=5 ): # down
            grid[(temp[0]+1),temp[1]]  =1
        if ((temp[1]-1) >= 0):  # left
            grid[temp[0],(temp[1]-1)] = 1
        if ((temp[1]+1) <= 5):  # right
            grid[temp[0],(temp[1]+1)] = 1
    return grid

