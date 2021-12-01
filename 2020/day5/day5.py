
    
def split_half(position, half):
    N = position.shape[0]
    assert(half == 'Upper' or half == 'Lower')
    assert(N > 1)
    
    
    split = int(N/2)
    if half == 'Lower':
        position = position[:split]
    elif half == 'Upper':
        position = position[-split:]
    return position
        
    
def find_row(string):
    assert(len(string) == 7)
    
    positions = np.arange(0,128,1)
    
    for s in string:
        
        if s == 'F':
            positions = split_half(positions, 'Lower')
        if s == 'B':
            positions = split_half(positions, 'Upper')
    return positions

def find_column(string):
    assert(len(string) == 3)
    
    positions = np.arange(0,8,1)
    
    for s in string:
        
        if s == 'L':
            positions = split_half(positions, 'Lower')
        if s == 'R':
            positions = split_half(positions, 'Upper')
    return positions    


if __name__ == '__main__':

    import numpy as np
    with open('day5', 'r') as fd: # read file
        out = fd.read().splitlines()      # str
        
    max_ID = 0
    seat_IDs = np.zeros((len(out),1)).astype(np.int)
    i = 0
    for line in out:
        row = find_row(line[:7])
        column = find_column(line[-3:])
        
        
        # Part 2
        ID = row*8 + column
        seat_IDs[i] = int(ID)
        i += 1
        
        # Part 1
        if ID > max_ID:
            max_ID = ID
            
    # Part 2 cont.
    # Sort the IDs
    sorted_IDs = np.array(sorted(seat_IDs))         # All should be 1,2,3,4... 
    difference = sorted_IDs[1:] - sorted_IDs[:-1]   # Should be 1,1,1,1,1,1...
    position = np.where(difference != 1)[0]         # Find the discrepency
    
    your_ID = (sorted_IDs[position] + sorted_IDs[position+1])/2 # Middle of two