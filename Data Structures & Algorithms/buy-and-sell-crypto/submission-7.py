class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMinimum = prices[0]
        profit = 0

        for price in prices:
            if price < currentMinimum:
                currentMinimum = price
            else:
                currentProfit = price - currentMinimum

                if currentProfit > profit:
                    profit = currentProfit

        return profit
