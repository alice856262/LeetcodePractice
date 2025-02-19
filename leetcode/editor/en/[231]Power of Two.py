# Given an integer n, return true if it is a power of two. Otherwise, return 
# false. 
# 
#  An integer n is a power of two, if there exists an integer x such that n == 2
# ˣ. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: true
# Explanation: 2⁰ = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 16
# Output: true
# Explanation: 2⁴ = 16
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= n <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without loops/recursion?
# 
#  Related Topics Math Bit Manipulation Recursion 👍 7083 👎 460


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Bitwise Manipulation
    def isPowerOfTwo(self, n: int) -> bool:
        # Edge case: n must be positive
        if n <= 0:
            return False
        # Use bitwise "AND" to check if n is a power of two
        return (n & (n - 1)) == 0

    ### 2. Iterative Division
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #
    #     remainder = 0
    #     while n > 0 and remainder == 0:
    #         remainder = n % 2
    #         n = n // 2
    #
    #     if n == 0:
    #         return True
    #     return False
# leetcode submit region end(Prohibit modification and deletion)
