# Given an integer n, return true if it is a power of three. Otherwise, return 
# false. 
# 
#  An integer n is a power of three, if there exists an integer x such that n ==
#  3ˣ. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 27
# Output: true
# Explanation: 27 = 3³
#  
# 
#  Example 2: 
# 
#  
# Input: n = 0
# Output: false
# Explanation: There is no x where 3ˣ = 0.
#  
# 
#  Example 3: 
# 
#  
# Input: n = -1
# Output: false
# Explanation: There is no x where 3ˣ = (-1).
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
#  Related Topics Math Recursion 👍 3189 👎 284


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Iterative Division
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            remainder = n % 3
            n = n // 3
            if remainder != 0:
                return False

        if n == 1:
            return True
        return False

    ### 2. Mathematical Divisibility
    # def isPowerOfThree(self, n: int) -> bool:
    #     # 1162261467 is 3^19, the largest power of 3 within the 32-bit signed integer range.
    #     return n > 0 and 1162261467 % n == 0
# leetcode submit region end(Prohibit modification and deletion)
