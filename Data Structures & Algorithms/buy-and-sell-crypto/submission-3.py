class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        
        pastMin = prices[0]
        maxVal = 0

        for price in prices:
            pastMin = min(pastMin,price)
            maxVal = max(maxVal, price - pastMin)
        
        return maxVal