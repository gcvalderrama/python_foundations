# Python program to rotate a matrix

def rotate_recursive(matrix):
    if not len(matrix):
        return matrix
    rows = len(matrix)
    if rows < 2:
        return matrix
    if len(matrix[0]) < 2:
        return matrix

    rotate_recursive(matrix)

    rows = len(sample)
    columns = len(sample[0])

    #sample_without_rows = (sample[:-1])[1:]

    mm = [0] * (rows - 2)
    for i in range(1, rows-1, 1):
        mm[i-1] = [0] * (columns-2)
        for j in range(1, columns -1, 1):
            mm[i-1][j-1] = sample[i][j]




    return matrix


def rotate_matrix_left(mat):
    if not len(mat):
        return

    """ 
            top : starting row index 
            bottom : ending row index 
            left : starting column index 
            right : ending column index 
    """

    top = 0
    bottom = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1

    while left < right and top < bottom:
        pass


def rotateMatrix(mat):
    if not len(mat):
        return

    """ 
        top : starting row index 
        bottom : ending row index 
        left : starting column index 
        right : ending column index 
    """

    top = 0
    bottom = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1

    while left < right and top < bottom:

        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top + 1][left]

        # Move elements of top row one step right
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat

def rotate_matrix(data, rows, columns):

    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = [0] * columns

    temp = data.split(" ")
    it = 0
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = temp[it]
            it = it + 1
    print(matrix)
    return rotateMatrix(matrix)

# Utility Function
def printMatrix(mat):
    for row in mat:
        print(row)


if __name__ == "__main__":

    sample = [[1,2,3,4],[4,5,6,4],[4, 5, 6, 4],[7,8,9,1]]

    tt = (sample[:-1])[1:]

    tt[0][0] = 10
    print("===")
    printMatrix(tt)
    print("===")
    printMatrix(sample)


    print("===")

    rows = len(sample)
    columns = len(sample[0])

    #sample_without_rows = (sample[:-1])[1:]

    mm = [0] * (rows - 2)
    for i in range(1, rows-1, 1):
        mm[i-1] = [0] * (columns-2)
        for j in range(1, columns -1, 1):
            mm[i-1][j-1] = sample[i][j]

    print(mm)

    # 1234
    # 4564
    # 7894

    # 1234
    # 4565
    # 7895

    #print(len(m))
