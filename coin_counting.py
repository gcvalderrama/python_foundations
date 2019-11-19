#  https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html

import unittest


def basic_small_change(denom, total_amount):

    if total_amount in denom:
        return 1

    sorted_denominations = sorted(denom, reverse=True)
    number_of_denoms = []
    for i in sorted_denominations:
        div = total_amount // i
        total_amount = total_amount % i
        if div > 0:
            number_of_denoms.append((i, div))

    return number_of_denoms


def recursive_solution(denom, total_amount):
    min_coin = total_amount
    if total_amount in denom:
        return 1
    else:
        for i in [c for c in denom if c < total_amount]:
            num_coin = 1 + recursive_solution(denom, total_amount - i)
            if num_coin < min_coin:
                min_coin = num_coin
    return min_coin


def recursive_solution_with_dp(denom, total_amount, known_results):
    min_coin = total_amount
    if total_amount in denom:
        known_results[total_amount] = 1
        return 1

    elif total_amount in known_results:
        return known_results[total_amount]

    else:
        for i in [c for c in denom if c <= total_amount]:
            num_coin = 1 + recursive_solution_with_dp(denom, total_amount-i, known_results)
            if num_coin < min_coin:
                min_coin = num_coin
                known_results[total_amount] = min_coin

    return min_coin


def dp_make_change(coin_list, change, min_coins):
    for cents in range(change+1):
        coin_count = cents
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j]+1
        min_coins[cents] = coin_count

    return min_coins[change]


def dp_make_change_v2(coin_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1

        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j]+1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin

    return min_coins[change]


def optimal_small_changes(denom, total_amount):
    if total_amount in denom:
        return 1

    sorted_denominations = sorted(denom, reverse=True)

    series = []

    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]
        number_of_denoms = []
        local_total = total_amount
        for i in [c for c in term if c <= local_total]:
            div = local_total // i
            local_total = local_total % i
            if div > 0:
                number_of_denoms.append((i, div))
        if local_total == 0:
            series.append(number_of_denoms)

    return sorted(series, key=lambda x: sum(pair[1] for pair in x))[0]




class Test (unittest.TestCase):

    def test_case_a(self):
        result = basic_small_change([1, 5, 8], 10)
        self.assertEqual([(8, 1), (1, 2)], result)

    def test_case_b(self):
        result = optimal_small_changes([1, 5, 8], 10)
        self.assertEqual([(5, 2)], result)

    def test_case_c(self):
        result = basic_small_change([1, 5, 10, 21, 25], 63)
        self.assertEqual([(25, 2), (10, 1), (1, 3)], result)

    def test_case_d(self):
        # result = recursive_solution([1, 5, 10, 21, 25], 63) very expensive
        #result = recursive_solution_with_dp([1, 5, 10, 21, 25], 63, dict())
        result = optimal_small_changes([1, 5, 10, 21, 25], 63)
        self.assertEqual([(21, 3)], result)

    def test_case_e(self):
        temp = dict()
        result = dp_make_change([1, 5, 10, 21, 25], 63, temp)
        self.assertTrue(3, result)

    def test_case_f(self):
        temp = dict()
        used = dict()
        result = dp_make_change_v2([1, 5, 10, 21, 25], 63, temp, used)
        self.assertTrue(3, result)
        coin = 63
        while coin > 0:
            thisCoin = used[coin]
            print(thisCoin)
            coin = coin - thisCoin
            # print(used)







if __name__ == "__main__":
    unittest.main()
