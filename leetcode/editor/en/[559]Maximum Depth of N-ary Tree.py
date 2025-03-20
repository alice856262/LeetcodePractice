# Given a n-ary tree, find its maximum depth. 
# 
#  The maximum depth is the number of nodes along the longest path from the 
# root node down to the farthest leaf node. 
# 
#  Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples). 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
# null,12,null,13,null,null,14]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The total number of nodes is in the range [0, 10⁴]. 
#  The depth of the n-ary tree is less than or equal to 1000. 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search 👍 2812 👎 91


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    ### 1. Recursive Method
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))

        return max_child_depth + 1

    ### 2. Iterative Method
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #
    #     max_depth = 0
    #     # Stack stores tuples of (node, current_depth)
    #     stack = [(root, 1)]
    #
    #     while stack:
    #         node, depth = stack.pop()
    #         max_depth = max(max_depth, depth)
    #         # For each child, push the child with depth increased by 1
    #         for child in node.children:
    #             stack.append((child, depth + 1))
    #
    #     return max_depth
# leetcode submit region end(Prohibit modification and deletion)
