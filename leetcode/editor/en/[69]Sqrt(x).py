# Given a non-negative integer x, return the square root of x rounded down to 
# the nearest integer. The returned integer should be non-negative as well. 
# 
#  You must not use any built-in exponent function or operator. 
# 
#  
#  For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down 
# to the nearest integer, 2 is returned.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 8515 👎 4548


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Binary Search
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    ### 2. Iterative Incremental Search
    # def mySqrt(self, x: int) -> int:
    #     if x == 0 or x == 1:  # Handle small edge cases
    #         return x
    #
    #     ans = 0
    #     for i in range(0, x + 1):  # Include x in the range
    #         if i * i > x:
    #             ans = i - 1
    #             break
    #         elif i * i == x:
    #             ans = i
    #             break
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
