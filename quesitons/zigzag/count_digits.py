
def split_digits(number):
    target = str(number)
    return [int(x) for x in target]
    
def count_digits(numbers):
    digits = list()
    for n in numbers:
        digits.extend(split_digits(n))

    map = dict()    
    for d in digits:
        if d in map:
            map[d] += 1
        else:
            map[d] = 1
    
    items = sorted(map.items(), key=lambda x: x[1], reverse=True)    
    return [ x[0] for x in items if x[1] == items[0][1]]

if __name__ == "__main__":
    a =   [99]
    res = count_digits(a)
    print(res)
