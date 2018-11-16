
def migratoryBirds(arr):
    max_item = 0
    max_index = 0
    state = {}
    for item in arr:
        if item not in state:
            state[item] = 1
        else:
            state[item] += 1
            if max_item < state[item]:
                max_item = state[item]
                max_index = item

    print(sorted(state.items(), key=lambda x: x[1], reverse=True))

    return max_index

if __name__ == '__main__':
    with open('birds.txt', 'r') as f:
        arr = list(map(int, f.readline().rstrip().split()))
        t = 0
        c = 0
        for i in arr:
            if i == 3:
                t +=1
            if i == 4:
                c +=1

        print(migratoryBirds(arr))
