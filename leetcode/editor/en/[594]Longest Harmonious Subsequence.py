# We define a harmonious array as an array where the difference between its 
# maximum value and its minimum value is exactly 1. 
# 
#  Given an integer array nums, return the length of its longest harmonious 
# subsequence among all its possible subsequences. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,3,2,2,5,2,3,7] 
#  
# 
#  Output: 5 
# 
#  Explanation: 
# 
#  The longest harmonious subsequence is [3,2,2,2,3]. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,3,4] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of 
# which have a length of 2. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [1,1,1,1] 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  No harmonic subsequence exists. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Hash Table Sliding Window Sorting Counting 👍 2258 👎 29
# 4


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Build a dictionary to count the frequency of each number
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        max_length = 0
        # Iterate through the dictionary's keys (unsorted)
        for num in nums_dict:
            if num + 1 in nums_dict:
                # Update max_length with the sum of frequencies of the pair (num, num+1)
                max_length = max(max_length, nums_dict[num] + nums_dict[num + 1])

        return max_length
# leetcode submit region end(Prohibit modification and deletion)
