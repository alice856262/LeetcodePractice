# Given the root of a binary tree, invert the tree, and return its root. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#  
# 
#  Example 2: 
#  
#  
# Input: root = [2,1,3]
# Output: [2,3,1]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 14
# 332 👎 235


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root

    ### 2. Iterative Method
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         # Swap left and right children
    #         node.left, node.right = node.right, node.left
    #
    #         # Add children to the stack
    #         if node.left:
    #             stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)
    #
    #     return root
# leetcode submit region end(Prohibit modification and deletion)
