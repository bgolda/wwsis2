import itertools

size = int(input("Please enter the size of the grid: "))
number = int(input("Please enter the winning number: "))
numbers = []
numbers.append(number)
print(numbers)

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

def has_won(board, player):
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