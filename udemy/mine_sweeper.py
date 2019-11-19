
def print_board(board):
    for i in board:
        print(i)


def produce_board(bombs, rows, cols):
    matrix = [[0 for x in range(cols)] for x in range(rows)]

    for b in bombs:
        x = b[0]
        y = b[1]
        matrix[x][y] = -1

    for b in bombs:
        x = b[0]
        y = b[1]
        for pivot_x in range(x - 1, x + 2):
            for pivot_y in range(y - 1, y + 2):  # fix python
                if 0 <= pivot_x < rows and 0 <= pivot_y < cols and matrix[pivot_x][pivot_y] != -1:
                    matrix[pivot_x][pivot_y] += 1
    return matrix


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


if __name__ == "__main__":
    bombs = [[0, 0], [0, 1]]  # no duplicates
    rows = 3
    cols = 4
    print_board(produce_board(bombs, rows, cols))

    print("#############")
    # NOTE: The following input values will be used for testing your solution.
    print_board(produce_board([[0, 2], [2, 0]], 3, 3))
    # [[0, 1, -1],
    #  [1, 2, 1],
    #  [-1, 1, 0]]
    print("#############")
    print_board(produce_board([[0, 0], [0, 1], [1, 2]], 3, 4))
    # [[-1, -1, 2, 1],
    #  [2, 3, -1, 1],
    #  [0, 1, 1, 1]]
    print("############# Last")
    print_board(produce_board([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))
    # [[1, 2, 2, 1, 0],
    #  [1, -1, -1, 2, 0],
    #  [1, 3, -1, 2, 0],
    #  [0, 1, 2, 2, 1],
    #  [0, 0, 1, -1, 1]]





