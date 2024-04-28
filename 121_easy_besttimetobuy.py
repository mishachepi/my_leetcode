"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_diff = 0
        prices_len = len(prices)
        i = 0
        while(i < prices_len - 1):
            if prices[i] >= prices[i + 1]:
                i += 1
                continue
            n = i + 1
            tmp_diff = prices[n] - prices[i]
            while(n < prices_len - 1):
                if prices[n] <= prices[n + 1]:
                    n += 1
                    continue
                new_diff = prices[n] - prices[i]
                if max_diff < new_diff:
                    max_diff = new_diff
                n += 1
            if prices[n - 1] < prices[n]:
                tmp2_diff = prices[n] - prices[i]
                if max_diff < tmp2_diff:
                    max_diff = tmp2_diff
            if max_diff < tmp_diff:
                max_diff = tmp_diff
            i += 1
        return max_diff
