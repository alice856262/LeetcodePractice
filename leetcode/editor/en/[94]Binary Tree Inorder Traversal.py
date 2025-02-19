# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
# 
#  
#  Input: root = [1,null,2,3] 
#  
# 
#  Output: [1,3,2] 
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
#  Output: [4,2,6,5,7,1,3,9,8] 
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
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 13797 👎 818


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def recursive(node):
            if not node:
                return
            recursive(node.left)
            result.append(node.val)
            recursive(node.right)
        recursive(root)
        return result

    ### 2. Iterative Method
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     stack = []
    #     current = root
    #     while current or stack:
    #         while current:
    #             stack.append(current)  # Step 1: Push current node to stack
    #             current = current.left  # Move to the left child
    #
    #         current = stack.pop()  # Step 2: Process the top of the stack
    #         result.append(current.val)  # Add node value to result
    #         current = current.right  # Move to the right child
    #
    #     return result
# leetcode submit region end(Prohibit modification and deletion)
