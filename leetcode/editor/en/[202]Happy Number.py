# Write an algorithm to determine if a number n is happy. 
# 
#  A happy number is a number defined by the following process: 
# 
#  
#  Starting with any positive integer, replace the number by the sum of the 
# squares of its digits. 
#  Repeat the process until the number equals 1 (where it will stay), or it 
# loops endlessly in a cycle which does not include 1. 
#  Those numbers for which this process ends in 1 are happy. 
#  
# 
#  Return true if n is a happy number, and false if not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 19
# Output: true
# Explanation:
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics Hash Table Math Two Pointers 👍 10819 👎 1538


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Keep track of numbers already seen to detect cycles
        input = str(n)

        while input != '1':
            if input in seen:  # If already seen this string before, there's a cycle
                return False
            seen.add(input)

            total = 0
            for i in input:
                total += int(i) ** 2
            input = str(total)

        return True
# leetcode submit region end(Prohibit modification and deletion)
