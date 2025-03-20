# A perfect number is a positive integer that is equal to the sum of its 
# positive divisors, excluding the number itself. A divisor of an integer x is an 
# integer that can divide x evenly. 
# 
#  Given an integer n, return true if n is a perfect number, otherwise return 
# false. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 7
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10⁸ 
#  
# 
#  Related Topics Math 👍 1143 👎 1258


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 is not a perfect number by definition
        if num <= 1:
            return False

        # Start with 1 as a divisor (1 is always a divisor for num > 1)
        total = 1
        i = 2

        # Iterate through potential divisors up to sqrt(num)
        while i * i <= num:
            if num % i == 0:
                total += i
                # Avoid adding the square root twice for perfect squares
                if i * i != num:
                    total += num // i
            i += 1

        return total == num

    ### Brute Force --> time limit exceed error for large inputs
    # def checkPerfectNumber(self, num: int) -> bool:
    #     total = 0
    #     for i in range(1, num // 2 + 1):
    #         if num % i == 0:
    #             total += i
    #
    #     return total == num
# leetcode submit region end(Prohibit modification and deletion)
