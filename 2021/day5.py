import numpy as np

def parse_line(line):
    x1, mid, y2 = line.split(',')
    y1, x2 = mid.split(' -> ')
    return np.array([x1, y1, x2, y2], dtype=int)

def parse_day5(lines):
    return np.array([parse_line(line) for line in lines])


file = open('day5','r').readlines()

pipes = parse_day5(file)


# straight lines
sl = np.logical_or( (pipes[:,0] == pipes[:,2]), (pipes[:,1] == pipes[:,3]) )

pipes = pipes[sl]

# Initialize ocean floor
maxx, minx = np.max(pipes[:,(0,2)]), np.min(pipes[:,(0,2)])
maxy, miny = np.max(pipes[:,(1,3)]), np.min(pipes[:,(1,3)])

floor = np.zeros((maxx-minx+1, maxy-miny+1))

# Run through each pipe
for pipe in pipes:
    
    if pipe[0] < pipe[2]:
        dir_x = 1
    else:
        dir_x = -1
    
    if pipe[1] < pipe[3]:
        dir_y = 1
    else:
        dir_y = -1
    
    
    length_x = abs(pipe[0] - pipe[2]) + 1
    length_y = abs(pipe[1] - pipe[3]) + 1
    
    # for loop to iterate over length of pipe
    if length_x > 1:
        for i in range(length_x):
            floor[pipe[0]+i*dir_x-minx, pipe[1]-miny] += 1
    if length_y > 1:
        for i in range(length_y):
            floor[pipe[0]-minx, pipe[1]+i*dir_y-miny] += 1
    
print(np.sum( floor >= 2 ))
    