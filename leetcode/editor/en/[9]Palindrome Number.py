# Given an integer x, return true if x is a palindrome, and false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string?
# 
#  Related Topics Math 👍 13322 👎 2782


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            # Build the reversed half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if the number is a palindrome
        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
# leetcode submit region end(Prohibit modification and deletion)
