if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]
    max_profit = 0
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] < nums[j]:
                profit = nums[j] - nums[i]
                if max_profit < profit:
                    max_profit = profit

    print(max_profit)

    max_profit = 0
    min_price = float('inf')
    for price in nums:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    print(max_profit)
