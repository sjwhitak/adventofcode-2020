import numpy as np

def check_bingo(board_mask):

        
    
    for i in range(5):
        # Vertical
        if np.all(board_mask[i,:]):
            return True
        # Horizontal
        if np.all(board_mask[:,i]):
            return True    
        
    # Diagonal
    # mask1 = np.zeros((5,5), dtype=bool)
    # mask2 = np.zeros((5,5), dtype=bool)
    # for i in range(5):
    #     mask1[i,i] = True
    #     mask2[i,-(i+1)] = True        
    # if np.array_equal(mask1, np.logical_and(mask1, board_mask)):
    #     return True
        
    # if np.array_equal(mask2, np.logical_and(mask2, board_mask)):
    #     return True
    
    return False
        

file = open('day4','r').readlines()

# Clean format with commas
file = [line.split() for line in file]


data = file[0][0].split(",")

board_count = (len(file) - 1)//6
boards = np.array([file[b*6+2:b*6+7] for b in range(board_count)], dtype=int)
board_mask = np.zeros(boards.shape, dtype=bool)
bingo_board_mask = np.zeros(boards.shape[0], dtype=bool)

# First drawn number
for counts,count in enumerate(data):
    # numpy mask count
    count_mask = np.zeros(boards.shape[1:]) + int(count)
    
    # Check each bingo board
    for i,board in enumerate(boards):
        board_mask[i] |= board == count_mask
        bingo_board_mask[i] = check_bingo(board_mask[i])
        
    # Check if there's a bingo!
    if np.any(bingo_board_mask):
        print( np.where(bingo_board_mask)[0] )
        break
    
# Choose the board
bingo_board = np.squeeze(boards[np.where(bingo_board_mask)])

# Invert mask, then sum
bingo_mask  = bingo_board[np.squeeze(~board_mask[bingo_board_mask])]
answer = np.sum(bingo_mask)*int(count)
