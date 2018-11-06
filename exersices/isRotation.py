
def is_rotation(vector_a, vector_b):
    if not vector_a or not vector_b:
        return False

    if len(vector_a) != len(vector_b):
        return False

    pivot = vector_a[0]

    if pivot not in vector_b:
        return False

    index = vector_b.index(pivot)

    for i in range(len(vector_a)):
        if vector_a[i] != vector_b[(index + i) % len(vector_a)]:
            return False
    return True


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    print(is_rotation(list1, list2a))
    list2b = [4, 5, 6, 7, 1, 2, 3]
    print(is_rotation(list1, list2b))
    # is_rotation(list1, list2b) should return True.
    list2c = [4, 5, 6, 9, 1, 2, 3]
    print(is_rotation(list1, list2c))
    # is_rotation(list1, list2c) should return False.
    list2d = [4, 6, 5, 7, 1, 2, 3]
    print(is_rotation(list1, list2d))
    # is_rotation(list1, list2d) should return False.
    list2e = [4, 5, 6, 7, 0, 2, 3]
    print(is_rotation(list1, list2e))
    # is_rotation(list1, list2e) should return False.
    list2f = [1, 2, 3, 4, 5, 6, 7]
    # is_rotation(list1, list2f) should return True.
    print(is_rotation(list1, list2f))