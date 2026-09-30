class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[i] < prices[j]:
                    total = prices[j] - prices[i]
                    if total > profit:
                        profit = total

        return profit
