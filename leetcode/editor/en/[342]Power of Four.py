# Given an integer n, return true if it is a power of four. Otherwise, return 
# false. 
# 
#  An integer n is a power of four, if there exists an integer x such that n == 
# 4ˣ. 
# 
#  
#  Example 1: 
#  Input: n = 16
# Output: true
#  
#  Example 2: 
#  Input: n = 5
# Output: false
#  
#  Example 3: 
#  Input: n = 1
# Output: true
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
#  Related Topics Math Bit Manipulation Recursion 👍 4006 👎 402


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Logarithm-based Check
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) % 1 == 0

    ### 2. Bit Manipulation
    # def isPowerOfFour(self, n: int) -> bool:
    #     return n > 0 and not(n & (n - 1)) and (n & 1431655765) == n
    #
    # ### 3. Iterative Division
    # def isPowerOfFour(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #
    #     while n > 1:
    #         remainder = n % 4
    #         n = n // 4
    #         if remainder != 0:
    #             return False
    #
    #     if n == 1:
    #         return True
    #     return False
# leetcode submit region end(Prohibit modification and deletion)
