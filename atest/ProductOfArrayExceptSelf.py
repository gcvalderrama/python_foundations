def productExceptSelf(nums):
    target = 1
    for idx in range(len(nums)):
        target = target * nums[idx]

    for idx in range(len(nums)):
        nums[idx] = target / nums[idx]

    return nums

def productExceptSelf2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    output = [0] * n
    p = 1
    for idx, val in enumerate(nums):
        output[idx] = p
        p *= val

    p = 1
    for idx in range(n - 1, -1, -1):
        output[idx] *= p
        p *= nums[idx]

    return output

if __name__ == '__main__':
    # [24,12,8,6]
    print(productExceptSelf2([1, 2, 3, 4]))

    # 0 0 0
    print(productExceptSelf([4, 0, 4]))
