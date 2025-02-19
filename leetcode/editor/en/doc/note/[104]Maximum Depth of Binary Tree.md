## Algorithm Description
### Key Idea
- Determine the maximum depth of a binary tree, which is the number of nodes along the longest path from the root node to any leaf node.
- Two methods were implemented:
  - Recursive Method: Use a straightforward recursive approach where the depth of a node is calculated based on the depths of its left and right subtrees.
  - Iterative Method: Store each node along with its depth in the stack, and keep updating the maximum depth as nodes are processed.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Return a depth of 0 if the current node is ```None```.
- Step 2: Recursively calculate the depth of the left and right subtrees.
- Step 3: Return the maximum of the two subtree depths plus 1 (to include the current node).
#### Method 2: Iterative Method
- Step 1: Return a depth of 0 if the tree is empty.
- Step 2: Initialize a stack with the root node and a depth of 1.
- Step 3: Use a loop to process nodes in the stack:
  - Pop a node and its associated depth.
  - Update the maximum depth encountered so far.
  - Push the left and right children of the node onto the stack with their depths incremented by 1.
- Step 4: When the stack is empty, return the maximum depth recorded.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. This accounts for the recursive call stack.
- Iterative Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is processed once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. This accounts for the maximum size of the stack during traversal.

## Notes on Solving Process
- Recursive Method:
  - Simple to implement but can lead to stack overflow for very deep trees.
- Iterative Method:
  - Avoid stack overflow issues and provide a clear simulation of the recursive process.