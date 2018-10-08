def sort(list):
    for iter_number in range(len(list) - 1, 0, -1):
        for idx in range(iter_number):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

if __name__ == "__main__":

    list = [19, 2, 31, 45, 6, 11, 121, 27]
    sort(list)
    print(list)

    list = [121, 100, 90, 80, 70, 50, 41, 2]
    sort(list)
    print(list)