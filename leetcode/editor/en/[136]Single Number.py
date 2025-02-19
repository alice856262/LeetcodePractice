# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one. 
# 
#  You must implement a solution with a linear runtime complexity and use only 
# constant extra space. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [2,2,1] 
#  
# 
#  Output: 1 
# 
#  Example 2: 
# 
#  
#  Input: nums = [4,1,2,1,2] 
#  
# 
#  Output: 4 
# 
#  Example 3: 
# 
#  
#  Input: nums = [1] 
#  
# 
#  Output: 1 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  Each element in the array appears twice except for one element which appears 
# only once. 
#  
# 
#  Related Topics Array Bit Manipulation 👍 17071 👎 774


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Dictionary Approach
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key, value in counts.items():
            if value == 1:
                return key

    ### 2. Bit Manipulation (XOR) Approach
    # def singleNumber(self, nums: List[int]) -> int:
    #     result = 0
    #     for num in nums:
    #         result ^= num
    #     return result
# leetcode submit region end(Prohibit modification and deletion)
