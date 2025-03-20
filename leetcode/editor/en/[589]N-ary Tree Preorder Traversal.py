# Given the root of an n-ary tree, return the preorder traversal of its nodes' 
# values. 
# 
#  Nary-Tree input serialization is represented in their level order traversal. 
# Each group of children is separated by the null value (See examples) 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
# null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  0 <= Node.val <= 10⁴ 
#  The height of the n-ary tree is less than or equal to 1000. 
#  
# 
#  
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
# 
#  Related Topics Stack Tree Depth-First Search 👍 3202 👎 203


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
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return
            result.append(node.val)  # Process the current node
            for child in node.children:  # Recursively traverse each child
                traverse(child)

        traverse(root)
        return result

    ### 2. Iterative Method
    # def preorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #
    #     result = []
    #     stack = [root]  # Initialize the stack with the root node
    #
    #     while stack:
    #         node = stack.pop()  # Pop the top node
    #         result.append(node.val)  # Process the current node
    #         # Push children to stack in reverse order so that the leftmost child is processed first
    #         for child in reversed(node.children):
    #             stack.append(child)
    #
    #     return result
# leetcode submit region end(Prohibit modification and deletion)
