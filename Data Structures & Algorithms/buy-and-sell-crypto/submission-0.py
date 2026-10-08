class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_stock =  max(prices)
        for n in prices:
            min_stock = min(n,min_stock)
            prof = n - min_stock
            if n > 0:
                max_profit = max(prof,max_profit)
        return max_profit