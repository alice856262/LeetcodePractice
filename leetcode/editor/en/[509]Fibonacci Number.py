# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is, 
# 
#  
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#  
# 
#  Given n, calculate F(n). 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 30 
#  
# 
#  Related Topics Math Dynamic Programming Recursion Memoization 👍 8549 👎 381


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Iterative Approach
    def fib(self, n: int) -> int:
        if n < 2:
            return n  # F(0) = 0, F(1) = 1

        a, b = 0, 1  # Initialize F(0) and F(1)
        for _ in range(2, n + 1):
            a, b = b, a + b  # Update to the next Fibonacci number
        return b

    ### 2. Naive Recursive Approach
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #
    #     return self.fib(n - 1) + self.fib(n - 2)
# leetcode submit region end(Prohibit modification and deletion)
