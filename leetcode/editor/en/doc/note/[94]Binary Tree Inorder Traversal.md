## Algorithm Description
### Key Idea
- Inorder traversal visits the **left subtree**, the **root**, and then the **right subtree**. This pattern must be maintained while traversing the tree.
- Two methods were implemented:
  - Recursive Method: Use a recursive function to traverse the left subtree, process the current node, and then traverse the right subtree.
  - Iterative Method: Simulate the stack behavior of recursion explicitly. Use a stack to traverse the tree while processing nodes in the correct order.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize an empty list to store the traversal result.
- Step 2: Define a function called ```recursive(node)```:
  - If node is null, return.
  - Recursively call ```recursive(node.left)``` to traverse the left subtree.
  - Add the current node's value to the result list.
  - Recursively call ```recursive(node.right)``` to traverse the right subtree.
- Step 3: Invoke ```recursive(root)``` to start the traversal from the root node.
#### Method 2: Iterative Method
- Step 1: Initialize an empty list result to store the traversal result and an empty stack to simulate recursion.
- Step 2: Set a pointer ```current``` to the root node.
- Step 3: While ```current``` is not null or the ```stack``` is not empty:
  - Traverse to the leftmost node, pushing each node onto the stack.
  - When ```current``` becomes null, pop the top node from the stack.
  - Add the popped node's value to the result list.
  - Move ```current``` pointer to the right child of the popped node.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree (space used by the recursive call stack).
- Iterative Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is processed once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree (space used by the explicit stack).

## Notes on Solving Process
- Recursive Method:
  - More intuitive but relies on the call stack for managing traversal, which can lead to stack overflow for deep trees.
- Iterative Method:
  - Slightly more complex but avoids potential stack overflow by explicitly managing the stack.