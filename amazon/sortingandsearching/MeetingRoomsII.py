class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def solve(data):

    max_rooms = 0
    rooms = []
    starts_time = sorted(set(map(lambda x: x.start, data)))

    for s in starts_time:

        finished_meetings = filter(lambda x: x.end <= s, rooms)
        for meet in finished_meetings:
            rooms.remove(meet)

        meetings = filter(lambda x: x.start == s, data)

        for meet in meetings:
            data.remove(meet)
            rooms.append(meet)

        max_rooms = max(len(rooms), max_rooms)

    return max_rooms

def solve2(intervals):
    R = cnt = 0
    for t, sign in sorted([w for i in intervals for w in [(i.start, 1), (i.end, -1)]]):
        cnt += sign
        R = max(R, cnt)
    return R

if __name__ == "__main__":
    data = list()
    data.append(Interval(5, 10))
    data.append(Interval(0, 30))
    data.append(Interval(15, 20))
    #print(solve(data))

    data = list()
    data.append(Interval(0, 30))
    data.append(Interval(5, 10))
    data.append(Interval(15, 20))
    #print(solve(data) == 2)

    data = list()
    data.append(Interval(1, 5))
    data.append(Interval(8, 9))
    data.append(Interval(8, 9))
    #print(solve(data) == 2)

    data = list()
    data.append(Interval(6, 10))
    data.append(Interval(13, 14))
    data.append(Interval(12, 14))
    print(solve2(data) == 2)







