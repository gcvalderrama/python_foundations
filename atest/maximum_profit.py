import unittest


def max_profit_function(array):
    max_profit = -1
    buy_price = 0
    sell_price = 0

    change_buy_index = True
    for index in range(len(array)-1):
        sell_price = array[index + 1]
        if change_buy_index:
            buy_price = array[index]
        if sell_price < buy_price:
            change_buy_index = True
            continue
        else:
            temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit

            change_buy_index = False

    return max_profit


class Test(unittest.TestCase):

    def test_case(self):
        price = [100, 180, 260, 310, 40, 535, 695]
        result = max_profit_function(price)
        self.assertEqual(655, result)

    def test_case_b(self):
        price = [310, 40, 535, 695, 10]
        result = max_profit_function(price)
        self.assertEqual(655, result)


if __name__ == "__main__":
    pass
