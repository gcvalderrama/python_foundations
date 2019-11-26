

def dowork(matrix):

    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])
    result = []
    while left < right and top < bottom:
        for i in range(left, right, 1):
            result.append(matrix[top][i])
        top += 1
        if top == bottom:
            break
        for i in range(top, bottom, 1):
            result.append(matrix[i][right-1])
        right -= 1
        if right == left:
            break
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        bottom -= 1
        if top == bottom:
            break
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1
    return result


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24]]
    # print(a[0][1:-1])
    print(dowork(a))
