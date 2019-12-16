import unittest


def rotate(matrix, r, c):

    new = [[0 for j in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            new[j][r - (i + 1)] = matrix[i][j]

    return new

    # i = j
    # 4 - (i + 1)



class Test(unittest.TestCase):

    def test_rotate(self):
        matrix = [
                  [1,   2,  3,  4],  # 0,0  0,1  0,2  0,3
                  [5,   6,  7,  8],  # 1,0  1,1  1,2  1,3
                  [9,  10, 11, 12],  # 2,0  2,1  2,2  2,3
                  [13, 14, 15, 16],  # 3,0  3,1  3,2  3,3
                 ]

        expected =[
                    [13,  9, 5, 1], #  0,3  1,3  2,3  3,3
                    [14, 10, 6, 2], #  0,2  1,2  2,2  3,2
                    [15, 11, 7, 3], #  0,1  1,1  2,1  3,1
                    [16, 12, 8, 4]  #  0,0  1,0  2,0  3,0
                  ] # 0,0  1,0  2,0
        result = rotate(matrix, 4, 4)

        self.assertEqual(expected, result)

        

