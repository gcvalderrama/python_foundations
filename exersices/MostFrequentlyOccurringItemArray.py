from collections import Counter


def most_frequent(data):
    if not data:
        return None
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

    # most_frequent(list1) should return 1
    list1 = [1, 3, 1, 3, 2, 1]
    print(most_frequent(list1))
    # most_frequent(list2) should return 3
    list2 = [3, 3, 1, 3, 2, 1]
    print(most_frequent(list2))
    # most_frequent(list3) should return None
    list3 = []
    print(most_frequent(list3))
    # most_frequent(list4) should return 0
    list4 = [0]
    print(most_frequent(list4))
    # most_frequent(list5) should return -1
    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    print(most_frequent(list5))

