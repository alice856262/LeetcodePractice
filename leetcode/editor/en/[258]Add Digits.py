# Given an integer num, repeatedly add all its digits until the result has only 
# one digit, and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= num <= 2³¹ - 1 
#  
# 
#  
#  Follow up: Could you do it without any loop/recursion in O(1) runtime? 
# 
#  Related Topics Math Simulation Number Theory 👍 5000 👎 1946


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Iterative Method
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        num_str = str(num)
        while len(num_str) > 1:
            ans = 0
            for i in num_str:
                ans += int(i)
                num_str = str(ans)
            if len(num_str) == 1:
                return ans

    ### 2. Mathematical Method
    # def addDigits(self, num: int) -> int:
    #     if num == 0:
    #         return 0
    #     return 1 + (num - 1) % 9
# leetcode submit region end(Prohibit modification and deletion)
