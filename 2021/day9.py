import numpy as np

data = open('day9','r').readlines()

floor = np.array([int(value) for column in data for value in column.strip()])
floor = floor.reshape((len(data), -1))

x_max = len(floor[:,0])
y_max = len(floor[0,:])

local_minima = list()

adjacents = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for x in range(x_max):
    for y in range(y_max):
        minima = True
        for dx, dy in adjacents:
            if x+dx >= 0 and x+dx < x_max and y+dy >= 0 and y+dy < y_max:
                if floor[x,y] >= floor[x+dx,y+dy]:
                    minima = False
                    break
        if minima:
            local_minima.append(floor[x,y]+1)
print( np.sum(local_minima) )

# Part 2 is looking for boundaries of 9's, then counting the area 
# surrounding the 9's.
floor_mask = floor != 9
local_minima = list()
# Run through the tiles 
