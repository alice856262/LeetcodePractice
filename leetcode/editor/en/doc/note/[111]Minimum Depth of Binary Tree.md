## Algorithm Description
### Key Idea
- The minimum depth of a binary tree is the shortest path from the root node to any leaf node (a node with no children).
- Two methods were implemented:
  - Recursive Method: Use a divide-and-conquer approach, where the depth of each subtree is calculated recursively, and the minimum depth is determined based on the structure of the tree.
  - Iterative Method: Use a stack to perform a traversal, keep track of the depth of each node, and find the minimum depth without exploring the entire tree.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Base Case:
  - If the tree is empty (root is ```None```), return 0 as the minimum depth.
- Step 2: Recursive Depth Calculation:
  - Compute the depth of the left subtree (```left_depth```).
  - Compute the depth of the right subtree (```right_depth```).
- Step 3: Handle Missing Subtrees:
  - If one subtree is empty, return the depth of the non-empty subtree plus 1.
  - If both subtrees exist, return the smaller of the two depths plus 1.
#### Method 2: Iterative Method
- Step 1: Base Case:
  - If the tree is empty (root is ```None```), return 0 as the minimum depth.
- Step 2: Initialize a stack with the root node and its depth (set to 1).
- Step 3: Traversal Loop:
  - Pop a node and its depth from the stack.
  - If the node is a leaf (no left or right children), update the minimum depth if the current depth is smaller.
  - Push the left and right children of the node (if they exist) into the stack, incrementing their depth.
- Step 4: After exploring all possible paths, return the smallest depth recorded.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. This is due to the recursive call stack.
- Iterative Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is processed once.
  - Space Complexity: O(n)
    - Worst case: the tree is completely unbalanced, and all nodes are stored in the stack.

## Notes on Solving Process
- Recursive Method:
  - Simpler to implement and understand but relies on the call stack, which can lead to stack overflow for very deep trees.
- Iterative Method:
  - More robust for larger trees and avoids potential stack overflow. A breadth-first search (BFS) variant using a queue could also be implemented for faster discovery.