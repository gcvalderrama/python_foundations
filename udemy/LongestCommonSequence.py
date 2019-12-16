import unittest


def recursive(p, q, m, n, state):
    if state[m][n] != -1:
        return state[m][n]
    if m == -1 or n == -1:
        result = 0
    elif p[m] == q[n]:
        result = 1 + recursive(p, q, m - 1, n - 1, state)
    else:
        temp1 = recursive(p, q, m-1, n, state)
        temp2 = recursive(p, q, m, n-1, state)
        result = max(temp1, temp2)
    state[m][n] = result
    return result


def LCS(p, q):
    state = [[-1 for i in range(len(q))] for j in range(len(p))]
    return recursive(p, q, len(p)-1, len(q)-1, state)


class Test(unittest.TestCase):

    def test_case(self):
        result = LCS("BATD", "ABACD")
        self.assertEqual(3, result)



