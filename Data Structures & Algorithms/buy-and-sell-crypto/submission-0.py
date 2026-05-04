class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProf = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProf = max(maxProf, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return maxProf