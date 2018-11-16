if __name__ == '__main__':

    digits = "234"

    def muls(lm, ln):
        ln = list(ln)
        q = []
        for i, m in enumerate(lm):
            q.extend([m + x for x in ln])
        return q


    pm = []
    dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    for i, v in enumerate(digits):
        if i == 0:
            pm = list(dic[int(v)])
        else:
            pm = muls(pm, dic[int(v)])
    print(pm)
