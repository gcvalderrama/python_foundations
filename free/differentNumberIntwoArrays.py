import unittest


class Test(unittest.TestCase):

    def test_case(self):
        
        ar = [2, 3, 5, 4, 5, 3, 4]
        res = ar[0]
        for i in range(1, len(ar)):
            res = res ^ ar[i]
            print(res)



if __name__ == '__main__':
    unittest.main()