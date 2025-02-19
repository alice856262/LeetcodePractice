## Algorithm Description
### Key Idea
- A root-to-leaf path in a binary tree is a sequence of nodes starting at the root and ending at a leaf.
- Two methods were implemented:
  - Recursive Method: Use Depth-First Search (DFS) to traverse the tree. Append the current node to the path and recurse for its children, adding paths to the result list when reaching a leaf.
  - Iterative Method: Use a stack to simulate DFS, maintaining the current node and its path in each stack entry. Add the path to the result list when a leaf node is reached.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Define a helper function ```dfs(node, path, paths)```:
  - Append ```node.val``` to ```path```.
  - If ```node``` is a leaf, add ```path``` to ```paths```.
  - Otherwise, append ```"->"``` to the path and recursively call ```dfs``` for ```node.left``` and ```node.right```.
- Step 2: Call ```dfs``` with ```root```, an empty string, and ```paths```.
- Step 3: Return ```paths``` as the result.
#### Method 2: Iterative Method
- Step 1: Check if ```root``` is ```None```. If so, return an empty list.
- Step 2: Initialize a stack with the tuple ```(root, str(root.val))```.
- Step 3: While the stack is not empty:
  - Pop a tuple ```(node, path)``` from the stack.
  - If ```node``` is a leaf, add ```path``` to ```paths```.
  - Otherwise, push ```node.right``` and ```node.left``` to the stack (if they exist), appending ```"->"``` and the child's value to ```path```.
- Step 4: Return ```paths``` as the result.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: Ο(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once during the traversal.
  - Space Complexity: Ο(h)
    - ```h``` is the height of the tree. The recursion stack requires space proportional to the height of the tree.
- Iterative Method
  - Time Complexity: Ο(n)
    - Each node is visited once during the traversal.
  - Space Complexity: Ο(h)
    - Worst case: the stack requires space proportional to the height of the tree.

## Notes on Solving Process
- Recursive Method:
  - Simpler to implement and intuitive for traversing a binary tree.
  - May encounter stack overflow for very deep trees.
- Iterative Method:
  - Avoids recursion and uses an explicit stack for traversal.
  - Handles very deep trees without recursion stack issues.