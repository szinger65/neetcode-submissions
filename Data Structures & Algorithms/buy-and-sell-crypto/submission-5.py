class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        length = len(prices)-1
        if l == length:
            return 0
        maxprof = 0
        while l<length:
            while prices[r] > prices[l] and r<length:
                price = prices[r] - prices[l]
                if price > maxprof:
                    maxprof = price
                r += 1
            price = prices[r] - prices[l]
            if price > maxprof:
                maxprof = price
            l = r
            r = l+1
        return maxprof
        
            

        
            