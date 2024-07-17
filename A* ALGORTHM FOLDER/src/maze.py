from random import *
import numpy as np

# Create the 101x101 grid with 30% of the cells blocked denoted by 1
# setting the (default) inital cell source (0,0) as 2 for idenity purposes
# setting the (default) final cell destination (100, 100) as -2 for identity purposes
def generateMaze():
    grid = np.zeros((101, 101))
    for i in range(101):
        for j in range(101):
            if np.random.rand() < 0.30:
                grid[i, j] = 1
    grid[0][0] = 2
    grid[len(grid) - 1][len(grid) - 1] = -2
    return grid