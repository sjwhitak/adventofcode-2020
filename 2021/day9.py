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


def basin_count(mask, position):
    valid_positions = [position]
    x_max = len(mask[:,0])
    y_max = len(mask[0,:])
    count = 1
    
    mask[position[0], position[1]] = False
    
    while True:
        # End when you're done with all available positions to search
        if len(valid_positions) == 0:
            return count, mask
        
        # Start at most recent position
        x, y = valid_positions[0]
        

        
        # Look at 4 surrounding areas
        for dx, dy in adjacents:
            if x+dx >= 0 and x+dx < x_max and y+dy >= 0 and y+dy < y_max:
                
                # Is it a possible area?
                if mask[x+dx, y+dy]:

                            
                    # It's a valid position! Save it and remove from search
                    # capabilities.
                    mask[x+dx, y+dy] = False
                    count += 1
                    valid_positions.append((x+dx, y+dy))
                            
                                 
        # Move to the next position
        valid_positions.pop(0)
        
# Part 2 -- map out sizes of surrounding contours with 9 being boundary
floor_mask = floor != 9

# Search each position for a basin
basin_sizes = list()
for x in range(x_max):
    for y in range(y_max):
        if floor_mask[x,y]:
            size, floor_mask = basin_count(floor_mask, (x,y))
            basin_sizes.append(size)

max_3 = sorted(basin_sizes)[-3:]
print(max_3[0] * max_3[1] * max_3[2])