def solve(x, min_value, max_value):
    result = 0
    for item in range(min_value + 1, max_value):
        for digit in str(item):
            if int(digit) == x:
                result += 1
    return result


if __name__ == "__main__":
    print(solve(3, 100, 250))  # 35
    print(solve(2, 10000, 12345))  # 1120
    print(solve(0, 20, 21))  # 0
    print(solve(9, 899, 1000))  # 0
    print(solve(1, 1100, 1345))  # 0
