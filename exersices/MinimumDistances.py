
def minimumDistances(a):

    state = dict()
    min_distance = 100000
    for idx in range(len(a)):
        if a[idx] in state:
            prev = state[a[idx]]
            state[a[idx]] = idx
            distance = idx - prev
            if distance < min_distance:
                min_distance = distance
        else:
            state[a[idx]] = idx

    return min_distance
if __name__ == '__main__':
    vector = [7, 1, 3, 4, 1, 7]
    print(minimumDistances(vector))
