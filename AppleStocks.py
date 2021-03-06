"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am
local time. The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday.

No "shorting" - you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).

"""

# Solution 1: Brute force - try every combination, keep track of max

"""Returns the maximum profit
    >>> get_max_profit_1([10, 7, 5, 8, 11, 9])
    6
"""


def get_max_profit_1(prices):
    # assign a max profit variable to
    max_profit = 0

    # iterate through list of prices, keep track of index, too
    for idx, buy_price in enumerate(prices):
        # calculate profits for prices after current price
        for sell_price in prices[idx+1:]:
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Analysis:
# Runtime O(n) to run through buy_prices, and O(n-1) for sell prices.
# Still O(n^2) for nested loop.


# Solution 2:
def get_max_profit_2(prices):

    # instantiate variables to track min price, max profit
    min_price = prices[0]
    max_profit = 0

    # iterate over list ONCE
    for price in prices:
        # make sure we're buying at the lowest price we've seen so far
        if price < min_price:
            min_price = price
        # or: min_price = min(min_price, price)
        # calculate potential profit from current price
        profit = price - min_price
        # keep track of profit
        if profit > max_profit:
            max_profit = profit
        # or: max_profit = max(max_profit, profit)

    return max_profit

# Analysis:
# Runtime is O(n) b/c we go through the list only once.


def get_max_profit_3(prices):
    min_price = prices[0]
    max_price = prices[0]
    if len(prices) <= 1:  # Edge Case 2
        raise ValueError("Evaluating profit requires atleast 2 data points")


    for price in prices:
        min_price = min(price, min_price)
        max_price = max(price, max_price)

    profit = max_price - min_price
    if profit <= 0:
        print(f"We shouldn't trade because profit is: {profit}")
    return profit

# Analysis:
# Runtime is O(n) b/c we go through the list only once.
# Spacetime is O(1) we use existing array "prices" to work with

"""
EDGE CASES:
1. Negative profit - meaning that share prices only went down (we shouldn't sell)
2. Only 1 data point - we can't find profit with only one data point
"""


def get_max_profit_4(prices):  # Solve Edge Case 1

    if len(prices) <= 1:  # Edge Case 2
        raise ValueError("Evaluating profit requires atleast 2 data points")

    # min price will be the first price of the day. max_profit will be the first profit we can calculate
    min_price = prices[0]
    max_price = prices[1]
    max_profit = prices[1] - prices[0]

    # calculate and roll through to find current profits of stock prices
    for price in prices:
        min_price = min(min_price, price)
        max_price = max(max_price, price)
        profit = max_price - min_price

    if max_price == prices[0]:  # if max price is the maximum it means the stock price has only gone down. (Edge case 2)
        print(f"Do not sell today because max profit is {max_profit}")
        return max_profit
    print("We should sell.")
    return profit



ans = get_max_profit_4([9, 7, 4, 1])
print(ans)


# Tests

import unittest
class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit_4([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit_4([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit_4([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit_4([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit_4([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit_4([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit_4([1])


unittest.main(verbosity=2)