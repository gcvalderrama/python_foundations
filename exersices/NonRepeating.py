
def non_repeating(data):
    state = dict()
    for i in data:
        if i not in state:
            state[i] = 1
        else:
            state[i] = state[i] + 1

    for i in data:
        if state[i] == 1:
            return i

    return None


if __name__ == "__main__":
    print(non_repeating("aaabbcdde"))
    print(non_repeating("aaabbeddc"))
    print(non_repeating("aabb"))
