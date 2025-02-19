# Given the roots of two binary trees root and subRoot, return true if there is 
# a subtree of root with the same structure and node values of subRoot and false 
# otherwise. 
# 
#  A subtree of a binary tree tree is a tree that consists of a node in tree 
# and all of this node's descendants. The tree tree could also be considered as a 
# subtree of itself. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the root tree is in the range [1, 2000]. 
#  The number of nodes in the subRoot tree is in the range [1, 1000]. 
#  -10⁴ <= root.val <= 10⁴ 
#  -10⁴ <= subRoot.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search String Matching Binary Tree Hash 
# Function 👍 8407 👎 542


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False

            return isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)

        if not root:
            return False
        return isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    ### 2. Iterative Method
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     def isIdentical(root, subRoot):
    #         if not root and not subRoot:
    #             return True
    #         if not root or not subRoot or root.val != subRoot.val:
    #             return False
    #         return isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)
    #
    #     if not root:
    #         return False
    #
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if isIdentical(node, subRoot):
    #             return True
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #
    #     return False
# leetcode submit region end(Prohibit modification and deletion)
