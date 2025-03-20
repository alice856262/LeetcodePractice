# Given the root of a Binary Search Tree (BST), return the minimum absolute 
# difference between the values of any two different nodes in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/ 
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search 
# Tree Binary Tree 👍 4534 👎 246


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev = None  # This variable holds the value of the previously visited node in the in-order traversal

        # Define a helper function to perform an in-order traversal of the BST
        # The in-order traversal ensures that the nodes are processed in ascending order
        def inorder(node: Optional[TreeNode]):
            nonlocal min_diff, prev
            if not node:
                return

            inorder(node.left)  # Recursively traverse the left subtree
            # If prev is set (i.e., this is not the very first node), calculate the difference between the current node's value and the previous node's value
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            inorder(node.right)  # Recursively traverse the right subtree

        inorder(root)
        return min_diff

    ### 2. Iterative Method
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     min_diff = float('inf')
    #     prev = None
    #     stack = []
    #     current = root
    #
    #     # Iterative inorder traversal using a stack
    #     while stack or current:
    #         # Reach the leftmost node of the current subtree
    #         while current:
    #             stack.append(current)
    #             current = current.left
    #         # Process the node at the top of the stack
    #         current = stack.pop()
    #         # If there is a previous node, update the minimum difference
    #         if prev is not None:
    #             min_diff = min(min_diff, current.val - prev)
    #         # Update prev to the current node's value
    #         prev = current.val
    #         # Move to the right subtree
    #         current = current.right
    #
    #     return min_diff
# leetcode submit region end(Prohibit modification and deletion)
