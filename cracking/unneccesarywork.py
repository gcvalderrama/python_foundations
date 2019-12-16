import unittest


# Example: Print all positive integer solutions to the equation a* + b* = c3  + d-1
#  where a, b, c,
# and d are integers between 1 and 1000.

def get_numbers(target):
    result = []
    for a in range(1, target + 1):
        for b in range(1, target + 1):
            for c in range(1, target + 1):
                for d in range(1, target + 1):
                    if (a ** 3 + b ** 3) == (c ** 3 + d ** 3):
                        result.append((a, b, c, d))
    return result


def get_numbers_version2(target):
    result = []
    for a in range(1, target + 1):
        for b in range(1, target + 1):
            for c in range(1, target + 1):
                d = pow(a ** 3 + b ** 3 - c ** 3, 1/3)
                if (a ** 3 + b ** 3) == c ** 3 + d ** 3:
                    result.append((a, b, c, d))

    return result


def get_numbers_version3(target):
    result = []
    state = dict()
    for c in range(1, target + 1):
        for d in range(1, target + 1):
            key = c ** 3 + d ** 3
            if key in state:
                state[key] += (c, d)
            else:
                state[key] = (c, d)

    for a in range(1, target + 1):
        for b in range(1, target + 1):
            key = a ** 3 + b ** 3
            for item in state[key]:
                result.append(item)

    return result


class Test(unittest.TestCase):

    def test_case(self):
        result = get_numbers(1000)
        print(result)

    def test_case_a(self):
        result = get_numbers_version2(1000)
        print(result)

    def test_case_b(self):
        result = get_numbers_version3(1000)
        print(result)


