# Given the root of a binary tree, return all root-to-leaf paths in any order. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: ["1"]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics String Backtracking Tree Depth-First Search Binary Tree 👍 677
# 3 👎 315


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 1. Recursive Method
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, paths):
            if not node:
                return

            # Append current node's value to the path
            path += str(node.val)
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Continue to the left and right children
                path += "->"  # Add the arrow for the next node
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)

        paths = []
        dfs(root, "", paths)
        return paths

    ### 2. Iterative Method
    # def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    #     if not root:
    #         return []
    #
    #     stack = [(root, str(root.val))]  # Stack stores (node, path)
    #     paths = []
    #
    #     while stack:
    #         node, path = stack.pop()
    #         # If it's a leaf node, add the path to the result
    #         if not node.left and not node.right:
    #             paths.append(path)
    #         # Push right and left children to the stack if they exist
    #         if node.right:
    #             stack.append((node.right, path + "->" + str(node.right.val)))
    #         if node.left:
    #             stack.append((node.left, path + "->" + str(node.left.val)))
    #
    #     return paths
# leetcode submit region end(Prohibit modification and deletion)
