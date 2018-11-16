if __name__ == "__main__":
    vector = [1, 2, 3, 4, 5]
    n = len(vector)
    d = 4
    rd = n - d
    result = [0] * n
    for idx in range(n):
        nidx = (idx + rd) % n
        result[nidx] = vector[idx]

    print(result)

    llist = SinglyLinkedList()






