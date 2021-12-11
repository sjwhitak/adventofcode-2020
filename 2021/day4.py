import numpy as np

def check_bingo(board_mask):
    for i in range(5):
        # Vertical
        if np.all(board_mask[i,:]):
            return True
        # Horizontal
        if np.all(board_mask[:,i]):
            return True
    return False

def print_answer(board, board_mask, board_number):
    board_mask = np.squeeze(board_mask)
    board = np.squeeze(board)
    summation = np.sum(board[~board_mask])
    print(summation * board_number)
    return
        

file = open('day4','r').readlines()

# Clean format with commas
file = [line.split() for line in file]


data = file[0][0].split(",")

board_count = (len(file) - 1)//6
boards = np.array([file[b*6+2:b*6+7] for b in range(board_count)], dtype=int)
board_mask = np.zeros(boards.shape, dtype=bool)
bingo_board_mask = np.zeros(boards.shape[0], dtype=bool)

bingo_list = list()
winner_found = False

# First drawn number
for counts,count in enumerate(data):
    # numpy mask count
    count_mask = np.zeros(boards.shape[1:]) + int(count)
    
    # Check each bingo board
    for i,board in enumerate(boards):
        board_mask[i] |= board == count_mask
        bingo_board_mask[i] = check_bingo(board_mask[i])
        
    # Check if there's a bingo! -- Part 1
    if np.any(bingo_board_mask) and not winner_found:
        winner = np.where(bingo_board_mask)[0]
        winner_board = board_mask[winner].copy()
        winning_number = int(count)
        winner_found = True
        
    # Find the last board to finish -- Part 2
    if np.sum(~bingo_board_mask) == 1:
        loser = np.where(~bingo_board_mask)[0]
    if np.sum(~bingo_board_mask) == 0:
        loser_board = board_mask[loser].copy()
        losing_number = int(count)
        break
    
print_answer(boards[winner], winner_board, winning_number)
print_answer(boards[loser], loser_board, losing_number)
