# Given an array nums of size n, return the majority element. 
# 
#  The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array. 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,3]
# Output: 3
#  
#  Example 2: 
#  Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5 * 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  
# Follow-up: Could you solve the problem in linear time and in 
# O(1) space?
# 
#  Related Topics Array Hash Table Divide and Conquer Sorting Counting 👍 20230 
# 👎 695


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

    ### 2. Dictionary Approach
    # def majorityElement(self, nums: List[int]) -> int:
    #     counts = {}
    #     for num in nums:
    #         counts[num] = counts.get(num, 0) + 1
    #     for key, value in counts.items():
    #         if value > (len(nums)/2):
    #             return key

    ### 3. Sorting Approach
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return nums[len(nums) // 2]
# leetcode submit region end(Prohibit modification and deletion)
