# Given an integer array nums, handle multiple queries of the following type: 
# 
#  
#  Calculate the sum of the elements of nums between indices left and right 
# inclusive where left <= right. 
#  
# 
#  Implement the NumArray class: 
# 
#  
#  NumArray(int[] nums) Initializes the object with the integer array nums. 
#  int sumRange(int left, int right) Returns the sum of the elements of nums 
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + 
# nums[right]). 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
# 
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁵ <= nums[i] <= 10⁵ 
#  0 <= left <= right < nums.length 
#  At most 10⁴ calls will be made to sumRange. 
#  
# 
#  Related Topics Array Design Prefix Sum 👍 3395 👎 1945


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    ### 1. Prefix Sum Approach
    def __init__(self, nums: List[int]):
        # Precompute the prefix sum array
        self.prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix[i] = self.prefix[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # The sum from index left to right is the difference of two prefix sums
        return self.prefix[right + 1] - self.prefix[left]

    ### 2. Iterative Summation Approach
    # def __init__(self, nums: List[int]):
    #     self.numArray = nums
    #
    # def sumRange(self, left: int, right: int) -> int:
    #     total = 0
    #     for i in range(left, right + 1):
    #         total += self.numArray[i]
    #     return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
