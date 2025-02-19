# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 13
# 191 👎 248


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has depth 0
        if not root:
            return 0

        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum depth plus 1 for the current node
        return max(left_depth, right_depth) + 1

    ### 2. Iterative Method
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # Base case: an empty tree has depth 0
    #     if not root:
    #         return 0
    #
    #     stack = [(root, 1)]  # Initialize a stack with the root node and depth 1
    #     max_depth = 0
    #     while stack:
    #         node, depth = stack.pop()  # Pop a node and its depth
    #         if node:
    #             max_depth = max(max_depth, depth)  # Update the maximum depth
    #             # Push the children nodes onto the stack with incremented depth
    #             stack.append((node.left, depth + 1))
    #             stack.append((node.right, depth + 1))
    #
    #     return max_depth
# leetcode submit region end(Prohibit modification and deletion)
