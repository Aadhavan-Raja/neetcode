class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        bestBuy = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[bestBuy]
            maxP = max(maxP, profit)
            if prices[i] < prices[bestBuy]:
                bestBuy = i
        return maxP
