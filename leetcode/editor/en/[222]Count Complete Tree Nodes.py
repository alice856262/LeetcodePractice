# Given the root of a complete binary tree, return the number of the nodes in 
# the tree. 
# 
#  According to Wikipedia, every level, except possibly the last, is completely 
# filled in a complete binary tree, and all nodes in the last level are as far 
# left as possible. It can have between 1 and 2ʰ nodes inclusive at the last level h.
#  
# 
#  Design an algorithm that runs in less than O(n) time complexity. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4,5,6]
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5 * 10⁴]. 
#  0 <= Node.val <= 5 * 10⁴ 
#  The tree is guaranteed to be complete. 
#  
# 
#  Related Topics Binary Search Bit Manipulation Tree Binary Tree 👍 8906 👎 552
# 


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getHeight(root):
            height = 0
            while root:
                height += 1
                root = root.left
            return height

        # Get the height of left and right subtrees
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        # If the heights are equal, the left subtree is a full binary tree (2^left_height - 1 nodes)
        if left_height == right_height:
            # Add root node and recursively calculate the nodes in the right subtree
            total = (2 ** left_height - 1) + 1 + self.countNodes(root.right)
        else:
            # Otherwise, the right subtree is a full binary tree (2^right_height - 1 nodes)
            # Add root node and recursively calculate the nodes in the left subtree
            total = (2 ** right_height - 1) + 1 + self.countNodes(root.left)
        return total

    ### Recursively count all nodes --> O(n) time complexity
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     # Count the nodes of the left and right subtrees recursively
    #     left_count = self.countNodes(root.left)
    #     right_count = self.countNodes(root.right)
    #
    #     # Total nodes = left subtree nodes + right subtree nodes + 1 (current node)
    #     return 1 + left_count + right_count
# leetcode submit region end(Prohibit modification and deletion)
