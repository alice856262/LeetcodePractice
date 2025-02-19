# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
#  
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in a strictly increasing order. 
#  
# 
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 11220 👎 586


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to process
            if left > right:
                return None

            # Create a node with the middle element
            mid = (left + right + 1) // 2
            node = TreeNode(nums[mid])
            # Recursively build the left and right subtrees
            node.left = recursive(left, mid - 1)
            node.right = recursive(mid + 1, right)
            return node

        # Call the helper function with the entire range of the array
        return recursive(0, len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)
