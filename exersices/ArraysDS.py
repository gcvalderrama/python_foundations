#  https://www.geeksforgeeks.org/maximum-sum-hour-glass-matrix/

def hourglassSum(arr):

    size = len(arr)
    options = []
    for i in range(size):
        for j in range(size):
            points = list()
            points.append([i, j])
            points.append([i, j + 1])
            points.append([i, j + 2])
            points.append([i + 1, j + 1])
            points.append([i + 2, j])
            points.append([i + 2, j + 1])
            points.append([i + 2, j + 2])
            skip = False
            total = 0
            for p in points:
                if p[0] < size and p[1] < size:
                    total += matrix[p[0]][p[1]]
                else:
                    skip = True
                    break
            if not skip:
                options.append(total)

    return sorted(options, reverse=True)[0]



if __name__ == "__main__":
    matrix = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    print(hourglassSum(matrix))

