# Given two non-negative integers, num1 and num2 represented as string, return 
# the sum of num1 and num2 as a string. 
# 
#  You must solve the problem without using any built-in library for handling 
# large integers (such as BigInteger). You must also not convert the inputs to 
# integers directly. 
# 
#  
#  Example 1: 
# 
#  
# Input: num1 = "11", num2 = "123"
# Output: "134"
#  
# 
#  Example 2: 
# 
#  
# Input: num1 = "456", num2 = "77"
# Output: "533"
#  
# 
#  Example 3: 
# 
#  
# Input: num1 = "0", num2 = "0"
# Output: "0"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 10⁴ 
#  num1 and num2 consist of only digits. 
#  num1 and num2 don't have any leading zeros except for the zero itself. 
#  
# 
#  Related Topics Math String Simulation 👍 5176 👎 783


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1, i2 = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ''

        while i1 >= 0 or i2 >= 0 or carry != 0:
            # Get the current digits or 0 if the index is out of bounds
            digit1 = int(num1[i1]) if i1 >= 0 else 0
            digit2 = int(num2[i2]) if i2 >= 0 else 0

            # Sum the digits and the carry
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            ans = str(digit) + ans

            i1 -= 1
            i2 -= 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
