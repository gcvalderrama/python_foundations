import copy
import math


def rotate_sub(i, j, n):
    return j, n - i - 1


def rotate(matrix, dim):
    rotated = copy.deepcopy(matrix)
    for i in range(dim):
        for j in range(dim):
            (new_i, new_j) = rotate_sub(i, j, dim)
            rotated[new_i][new_j] = matrix[i][j]
    return rotated


def in_rotate(given_array, n):
    for i in range(math.ceil(n/2)):
        for j in range(math.floor(n/2)):
            tmp = [-1] * 4
            (current_i, current_j) = (i, j)
            for k in range(4):
                tmp[k] = given_array[current_i][current_j]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
            for k in range(4):
                index = (k - 1) % 4
                given_array[current_i][current_j] = tmp[index]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
    return given_array


def print_board(board):
    for i in board:
        print(i)


if __name__ == "__main__":
    # NOTE: The following input values will be used for testing your solution.
    a1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    print_board(in_rotate(a1, 3))
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]

    print_board(in_rotate(a1, 3))

    a2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
    print_board(in_rotate(a2, 4))
    # [[13, 9, 5, 1],
    #  [14, 10, 6, 2],
    #  [15, 11, 7, 3],
    #  [16, 12, 8, 4]]

