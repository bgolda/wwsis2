import itertools

print("Welcome to Tic Tac Toe game. You can play against your friend or AI.\n")
print("AI is available only for a grid size of 3.\n")
mode = int(input("Who would you like to play against (1 - friend, 2 - AI): "))
print("\nGrid size information:")
print("- Minimum playable grid size is 3")
print("- Maximum playable grid size is 15")
print("- Grid size of 3 to 5 will require 3 consecutive positions to win")
print("- Grid size of 6 to 10 will require 5 consecutive positions to win")
print("- Grid size of 10 to 15 will require 7 consecutive positions to win")

size = int(input("\nPlease enter the size of the grid: "))
#number = int(input("Please enter the winning number: "))

def print_board(board):
    for index, cell in enumerate(board, start=1):
        print("{:^3}".format(cell if cell else index), end="\n\n" if index % size == 0 else " ")

def do_turn(board, player):
    position = int(input("Player {}. Enter the position to play: ".format(player))) - 1
    if board[position] == None:
        board[position] = player
    else:
        print("You're not allowed to do that \n")
        player = next(players)

def is_draw(board):
    return all (board[position] is not None for position in range(size*size))

def has_won_grid1(board, player):
    def has_combination(combination, symbol):
        return all(board[row*size + col] == symbol for row, col in combination)
    winning_patterns = [
        lambda row, col: [(row-1, col), (row, col), (row+1, col)] if 0 < row < size-1 else None,
        lambda row, col: [(row, col-1), (row, col), (row, col+1)] if 0 < col < size-1 else None,
        lambda row, col: [(row-1, col-1), (row, col), (row+1, col+1)] if 0 < row < size-1 and 0 < col < size-1 else None,
        lambda row, col: [(row-1, col+1), (row, col), (row+1, col-1)] if 0 < row < size-1 and 0 < col < size-1 else None
    ]

    combinations = (pattern(position // size, position % size) for pattern in winning_patterns for position in range (size*size))
    return any(has_combination(combination, player) for combination in combinations if combination is not None)

def has_won_grid2(board, player):
    def has_combination(combination, symbol):
        return all(board[row*size + col] == symbol for row, col in combination)
    winning_patterns = [
        lambda row, col: [(row-2, col), (row-1, col), (row, col), (row+1, col), (row+2, col)] if 1 < row < size-2 else None,
        lambda row, col: [(row, col-2), (row, col-1), (row, col), (row, col+1), (row, col+2)] if 1 < col < size-2 else None,
        lambda row, col: [(row-2, col-2), (row-1, col-1), (row, col), (row+1, col+1), (row+2, col+2)] if 1 < row < size-2 and 1 < col < size-2 else None,
        lambda row, col: [(row-2, col+2), (row-1, col+1), (row, col), (row+1, col-1), (row+2, col-2)] if 1 < row < size-2 and 1 < col < size-2 else None
    ]

    combinations = (pattern(position // size, position % size) for pattern in winning_patterns for position in range (size*size))
    return any(has_combination(combination, player) for combination in combinations if combination is not None)

def has_won_grid3(board, player):
    def has_combination(combination, symbol):
        return all(board[row*size + col] == symbol for row, col in combination)
    winning_patterns = [
        lambda row, col: [(row-3, col), (row-2, col), (row-1, col), (row, col), (row+1, col), (row+2, col), (row+3, col)] if 2 < row < size-3 else None,
        lambda row, col: [(row, col-3), (row, col-2), (row, col-1), (row, col), (row, col+1), (row, col+2), (row, col+3)] if 2 < col < size-3 else None,
        lambda row, col: [(row-3, col-3), (row-2, col-2), (row-1, col-1), (row, col), (row+1, col+1), (row+2, col+2), (row+3, col+3)] if 2 < row < size-3 and 2 < col < size-3 else None,
        lambda row, col: [(row-3, col+3), (row-2, col+2), (row-1, col+1), (row, col), (row+1, col-1), (row+2, col-2), (row+3, col-3)] if 2 < row < size-3 and 2 < col < size-3 else None
    ]

    combinations = (pattern(position // size, position % size) for pattern in winning_patterns for position in range (size*size))
    return any(has_combination(combination, player) for combination in combinations if combination is not None)

board = [None]  * (size * size) 
players = itertools.cycle(["O", "X"])
player = next(players)
if (size > 2) & (size < 6):
    while not has_won_grid1(board, player) and not is_draw(board):
        player = next(players)
        print_board(board)
        do_turn(board, player)

    print_board(board)
    if has_won_grid1(board, player):
        print("Player {} is the winner".format(player))
    else:
        print("Game drawn")

elif (size > 5) & (size < 11):
    while not has_won_grid2(board, player) and not is_draw(board):
        player = next(players)
        print_board(board)
        do_turn(board, player)

    print_board(board)
    if has_won_grid2(board, player):
        print("Player {} is the winner".format(player))
    else:
        print("Game drawn")

elif (size > 10) & (size < 16):
    while not has_won_grid3(board, player) and not is_draw(board):
        player = next(players)
        print_board(board)
        do_turn(board, player)

    print_board(board)
    if has_won_grid3(board, player):
        print("Player {} is the winner".format(player))
    else:
        print("Game drawn")

else:
    print("Wrong grid size provided!")
