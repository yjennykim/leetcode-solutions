class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[r-1] < prices[r]:
                max_profit += prices[r]-prices[r-1]
        
        return max_profit