board = [
    [3, 0, 0, 1, 0, 0, 0, 2, 0],
    [4, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 9, 2, 6, 0, 0, 8, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 1, 0, 6, 0, 0, 4, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 7],
    [0, 0, 9, 0, 0, 1, 4, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 6, 0, 5, 0, 0, 1, 0]
]


def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):

        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def create_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - - - -")
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print("", bo[row][col])
            else:
                print(f" {bo[row][col]} ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)
    
    return None

create_board(board)
solve(board)
print("\n- - - - - - - - - - - - - - - - - - - - - - -\n")
create_board(board)