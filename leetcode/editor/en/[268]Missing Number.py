# Given an array nums containing n distinct numbers in the range [0, n], return 
# the only number in the range that is missing from the array. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [3,0,1] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is 
# the missing number in the range since it does not appear in nums. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [0,1] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is 
# the missing number in the range since it does not appear in nums. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [9,6,4,2,3,5,7,0,1] 
#  
# 
#  Output: 8 
# 
#  Explanation: 
# 
#  n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is 
# the missing number in the range since it does not appear in nums. 
# 
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  
#  
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁴ 
#  0 <= nums[i] <= n 
#  All the numbers of nums are unique. 
#  
# 
#  
#  Follow up: Could you implement a solution using only O(1) extra space 
# complexity and O(n) runtime complexity? 
# 
#  Related Topics Array Hash Table Math Binary Search Bit Manipulation Sorting ?
# ? 12717 👎 3379


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Sum Formula
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
        actual_sum = sum(nums)  # Sum of elements in the array
        return expected_sum - actual_sum

    ### 2. XOR Method
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     result = 0
    #     # XOR all numbers from 0 to n
    #     for i in range(n + 1):
    #         result ^= i
    #     # XOR all numbers in the array
    #     for num in nums:
    #         result ^= num
    #     return result

    ### 3. Brute Force
    # def missingNumber(self, nums: List[int]) -> int:
    #     for i in range(len(nums) + 1):
    #         if i not in nums:
    #             return i
# leetcode submit region end(Prohibit modification and deletion)
