import itertools
from functools import reduce

if __name__ == "__main__":
    horses = [1, 2, 3, 4]
    races = itertools.permutations(horses)
    pyString = 'abcdefghi'
    print(pyString[slice(1, 8, 2)])

    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x:  x ** 2, items))
    print(squared)
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

    print("###")

    print(sorted(items, key=lambda x:x, reverse=True))

    print(len(list(races)))  # 4 x 3 x 2 x 1
    print(list(itertools.combinations(horses, 3)))
    print(list(itertools.combinations_with_replacement(horses, 3)))

