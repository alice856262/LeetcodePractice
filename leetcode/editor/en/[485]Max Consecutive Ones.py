# Given a binary array nums, return the maximum number of consecutive 1's in 
# the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#  The maximum number of consecutive 1s is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] is either 0 or 1. 
#  
# 
#  Related Topics Array 👍 6103 👎 466


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        # After the loop, update max_count in case the array ends with 1's
        return max(max_count, count)
# leetcode submit region end(Prohibit modification and deletion)
