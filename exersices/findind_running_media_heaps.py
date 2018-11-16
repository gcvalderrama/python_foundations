import heapq
import copy

def runningMedian(numbers):

    left_heap = list()
    right_heap = list()

    # heapq.heapify(left_heap)
    # heapq.heapify(right_heap)

    results = list()
    results.append(numbers[0])
    count = 2
    heapq.heappush(right_heap, numbers[0])

    for num in numbers[1:]:

        b = right_heap[0]

        if num <= b:
            heapq.heappush(left_heap, -1 * num)
        else:
            heapq.heappush(right_heap, num)

        if len(left_heap) - len(right_heap) > 1:
            pivot = heapq.heappop(left_heap)
            heapq.heappush(right_heap, -1 * pivot)

        if len(right_heap) - len(left_heap) > 1:
            pivot = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -1 * pivot)

        a = -1 * left_heap[0]
        b = right_heap[0]

        if count % 2 == 0:
            results.append((a + b) / 2)
        else:
            if len(left_heap) > len(right_heap):
                results.append(a)
            else:
                results.append(b)

        count = count + 1

    return results


def dowork():
    numbers = []
    with open('finding_media.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            numbers.append(int(l))
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [12, 4, 5, 3, 8, 7]
    return runningMedian(numbers)


if __name__ == "__main__":
    print(dowork())