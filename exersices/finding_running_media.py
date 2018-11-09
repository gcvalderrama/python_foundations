# https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/
# https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/

import math
import cProfile

class node:
    def __init__(self):
        self.value = None
        self.next_node = None
        self.previous_node = None


def runningMedian(a):
    #
    # Write your code here.
    #
    target = None
    result = list()
    number = 1

    len_left = 0
    len_right = 0
    root = None
    for c in a:
        t = node()
        t.value = c
        if not target:
            target = t
            root = target
        else:
            while True:
                if target.value <= c:
                    if target.next_node is not None and c <= target.next_node.value:
                        t.next_node = target.next_node
                        target.next_node.previous_node = t
                        target.next_node = t
                        t.previous_node = target
                        break
                    elif not target.next_node:
                        target.next_node = t
                        t.previous_node = target

                        break
                    else:
                        target = target.next_node

                if c < target.value:
                    if target.previous_node is not None and c >= target.previous_node.value:

                        t.previous_node = target.previous_node
                        target.previous_node.next_node = t
                        target.previous_node = t
                        t.next_node = target

                        break
                    elif not target.previous_node:
                        t.next_node = target
                        target.previous_node = t
                        break
                    else:
                        target = target.previous_node

            if t.value < root.value:
                len_left = len_left + 1
            else:
                len_right = len_right + 1

        if len_left - len_right == 2:
            root = root.previous_node
            len_left = len_left - 1
            len_right = len_right + 1
        elif len_right - len_left == 1:
            root = root.next_node
            len_left = len_left + 1
            len_right = len_right - 1

        if number % 2 == 0:
            result.append((root.value + root.previous_node.value) / 2)
        else:
            result.append(root.value)

        number = number + 1
        target = root

    return result


def dowork():
    inp = []
    with open('finding_media.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            inp.append(int(l))
    return runningMedian(inp)

if __name__ == "__main__":
    cProfile.run("dowork()")
    # print(dowork())

