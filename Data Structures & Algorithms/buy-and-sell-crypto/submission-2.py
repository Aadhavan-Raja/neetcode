class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        r = len(prices) -1
        while l < r:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
            if prices[l+1] < prices[l]:
                l += 1
            else:
                r -= 1
        return maxP