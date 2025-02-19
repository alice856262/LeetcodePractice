# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums. 
# 
#  
#  Example 1: 
#  Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#  
#  Example 2: 
#  Input: nums = [1,1]
# Output: [2]
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= n 
#  
# 
#  
#  Follow up: Could you do it without extra space and in O(n) runtime? You may 
# assume the returned list does not count as extra space. 
# 
#  Related Topics Array Hash Table 👍 9684 👎 510


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. In-place Marking Approach
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        for i, n in enumerate(nums):
            if n > 0:
                missing.append(i + 1)
        return missing

    ### 2. Sorting with Pointer Approach
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     n = len(nums)
    #     pointer = 0
    #     missing = []
    #
    #     for number in range(1, n + 1):
    #         if pointer < n and nums[pointer] == number:
    #             # Skip all occurrences of this number (handle duplicates)
    #             while pointer < n and nums[pointer] == number:
    #                 pointer += 1
    #         else:
    #             # If the number is not found, add it to the missing list
    #             missing.append(number)
    #
    #     return missing
# leetcode submit region end(Prohibit modification and deletion)
