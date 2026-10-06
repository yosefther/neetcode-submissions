class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i , j = 0 , 1 
        maxP = 0          
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxP = max(maxP , profit)
            else :
                i = j
            j= 1 + j 
        return maxP