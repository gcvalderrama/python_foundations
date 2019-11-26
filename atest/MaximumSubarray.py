if __name__ == '__main__':
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    for i in range(1, len(input)):
        t = input[i-1]
        if t > 0:
            input[i] += t

    print (max(input))