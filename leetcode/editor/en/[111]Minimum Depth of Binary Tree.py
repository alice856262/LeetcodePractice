# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁵]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 74
# 27 👎 1320


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has depth 0
        if not root:
            return 0

        # Recursively calculate the depth of left and right subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            return min(left_depth, right_depth) + 1

    ### 2. Iterative Method
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     # Base case: an empty tree has depth 0
    #     if not root:
    #         return 0
    #
    #     stack = [(root, 1)]  # Initialize stack with the root node and depth 1
    #     min_depth = 100000  # Track the minimum depth
    #     while stack:
    #         node, depth = stack.pop()  # Pop a node and its depth
    #         if node:
    #             # Check if the node is a leaf node
    #             if not node.left and not node.right:
    #                 min_depth = min(min_depth, depth)
    #             # Push the left and right children of the node with updated depth
    #             if node.left:
    #                 stack.append((node.left, depth + 1))
    #             if node.right:
    #                 stack.append((node.right, depth + 1))
    #
    #     return min_depth
# leetcode submit region end(Prohibit modification and deletion)
