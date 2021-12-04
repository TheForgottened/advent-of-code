numbers_to_draw = []
drawn_numbers = []
boards = []

# Returns -1 if the board hasn't won (yet)
def get_board_score(board, drawn_numbers):
    side_size = 5
    flag = True

    for i in range(side_size):
        flag = True

        # Check line
        for j in range(side_size):
            if (board[(i * side_size) + j] not in drawn_numbers): flag = False

        # If the line is a winner
        if (flag == True): break

        flag = True

        # Check column
        for j in range(side_size):
            if (board[i + (j * side_size)] not in drawn_numbers): flag = False

        # If the column is a winner
        if (flag == True): break

    if (flag == True):
        fixed_board =  [0 if n in drawn_numbers else n for n in board]       
        return sum(fixed_board) * drawn_numbers[-1]

    return -1

with open('input.txt', 'r') as f:
    raw_numbers_to_draw = f.readline().split(',')
    numbers_to_draw = [int(n) for n in raw_numbers_to_draw]

    raw_board = ""
    i = 0
    for line in f:
        if (line == '\n'): 
            continue

        raw_board += line
        i += 1

        if (i % 5 == 0):
            board = [int(n) for n in raw_board.split()]
            boards.append(board)
            raw_board = ""

last_winning_board = []
last_winning_board_score = 0
while numbers_to_draw:
    drawn_numbers.append(numbers_to_draw.pop(0))

    i = 0
    while i < len(boards):
        board_score = get_board_score(boards[i], drawn_numbers)

        if (board_score != -1): 
            last_winning_board = boards[i]
            last_winning_board_score = board_score
            boards.pop(i)
        else:
            i += 1

i = 0
for n in last_winning_board:
    print(str(n) + "\t", end =" ")
    i += 1

    if (i % 5 == 0): print("")

print("Score: " + str(last_winning_board_score))
