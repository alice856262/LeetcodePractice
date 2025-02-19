## Algorithm Description
### Key Idea
- Preorder traversal visits nodes in the order: **Root -> Left Subtree -> Right Subtree**.
- Two methods were implemented:
  - Recursive Method: Use a helper function that recursively visits the root, left, and right nodes.
  - Iterative Method: Use a stack to simulate the recursive process and traverse the nodes in the required order.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize an empty list ```result``` to store the traversal.
- Step 2: Define a helper function ```dfs(node)```.
  - Appends ```node.val``` to ```result``` (visit the root).
  - Recursively calls ```dfs``` on ```node.left``` (left subtree).
  - Recursively calls ```dfs``` on ```node.right``` (right subtree).
- Step 3: Call the helper function ```dfs``` starting with the ```root```.
#### Method 2: Iterative Method
- Step 1: If ```root``` is ```None```, return an empty list.
- Step 2: Initialize a stack and add the ```root``` node to it.
- Step 3: Initialize an empty list ```result``` to store the traversal.
- Step 4: While the stack is not empty:
  - Pop the top node from the stack.
  - Append its value to ```result``` (visit the root).
  - If the node has a right child, push it onto the stack.
  - If the node has a left child, push it onto the stack.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes. Visiting each node once takes O(n).
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. The recursion stack requires space proportional to the height of the tree O(h).
    - Worst case (skewed tree): ```h = n```.
- Iterative Method
  - Time Complexity: O(n)
    - Visiting each node once takes O(n).
  - Space Complexity: O(h)
    - The space complexity is proportional to the height of the tree, O(h), where ```h``` can range from O(log n) (balanced tree) to O(n) (skewed tree).

## Notes on Solving Process
- Recursive Method:
  - Intuitive and easy to implement, but may lead to stack overflow for very deep trees (if recursion depth exceeds system limits).
- Iterative Method:
  - More suitable for environments with limited stack size.
  - Explicit stack management is required but avoids recursion overhead.
- Edge cases to consider:
  - An empty tree (```root``` is ```None```).
  - A tree with a single node.
  - Trees with unbalanced structures (e.g., completely skewed trees).