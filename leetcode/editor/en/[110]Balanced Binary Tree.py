# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 11072 👎 740


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            # Base case: the height of an empty tree is 0
            if not node:
                return 0

            # Recursively compute the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # If any subtree is unbalanced, propagate the unbalanced signal (-1)
            else:
                return max(left_height, right_height) + 1  # Return height of the current subtree
        return height(root) != -1
# leetcode submit region end(Prohibit modification and deletion)
