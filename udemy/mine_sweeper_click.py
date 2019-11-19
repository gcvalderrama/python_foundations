import queue


def click_internal(field, num_rows, num_cols, given_i, given_j):

    field[given_i][given_j] = -2

    for i in range(given_i - 1, given_i + 2):
        for j in range(given_j - 1, given_j + 2):
            if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] == 0:
                click_internal(field, num_rows, num_cols, i, j)


def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] != 0:
        return field
    click_internal(field, num_rows, num_cols, given_i, given_j)
    return field


def click2(field, num_rows, num_cols, given_i, given_j):

    to_check = queue.Queue()
    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
        to_check.put((given_i, given_j))
    else:
        return field
    while not to_check.empty():
        (current_i, current_j) = to_check.get()
        for i in range(current_i - 1, current_i + 2):
            for j in range(current_j - 1, current_j + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols
                        and field[i][j] == 0):
                    field[i][j] = -2
                    to_check.put((i, j))
    return field


def print_board(board):
    for i in board:
        print(i)


if __name__ == "__main__":

    print( 5 % 4)

    field = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, -1, 1, 0]]
    print_board(click(field, 3, 5, 0, 0))

    field1 = [[0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, -1, 1, 0]]

    print("########")
    print_board(click(field1, 3, 5, 2, 2))
    # [[0, 0, 0, 0, 0],
    #  [0, 1, 1, 1, 0],
    #  [0, 1, -1, 1, 0]]
    print("########")
    print_board(click(field1, 3, 5, 1, 4))
    # [[-2, -2, -2, -2, -2],
    #  [-2, 1, 1, 1, -2],
    #  [-2, 1, -1, 1, -2]]

    field2 = [[-1, 1, 0, 0],
              [1, 1, 0, 0],
              [0, 0, 1, 1],
              [0, 0, 1, -1]]

    print("########")
    print_board(click(field2, 4, 4, 0, 1))
    # [[-1, 1, 0, 0],
    #  [1, 1, 0, 0],
    #  [0, 0, 1, 1],
    #  [0, 0, 1, -1]]
    print("########")
    print_board(click(field2, 4, 4, 1, 3))
    # [[-1, 1, -2, -2],
    #  [1, 1, -2, -2],
    #  [-2, -2, 1, 1],
    #  [-2, -2, 1, -1]]
