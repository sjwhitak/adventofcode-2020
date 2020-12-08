# Part 1 -- down 1, left 3
import numpy as np

with open('day3', 'r') as fd: # read file
    out = fd.read().splitlines()      # str
    
left_position = 0
down_position = 0
left_size = len(out[0])
counter = 0
while down_position < len(out):
    # Wrap around
    if left_position >= left_size:
        left_position -= left_size
    
    position = out[down_position][left_position]
    
    if position == '#':
        counter += 1
    
    # print(position)
    
    left_position += 3
    down_position += 1
    #%%
# Part 2 : (left,down): (1,1) and (3,1) and (5,1) and (7,1) and (1,2)
import numpy as np

def calc_day3(left, right, out):
    left_position = 0
    down_position = 0
    left_size = len(out[0])
    counter = 0
    while down_position < len(out):
        # Wrap around
        if left_position >= left_size:
            left_position -= left_size
        
        position = out[down_position][left_position]
        
        if position is '#':
            counter += 1
        
        print(position)
        
        left_position += left
        down_position += right
    return counter
        
with open('day3', 'r') as fd: # read file
    out = fd.read().splitlines()      # str

c1 = calc_day3(1,1,out)
c2 = calc_day3(3,1,out)
c3 = calc_day3(5,1,out)
c4 = calc_day3(7,1,out)
c5 = calc_day3(1,2,out)
answer = c1*c2*c3*c4*c5