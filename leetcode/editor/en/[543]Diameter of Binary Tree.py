# Given the root of a binary tree, return the length of the diameter of the 
# tree. 
# 
#  The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree. This path may or may not pass through the root. 
# 
#  The length of a path between two nodes is represented by the number of edges 
# between them. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 14365 👎 1111


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter
            if not node:
                return 0

            # Calculate the depth of left and right subtrees
            left = depth(node.left)
            right = depth(node.right)

            # Update the diameter
            diameter = max(diameter, left + right)

            # Return the height of the current subtree
            return max(left, right) + 1

        depth(root)
        return diameter

    ### 2. Iterative Method
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     stack = [(root, False)]
    #     height = {}
    #     diameter = 0
    #
    #     while stack:
    #         node, visited = stack.pop()
    #
    #         if node is None:
    #             continue
    #
    #         if not visited:
    #             # Push the node back with the visited flag
    #             stack.append((node, True))
    #             # Push children onto the stack
    #             stack.append((node.left, False))
    #             stack.append((node.right, False))
    #         else:
    #             # Compute the height of the node after visiting children
    #             left = height.get(node.left, 0)
    #             right = height.get(node.right, 0)
    #             height[node] = max(left, right) + 1
    #
    #             # Update the diameter
    #             diameter = max(diameter, left + right)
    #
    #     return diameter
# leetcode submit region end(Prohibit modification and deletion)
