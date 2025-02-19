# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively?
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 15
# 681 👎 399


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)

    ### 2. Iterative Method
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #
    #     stack = [(root.left, root.right)]  # Stack contains pairs of nodes to compare
    #     while stack:
    #         left, right = stack.pop()
    #         # If both are None, continue
    #         if not left and not right:
    #             continue
    #         # If one is None or values are not equal, tree is not symmetric
    #         if not left or not right or left.val != right.val:
    #             return False
    #         # Push children to stack in mirrored order
    #         stack.append((left.left, right.right))
    #         stack.append((left.right, right.left))
    #
    #     return True
# leetcode submit region end(Prohibit modification and deletion)
