import numpy as np

data = open('day9','r').readlines()

floor = np.array([int(value) for column in data for value in column.strip()])
floor = floor.reshape((len(data), -1))

x_max = len(floor[:,0])
y_max = len(floor[0,:])

local_minima = list()

for x in range(x_max):
    for y in range(y_max):
        
        # Middle areas
        if x > 0 and y > 0 and x < x_max-1 and y < y_max-1:
            if floor[x,y] < floor[x+1,y] and \
               floor[x,y] < floor[x-1,y] and \
               floor[x,y] < floor[x,y+1] and \
               floor[x,y] < floor[x,y-1]:
                   local_minima.append(floor[x,y]+1)
        
        # 4 Corners
        if x == 0 and y == 0:
            if floor[x,y] < floor[x+1,y] and floor[x,y] < floor[x,y+1]:
                local_minima.append(floor[x,y]+1)
        if x == x_max-1 and y == 0:
            if floor[x,y] < floor[x-1,y] and floor[x,y] < floor[x,y+1]:
                local_minima.append(floor[x,y]+1)
        if x == 0 and y == y_max-1:
            if floor[x,y] < floor[x+1,y] and floor[x,y] < floor[x,y-1]:
                local_minima.append(floor[x,y]+1)
        if x == x_max-1 and y == y_max-1:
            if floor[x,y] < floor[x-1,y] and floor[x,y] < floor[x,y-1]:
                local_minima.append(floor[x,y]+1)
                
        # Four edges
        if x == 0 and (y>0 and y<y_max-1):
            if floor[x,y] < floor[x+1,y] and \
                floor[x,y] < floor[x,y+1] and \
                floor[x,y] < floor[x,y-1]:
                local_minima.append(floor[x,y]+1)
        if x == x_max-1 and (y>0 and y<y_max-1):
            if floor[x,y] < floor[x-1,y] and \
                floor[x,y] < floor[x,y+1] and \
                floor[x,y] < floor[x,y-1]:
                local_minima.append(floor[x,y]+1)
        if (x>0 and x<x_max-1) and y == 0:
            if floor[x,y] < floor[x+1,y] and \
                floor[x,y] < floor[x-1,y] and \
                floor[x,y] < floor[x,y+1]:
                local_minima.append(floor[x,y]+1)
        if (x>0 and x<x_max-1) and y == y_max-1:
            if floor[x,y] < floor[x+1,y] and \
                floor[x,y] < floor[x-1,y] and \
                floor[x,y] < floor[x,y-1]:
                local_minima.append(floor[x,y]+1)
print( np.sum(local_minima) )