# Given the root of a binary tree, return the sum of all left leaves. 
# 
#  A leaf is a node with no children. A left leaf is a leaf that is the left 
# child of another node. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 1
# 5 respectively.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 55
# 80 👎 313


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_total = 0

        def getLeftLeaves(root, isLeft):
            nonlocal left_total
            if not root:
                return
            if not root.left and not root.right:
                if isLeft:
                    left_total += root.val
                return

            getLeftLeaves(root.left, True)
            getLeftLeaves(root.right, False)

        getLeftLeaves(root, False)
        return left_total

    ### 2. Iterative Method
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     total = 0
    #     stack = [(root, False)]
    #
    #     while stack:
    #         node, isLeft = stack.pop()
    #
    #         # Check if the node is a leaf.
    #         if not node.left and not node.right:
    #             if isLeft:
    #                 total += node.val
    #         else:
    #             # Push the right child first so that the left child is processed first.
    #             if node.right:
    #                 stack.append((node.right, False))
    #             if node.left:
    #                 stack.append((node.left, True))
    #
    #     return total
# leetcode submit region end(Prohibit modification and deletion)
