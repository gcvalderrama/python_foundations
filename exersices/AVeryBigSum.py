import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
from collections import deque


def aVeryBigSum(ar):
    result = []

    for item in ar:
        tmp = [int(c) for c in str(item)]
        idx_result = len(result) - 1
        idx_tmp = len(tmp) - 1
        c = 0
        target = deque()
        while idx_result >= 0 or idx_tmp >= 0:
            a = 0
            b = 0
            if idx_tmp >= 0:
                a = tmp[idx_tmp]
            if idx_result >= 0:
                b = result[idx_result]

            if a + b + c > 9:
                res = (a + b + c) % 10
                c = (a + b + c) // 10
                target.appendleft(res)
            else:
                target.appendleft(a + b + c)
                c = 0
            idx_result -= 1
            idx_tmp -= 1

        if c:
            target.appendleft(c)

        result = list(target)

    t = ''.join([str(c) for c in result]).lstrip('0')
    return t


if __name__ == '__main__':

    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    ar = [10, 1001458909, 1004570889, 1007019111, 1003302837, 1002514638, 1006431461,
          1002575010, 1007514041, 1007548981, 1004402249]
    result = aVeryBigSum(ar)
    print(10047338126)
    print(result)

