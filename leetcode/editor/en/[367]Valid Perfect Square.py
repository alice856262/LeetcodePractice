# Given a positive integer num, return true if num is a perfect square or false 
# otherwise. 
# 
#  A perfect square is an integer that is the square of an integer. In other 
# words, it is the product of some integer with itself. 
# 
#  You must not use any built-in library function, such as sqrt. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an 
# integer.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 4386 👎 318


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Binary Search Approach
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False

    ### 2. Iterative Approach
    # def isPerfectSquare(self, num: int) -> bool:
    #     root = 1
    #     while num > root ** 2:
    #         root += 1
    #
    #     if num == root ** 2:
    #         return True
    #     else:
    #         return False
# leetcode submit region end(Prohibit modification and deletion)
