# Given an integer num, return a string of its base 7 representation. 
# 
#  
#  Example 1: 
#  Input: num = 100
# Output: "202"
#  
#  Example 2: 
#  Input: num = -7
# Output: "-10"
#  
#  
#  Constraints: 
# 
#  
#  -10⁷ <= num <= 10⁷ 
#  
# 
#  Related Topics Math 👍 837 👎 235


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        abs_num = abs(num)

        if num == 0:
            return '0'

        while abs_num > 0:
            remainder = abs_num % 7
            abs_num = abs_num // 7
            ans = str(remainder) + ans

        return ans if num > 0 else '-' + ans
# leetcode submit region end(Prohibit modification and deletion)
