# Given the root of a binary tree, return the sum of every tree node's tilt. 
# 
#  The tilt of a tree node is the absolute difference between the sum of all 
# left subtree node values and all right subtree node values. If a node does not 
# have a left child, then the sum of the left subtree node values is treated as 0. 
# The rule is similar if the node does not have a right child. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3]
# Output: 1
# Explanation: 
# Tilt of node 2 : |0-0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; 
# right subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [4,2,9,3,5,null,7]
# Output: 15
# Explanation: 
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; 
# right subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just 
# right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, 
# and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
#  
# 
#  Example 3: 
#  
#  
# Input: root = [21,7,14,1,1,2,2,3,3]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 2294 👎 2216


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def findTilt(self, root: Optional[TreeNode]) -> int:
        difference = 0

        def getTotal(root):
            nonlocal difference
            if not root:
                return 0

            # Recursively calculate the sum of the left subtree
            left_total = getTotal(root.left)
            # Recursively calculate the sum of the right subtree
            right_total = getTotal(root.right)
            # Update the difference between left and right subtree sums
            difference += abs(left_total - right_total)

            # Return the sum of the subtree rooted at the current node
            return root.val + left_total + right_total

        getTotal(root)
        return difference

    ### 2. Iterative Method
    # def findTilt(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     difference = 0
    #     stack1 = [root]  # First stack for the traversal
    #     stack2 = []  # Second stack to hold nodes in postorder
    #     subtree_sum = {}  # Dictionary to store the sum of the subtree for each node
    #
    #     # Perform a postorder traversal using two stacks
    #     while stack1:
    #         # Pop from stack1, and push the popped node to stack2
    #         node = stack1.pop()
    #         stack2.append(node)
    #         # Push its children onto stack1
    #         if node.left:
    #             stack1.append(node.left)
    #         if node.right:
    #             stack1.append(node.right)
    #
    #     # Process nodes in postorder order (from stack2)
    #     while stack2:
    #         # For each node, compute the sum of its left and right subtrees (using previously computed values)
    #         node = stack2.pop()
    #         left_sum = subtree_sum[node.left] if node.left in subtree_sum else 0
    #         right_sum = subtree_sum[node.right] if node.right in subtree_sum else 0
    #         # Update the overall difference
    #         difference += abs(left_sum - right_sum)
    #         # Store the subtree sum for that node
    #         subtree_sum[node] = node.val + left_sum + right_sum
    #
    #     return difference
# leetcode submit region end(Prohibit modification and deletion)
