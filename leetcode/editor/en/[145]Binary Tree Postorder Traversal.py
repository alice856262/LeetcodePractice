# Given the root of a binary tree, return the postorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
# 
#  
#  Input: root = [1,null,2,3] 
#  
# 
#  Output: [3,2,1] 
# 
#  Explanation: 
# 
#  
# 
#  Example 2: 
# 
#  
#  Input: root = [1,2,3,4,5,null,8,null,null,6,7,9] 
#  
# 
#  Output: [4,6,7,5,2,9,8,3,1] 
# 
#  Explanation: 
# 
#  
# 
#  Example 3: 
# 
#  
#  Input: root = [] 
#  
# 
#  Output: [] 
# 
#  Example 4: 
# 
#  
#  Input: root = [1] 
#  
# 
#  Output: [1] 
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 7282 👎 208


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)  # Traverse the left subtree
            dfs(node.right)  # Traverse the right subtree
            result.append(node.val)  # Visit the root

        dfs(root)
        return result

    ### 2. Iterative Method
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #
    #     stack = [root]
    #     result = []
    #     while stack:
    #         node = stack.pop()
    #         result.append(node.val)  # Visit the root
    #         if node.left:
    #             stack.append(node.left)  # Push left child
    #         if node.right:
    #             stack.append(node.right)  # Push right child
    #
    #     return result[::-1]
# leetcode submit region end(Prohibit modification and deletion)
