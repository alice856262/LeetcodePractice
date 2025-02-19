# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock. 
# 
#  Return the maximum profit you can achieve from this transaction. If you 
# cannot achieve any profit, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you 
# must buy before you sell.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming 👍 32255 👎 1231


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the minimum price and maximum profit
        min_price = float('inf')  # Start with an infinite value for the minimum price
        max_profit = 0  # Start with zero profit

        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if the stock is sold at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit

    ### Brute Force --> time limit exceed error for large input sizes
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = []
    #     for i in range(len(prices)):
    #         for j in range(i, len(prices)):
    #             profit.append(prices[j] - prices[i])
    #     max = 0
    #     for i in profit:
    #         if i > max:
    #             max = i
    #     return max
# leetcode submit region end(Prohibit modification and deletion)
