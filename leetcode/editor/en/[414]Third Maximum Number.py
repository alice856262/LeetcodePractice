# Given an integer array nums, return the third distinct maximum number in this 
# array. If the third maximum does not exist, return the maximum number. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned 
# instead.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they 
# have the same value).
# The third distinct maximum is 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow up: Can you find an 
# O(n) solution?
# 
#  Related Topics Array Sorting 👍 3183 👎 3301


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Single-Pass with Three Variables
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for num in nums:
            # Skip if the number is already one of the maximums
            if num == first or num == second or num == third:
                continue

            # Update first, second, and third accordingly
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        # If the third maximum doesn't exist, return the maximum
        return third if third is not None else first

    ### 2. Sorting and Unique Extraction
    # def thirdMax(self, nums: List[int]) -> int:
    #     unique_num = []
    #     nums.sort(reverse=True)
    #
    #     i = 0
    #     while len(unique_num) < 3 and i < len(nums):
    #         if nums[i] not in unique_num:
    #             unique_num.append(nums[i])
    #         i += 1
    #
    #     return unique_num[2] if len(unique_num) >= 3 else unique_num[0]
# leetcode submit region end(Prohibit modification and deletion)
