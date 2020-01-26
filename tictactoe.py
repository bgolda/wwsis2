import itertools

size = 3

def print_board(board):
    for index, cell in enumerate(board, start=1):
        print("{:^3}".format(cell if cell else index), end="\n\n" if index % size == 0 else " ")

def do_turn(board, player):
    position = int(input("Player {}. Enter the position to play: ".format(player))) - 1
    board[position] = player

def is_draw(board):
    return all (board[position] is not None for position in range(size*size))

def has_won(board, player):
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

board = [None]  * (size * size) 
players = itertools.cycle(["O", "X"])
player = next(players)
while not has_won(board, player) and not is_draw(board):
    player = next(players)
    print_board(board)
    do_turn(board, player)

print_board(board)
if has_won(board, player):
    print("Player {} is the winner".format(player))
else:
    print("Game drawn")