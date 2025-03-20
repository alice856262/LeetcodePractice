# Given the root of a binary search tree (BST) with duplicates, return all the 
# mode(s) (i.e., the most frequently occurred element) in it. 
# 
#  If the tree has more than one mode, return them in any order. 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than or equal 
# to the node's key. 
#  The right subtree of a node contains only nodes with keys greater than or 
# equal to the node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# Follow up: Could you do that without using any extra space? (Assume that the 
# implicit stack space incurred due to recursion does not count).
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 3974
#  👎 799


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None  # Tracks the previous node's value during in-order traversal
        self.curr_count = 0  # Current frequency count for the ongoing value
        self.max_count = 0  # Maximum frequency encountered so far
        self.res = []  # List to store the mode(s)

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Process current node:
            # If this is the first node or a different value than the previous, reset count to 1
            # Otherwise, increment the count
            if self.prev is None or node.val != self.prev:
                self.curr_count = 1
            else:
                self.curr_count += 1

            # Update mode(s) based on the current count
            if self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.res = [node.val]  # Start a new result list with the current value
            elif self.curr_count == self.max_count:
                # Append the current value only if it's not already the last added (avoids duplicates)
                if not self.res or self.res[-1] != node.val:
                    self.res.append(node.val)

            # Update previous value and traverse right subtree
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
