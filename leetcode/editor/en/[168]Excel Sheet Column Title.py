# Given an integer columnNumber, return its corresponding column title as it 
# appears in an Excel sheet. 
# 
#  For example: 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
#  
# 
#  
#  Example 1: 
# 
#  
# Input: columnNumber = 1
# Output: "A"
#  
# 
#  Example 2: 
# 
#  
# Input: columnNumber = 28
# Output: "AB"
#  
# 
#  Example 3: 
# 
#  
# Input: columnNumber = 701
# Output: "ZY"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= columnNumber <= 2³¹ - 1 
#  
# 
#  Related Topics Math String 👍 5719 👎 852


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result  # Prepend the character directly
            columnNumber //= 26
        return result
# leetcode submit region end(Prohibit modification and deletion)
