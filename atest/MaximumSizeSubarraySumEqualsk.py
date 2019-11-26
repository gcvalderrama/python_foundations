def maxSubArrayLen(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    max_len = 0
    running_sum = {0: -1}
    cur_sum = 0

    for num_index in range(len(nums)):
        num = nums[num_index]
        cur_sum += num
        if (cur_sum - k) in running_sum:
            length = num_index - running_sum[cur_sum - k]
            if length > max_len:
                max_len = length
        if cur_sum not in running_sum:
            running_sum[cur_sum] = num_index
    print(running_sum)
    return max_len
    "".index()


if __name__ == '__main__':
    #print(maxSubArrayLen([1, -1, 5, -2, 3], 3))
    #print(maxSubArrayLen([3, -1, 5, -2, 3], 3))
    #print(maxSubArrayLen([1, -1, 4, -8, 3], 3))
    #print(maxSubArrayLen([1, 4, -1, -8, 3], 3))

    v1 = "0.1.0".split('.')
    v2 = "0.0.1".split('.')


    if len(v1) < len(v2):
        for i in range(len(v2) - len(v1)):
            v1.append('0')
    elif len(v2) < len(v1):
        for i in range(len(v1) - len(v2)):
            v2.append('0')



    number1 = 0
    pivot = 1
    for i in range(len(v1) - 1, -1, - 1):
        number1 += int(v1[i]) * pivot

        pivot = pivot * 10

    number2 = 0
    pivot = 1
    for i in range(len(v2) - 1, -1, - 1):
        number2 += int(v2[i]) * pivot
        pivot = pivot * 10

    if number1 > number2:
        print(1)
    if number1 < number2:
        print(-1)
