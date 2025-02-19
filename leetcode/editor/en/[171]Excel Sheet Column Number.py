# Given a string columnTitle that represents the column title as appears in an 
# Excel sheet, return its corresponding column number. 
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
# Input: columnTitle = "A"
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: columnTitle = "AB"
# Output: 28
#  
# 
#  Example 3: 
# 
#  
# Input: columnTitle = "ZY"
# Output: 701
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= columnTitle.length <= 7 
#  columnTitle consists only of uppercase English letters. 
#  columnTitle is in the range ["A", "FXSHRXW"]. 
#  
# 
#  Related Topics Math String 👍 4860 👎 381


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        reverse = columnTitle[::-1]
        result = 0
        for i in range(len(reverse)):
            result += (ord(reverse[i]) - ord('A')) * (26 ** i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
