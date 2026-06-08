from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        best_profit = 0

        for price in prices:
            profit = price - lowest_buy
            if profit > best_profit:
                best_profit = profit
            
            if price < lowest_buy:
                lowest_buy = price
        
        return best_profit

sol = Solution()

prices = [10,1,5,6,7,1]
prices2 = [10,8,7,5,2]

print(sol.maxProfit(prices))