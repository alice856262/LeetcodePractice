# Given a 32-bit integer num, return a string representing its hexadecimal 
# representation. For negative integers, two’s complement method is used. 
# 
#  All the letters in the answer string should be lowercase characters, and 
# there should not be any leading zeros in the answer except for the zero itself. 
# 
#  Note: You are not allowed to use any built-in library method to directly 
# solve this problem. 
# 
#  
#  Example 1: 
#  Input: num = 26
# Output: "1a"
#  
#  Example 2: 
#  Input: num = -1
# Output: "ffffffff"
#  
#  
#  Constraints: 
# 
#  
#  -2³¹ <= num <= 2³¹ - 1 
#  
# 
#  Related Topics Math Bit Manipulation 👍 1349 👎 225


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Bitwise Approach
    def toHex(self, num: int) -> str:
        hex_digits = '0123456789abcdef'
        ans = ''

        if num == 0:
            return hex_digits[num]
        if num < 0:
            # For negative numbers, obtain the 32-bit two's complement representation
            num &= 0xFFFFFFFF

        # Process 4 bits at a time until all bits are processed
        while num:
            # Extract the last 4 bits (a hexadecimal digit) using bitwise AND with 0xf
            ans = hex_digits[num & 0xf] + ans
            # Right shift num by 4 bits to process the next hexadecimal digit
            num >>= 4
        return ans

    ### 2. Division and Modulo Approach
    # def toHex(self, num: int) -> str:
    #     hex_digits = '0123456789abcdef'
    #     ans = ''
    #
    #     if num == 0:
    #         return hex_digits[num]
    #     if num < 0:
    #         num &= 0xFFFFFFFF
    #
    #     while num > 0:
    #         remainder = num % 16
    #         num //= 16
    #         ans += hex_digits[remainder]
    #     return ans[::-1]
# leetcode submit region end(Prohibit modification and deletion)
