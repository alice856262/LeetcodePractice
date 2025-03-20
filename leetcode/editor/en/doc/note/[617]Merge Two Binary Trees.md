## Algorithm Description
### Key Idea
- The problem requires merging two binary trees by summing overlapping nodes and keeping non-null nodes when one tree has a missing node.
- Two methods were implemented: (both methods traverse and modify the trees in-place)
  - Recursive Method: Recursively traverse both trees, summing node values when both exist and attaching non-null nodes when one is missing.
  - Iterative Method: Use a stack to traverse both trees iteratively, merging values when both nodes exist and attaching non-null children when necessary.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Base Case:
  - If both nodes are ```None```, return ```None```.
  - If one of the nodes is ```None```, return the non-null node.
- Step 2: Sum the values of the current nodes (```root1.val += root2.val```).
- Step 3: Recursively call:
  - Merge the left subtrees (```root1.left = mergeTrees(root1.left, root2.left)```).
  - Merge the right subtrees (```root1.right = mergeTrees(root1.right, root2.right)```).
- Step 4: Return merged root ```root1```.
#### Method 2: Iterative Method
- Step 1: Base Case:
  - If both trees are ```None```, return ```None```.
  - If one tree is ```None```, return the non-null tree.
- Step 2: Initialize a stack and push the root nodes ```(root1, root2)``` onto the stack.
- Step 3: Iterate while the stack is not empty:
  - Pop a pair of nodes ```(node1, node2)```.
  - If ```node2``` is ```None```, **continue** (skip merging).
  - Merge the values (```node1.val += node2.val```).
  - Check and merge left children:
    - If both exist, push ```(node1.left, node2.left)``` onto the stack.
    - If ```node1.left``` is ```None```, assign ```node2.left``` to ```node1.left```.
  - Check and merge right children:
    - If both exist, push ```(node1.right, node2.right)``` onto the stack.
    - If ```node1.right``` is ```None```, assign ```node2.right``` to ```node1.right```.
- Step 4: Return merged root ```root1```.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(min(m, n))
    - ```m``` and ```n``` are the number of nodes in the two trees. Each node is visited once.
  - Space Complexity: O(min(m, n))
    - Worst case (unbalanced tree): the recursion depth is O(min(m, n)).
- Iterative Method
  - Time Complexity: O(min(m, n))
    - Each node is visited once.
  - Space Complexity: O(min(m, n))
    - Worst case (unbalanced tree): the stack stores O(min(m, n)) nodes.

## Notes on Solving Process
- Recursive Method:
  - The recursive approach is intuitive and follows a depth-first strategy, but the call stack depth can be large in an unbalanced tree.
- Iterative Method:
  - The iterative approach tracks traversal using a stack, and is efficient for large trees since it prevents excessive recursive calls.