# You are given a large integer represented as an integer array digits, where 
# each digits[i] is the iᵗʰ digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. The large integer does 
# not contain any leading 0's. 
# 
#  Increment the large integer by one and return the resulting array of digits. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  digits does not contain any leading 0's. 
#  
# 
#  Related Topics Array Math 👍 9812 👎 5447


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Iterative Approach with Carry Handling
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and iterate backward
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, increment it
                digits[i] += 1
                return digits
            else:
                # If the current digit is 9, set it to 0
                digits[i] = 0

        # If all digits were 9, prepend a 1 to the array
        return [1] + digits

    ### 2. Conversion to Integer and Back
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     digits_str = ''
    #     for i in digits:
    #         digits_str += str(i)
    #
    #     digits_num = int(digits_str)
    #     digits_num += 1
    #     digits_str = str(digits_num)
    #     ans = []
    #     for i in digits_str:
    #         ans.append(int(i))
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
