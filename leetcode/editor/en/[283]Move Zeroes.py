# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
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
# Follow up: Could you minimize the total number of operations done?
# 
#  Related Topics Array Two Pointers 👍 17440 👎 501


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer for the position of the next non-zero element
        non_zero_pos = 0

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the element at non_zero_pos
                nums[i], nums[non_zero_pos] = nums[non_zero_pos], nums[i]
                # Move the non_zero_pos pointer forward
                non_zero_pos += 1
# leetcode submit region end(Prohibit modification and deletion)
