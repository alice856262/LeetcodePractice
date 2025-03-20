# The Hamming distance between two integers is the number of positions at which 
# the corresponding bits are different. 
# 
#  Given two integers x and y, return the Hamming distance between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are 
# different.
#  
# 
#  Example 2: 
# 
#  
# Input: x = 3, y = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= x, y <= 2³¹ - 1 
#  
# 
#  
#  Note: This question is the same as 2220: Minimum Bit Flips to Convert Number.
#  
# 
#  Related Topics Bit Manipulation 👍 3910 👎 223


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1

        return count
# leetcode submit region end(Prohibit modification and deletion)
