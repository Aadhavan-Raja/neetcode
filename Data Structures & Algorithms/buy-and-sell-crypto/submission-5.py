class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        bestBuy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - bestBuy
            maxP = max(maxP, profit)
            bestBuy = min(BestBuy, prices[i])
        return maxP

