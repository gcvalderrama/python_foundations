
def diagonalDifference(arr):
    a = 0
    b = 0
    lenght = len(arr) - 1
    for i in range(len(arr)):
        a += matrix[i][i]
        b += matrix[i][lenght - i]

    return abs(a - b)

if __name__ == '__main__':

    parts = "12:45:54PM".split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2][:2])
    if parts[2][2:] == "PM" and hours < 12:
        hours = (hours + 12)
    else:
        hours = hours % 12
    print("{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds))


    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]

    print(diagonalDifference(matrix))
