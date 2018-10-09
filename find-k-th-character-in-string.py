def itert(m, k, n):
    list = bin(m)[2:]

    for i in range(n):
        t = ""
        for j in range(len(list)):
            if list[j] == "0":
                t += "01"
            else:
                t += "10"
        list = t

    return (list[k])


if __name__ == "__main__":
    print(itert(5, 5, 3))
    print(itert(11, 6, 4))
