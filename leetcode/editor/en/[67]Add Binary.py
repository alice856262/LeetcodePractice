# Given two binary strings a and b, return their sum as a binary string. 
# 
#  
#  Example 1: 
#  Input: a = "11", b = "1"
# Output: "100"
#  
#  Example 2: 
#  Input: a = "1010", b = "1011"
# Output: "10101"
#  
#  
#  Constraints: 
# 
#  
#  1 <= a.length, b.length <= 10⁴ 
#  a and b consist only of '0' or '1' characters. 
#  Each string does not contain leading zeros except for the zero itself. 
#  
# 
#  Related Topics Math String Bit Manipulation Simulation 👍 9658 👎 1009


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Iterative Addition
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1  # Pointers for both strings starting at the last character

        # Iterate until both strings are processed or carry exists
        while i >= 0 or j >= 0 or carry:
            # Get the current digits or 0 if the pointer is out of range
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            # Calculate the sum of digits and carry
            total = digit_a + digit_b + carry
            # Append the least significant bit of the sum to the result
            result.append(str(total % 2))
            # Update the carry
            carry = total // 2
            # Move the pointers to the left
            i -= 1
            j -= 1

        # Reverse the result to get the correct order and join it as a string
        return ''.join(reversed(result))

    ### 2. Built-in Function
    # def addBinary(self, a: str, b: str) -> str:
    #     s = bin(int(a, 2) + int(b, 2))
    #     return s[2::]
# leetcode submit region end(Prohibit modification and deletion)
