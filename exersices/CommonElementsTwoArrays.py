from collections import defaultdict


def get_common2(vector_a, vector_b):
    if not vector_a or not vector_b:
        return []

    pos_a = 0
    pos_b = 0

    len_a = len(vector_a)
    len_b = len(vector_b)
    result = []
    while pos_a < len_a and pos_b < len_b:
        if vector_a[pos_a] == vector_b[pos_b]:
            result.append(vector_a[pos_a])
            pos_a += 1
            pos_b += 1
        elif vector_a[pos_a] > vector_b[pos_b]:
            pos_b += 1
        else:
            pos_a += 1

    return result


def get_common(vector_a, vector_b):

    if not vector_a or not vector_b:
        return []

    state = defaultdict(lambda: 0)
    result = []
    for a in vector_a:
        state[a] += 1
    for b in vector_b:
        state[b] += 1
        if state[b] == 2:
            result.append(b)

    return result


if __name__ == "__main__":
    A = [1, 3, 4, 6, 7, 9]
    B = [1, 2, 4, 5, 9, 10]
    print(get_common(A,B))

    # NOTE: The following input values will be used for testing your solution.
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    print(get_common(list_a1, list_a2))
    # common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    print(get_common(list_b1 , list_b2))
    # common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    print(get_common(list_c1, list_c2))
    # common_elements(list_b1, list_b2) should return [] (an empty list).
