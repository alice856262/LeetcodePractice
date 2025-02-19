# Given a positive integer n, write a function that returns the number of set 
# bits in its binary representation (also known as the Hamming weight). 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 11 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  The input binary string 1011 has a total of three set bits. 
# 
#  Example 2: 
# 
#  
#  Input: n = 128 
#  
# 
#  Output: 1 
# 
#  Explanation: 
# 
#  The input binary string 10000000 has a total of one set bit. 
# 
#  Example 3: 
# 
#  
#  Input: n = 2147483645 
#  
# 
#  Output: 30 
# 
#  Explanation: 
# 
#  The input binary string 1111111111111111111111111111101 has a total of 
# thirty set bits. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  
# Follow up: If this function is called many times, how would you optimize it?
# 
#  Related Topics Divide and Conquer Bit Manipulation 👍 6706 👎 1345


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Bitwise Manipulation
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1  # Check if the least significant bit is set
            n >>= 1  # Right-shift to process the next bit
        return count

    ### 2. String Conversion
    # def hammingWeight(self, n: int) -> int:
    #     bits = ''
    #     while n > 0:
    #         remainder = str(n % 2)
    #         n = n // 2
    #         bits += remainder
    #
    #     count = 0
    #     for i in bits:
    #         if i == '1':
    #             count += 1
    #
    #     return count
# leetcode submit region end(Prohibit modification and deletion)
