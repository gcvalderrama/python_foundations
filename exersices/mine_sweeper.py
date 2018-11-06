
def print_board(board):
    for i in board:
        print(i)


def move(target, matrix, rows, cols, x, y):
    result = None
    if target == "top":
        if x == 0:
            return None
        else:
            result = [x - 1, y]
    elif target == "bottom":
        if x + 1 == rows:
            return None
        else:
            result = [x + 1, y]
    elif target == "left":
        if y == 0:
            return None
        else:
            result = [x, y - 1]
    elif target == "right":
        if y + 1 == cols:
            return None
        else:
            result = [x, y + 1]
    else:
        raise ValueError("target not allowed")

    if matrix[result[0]][result[1]] == -1:
        return None
    else:
        return result


def produce_board(bombs, rows, cols):
    matrix = [[0 for x in range(cols)] for y in range(rows)]

    for b in bombs:
        x = b[0]
        y = b[1]
        matrix[x][y] = -1

    for b in bombs:
        x = b[0]
        y = b[1]
        for pivot_x in range(x - 1, x + 2):
            for pivot_y in range(y - 1, y + 2):  # fix python
                if 0 <= pivot_x < rows and \
                        0 <= pivot_y < cols and \
                        matrix[pivot_x][pivot_y] != -1:
                    matrix[pivot_x][pivot_y] += 1
    return matrix


if __name__ == "__main__":
    bombs = [[0, 0], [0, 1]]  # no duplicates
    rows = 3
    cols = 4
    print_board(produce_board( bombs, rows, cols))


    # -1 -1 1 0
    # 2 2 1 0
    # 0 0 0 0




