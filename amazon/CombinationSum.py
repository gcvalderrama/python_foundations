import heapq

if __name__ == '__main__':

    candidates =[2,3,6,7]
    target = 7

    res = []
    resList = []

    heapq.heappop()
    def backtracking(start, rest):
        if rest == 0:
            temp = resList[:]
            res.append(temp)
        for i in range(start, len(candidates)):
            if (candidates[i] <= rest):
                resList.append(candidates[i])
                backtracking(i, rest - candidates[i])
                resList.pop()

    backtracking(0, target)
    print(res)
