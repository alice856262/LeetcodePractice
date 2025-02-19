# Given an integer n, return an array ans of length n + 1 such that for each i (
# 0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 10⁵ 
#  
# 
#  
#  Follow up: 
# 
#  
#  It is very easy to come up with a solution with a runtime of O(n log n). Can 
# you do it in linear time O(n) and possibly in a single pass? 
#  Can you do it without using any built-in function (i.e., like __builtin_
# popcount in C++)? 
#  
# 
#  Related Topics Dynamic Programming Bit Manipulation 👍 11374 👎 566


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Bit Manipulation
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # i >> 1 gives i divided by 2 (remove the least significant bit), and (i & 1) is 1 if the least significant bit of i is 1, else it's 0
            ans[i] = ans[i >> 1] + (i & 1)  # (i & 1) can be changed to (i % 2)

        return ans

    ### 2. Iterative Method
    # def countBits(self, n: int) -> List[int]:
    #     ans = [0] * (n + 1)
    #
    #     # Compute the number of 1's in the binary representation for each number
    #     for i in range(n + 1):
    #         count = 0
    #         temp = i
    #         while temp > 0:
    #             # Check if the last bit is 1 by computing the remainder when divided by 2
    #             count += temp % 2
    #             # Remove the last bit by performing integer division by 2
    #             temp //= 2
    #         ans[i] = count
    #
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
