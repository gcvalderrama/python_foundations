from collections import Counter


def most_frequent(data):
    max_number = max_count = 0
    numbers = dict()

    for i in data:
        if i not in numbers:
            numbers[i] = 1
        else:
            numbers[i] = numbers[i] + 1

        if numbers[i] > max_count:
            max_number = i
            max_count = numbers[i]

    return max_number


if __name__ == "__main__":
    data = [1, 3, 1, 3, 2, 1, 3, 3]
    print(most_frequent(data))

