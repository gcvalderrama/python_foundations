import unittest


def is_number(c):
    try:
        number = int(c)
        return True
    except:
        return False


def is_compressed(target):
    pivot = 1
    for c in target[1:]:
        if is_number(c):
            pivot -= 1
        else:
            pivot += 1

    return pivot == 0


def compress(target):

    if not target:
        return ""
    if len(target) == 1:
        return target

    if not is_compressed(target):
        temp = target[0]
        count = 1
        result = ""

        for c in target[1:]:

            if c == temp:
                count += 1
            else:
                result += "{}{}".format(temp, count)
                temp = c
                count = 1

        result += "{}{}".format(temp, count)

        return result
    else:
        result = ""
        factor = ""
        previous = target[0]
        for c in target[1:]:
            if is_number(c):
                factor += c
            else:
                result += previous * int(factor)
                previous = c
                factor = ""

        result += previous * int(factor)

        return result


class Test(unittest.TestCase):

    def test_compress(self):
        result = compress("aaabbbccd")
        self.assertEqual("a3b3c2d1", result)

        result = compress("aaabbbccdd")
        self.assertEqual("a3b3c2d2", result)

        result = compress(result)
        self.assertEqual("aaabbbccdd", result)
