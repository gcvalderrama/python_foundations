import unittest
# ex. input interger 1234, return "1234" in string or characters
# Given a integer , return corresponding ASCII char representation without using language building in feature.


def int_to_ascci(target):
    if target < 10:
        return ord(target)

    result = []
    temp = target
    res = 0
    while temp > 0:
        res = temp % 10
        temp = (temp - res) / 10
        result.append(str(ord(str(int(res)))))

    return "".join(result[::-1])


class Test(unittest.TestCase):

    def test(self):
        result = int_to_ascci(1234)
        print(result)

    def test(self):
        result = int_to_ascci(1230)
        print(result)

