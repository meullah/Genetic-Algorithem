def makeGrid(grid, array):
    for i in range(5):
        temp = array[i]
        grid[temp[0], temp[1]] = 1
         # up
        if((temp[0]-1) >= 0):
            grid[(temp[0]-1), temp[1]] = 1
         # down
        if((temp[0]+1) <=5 ):
            grid[(temp[0]+1), temp[1]]  =1
         # left
        if ((temp[1]-1) >= 0):  
            grid[temp[0], (temp[1]-1)] = 1
         # left
        if ((temp[1]+1) <= 5):  
            grid[temp[0], (temp[1]+1)] = 1
         # right
    return grid

