## Algorithm Description
### Key Idea
- Inverting a binary tree involves swapping the left and right subtrees of each node in the tree.
- Two methods were implemented:
  - Recursive Method: Utilize the call stack to traverse and invert subtrees recursively.
  - Iterative Method: Use an explicit stack to simulate depth-first traversal and invert the tree iteratively.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Base Case:
  - If the current node is ```None``` or both its children are ```None```, return the node.
- Step 2: Recursive Step:
  - Store the left subtree in a temporary variable ```temp```.
  - Assign the inverted right subtree to ```root.left```.
  - Assign the inverted left subtree (stored in ```temp```) to ```root.right```.
- Step 3: Return the current root after swapping its left and right subtrees.
#### Method 2: Iterative Method
- Step 1: Base Case:
  - If the root is ```None```, return ```None```.
- Step 2: Initialize a stack with the root node and traverse the tree in depth-first order:
  - While the stack is not empty:
    - Pop the top node from the stack.
    - Swap its left and right children.
    - Push the non-```None``` children onto the stack.
- Step 3: Return the root after processing all nodes.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes. Visiting each node once takes O(n).
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. The recursion stack requires space proportional to the height of the tree O(h).
- Iterative Method
  - Time Complexity: O(n)
    - Visiting each node once takes O(n).
  - Space Complexity: O(h)
    - The space complexity is proportional to the height of the tree, O(h), where ```h``` can range from O(log n) (balanced tree) to O(n) (skewed tree).

## Notes on Solving Process
- Recursive Method:
  - Simplifies the implementation by leveraging the call stack to manage the traversal and inversion process.
  - May result in stack overflow for very deep trees (e.g., skewed trees).
- Iterative Method:
  - Uses an explicit stack to avoid recursion, making it more suitable for trees with large depths.
  - Offers better control over stack usage and avoids issues with recursion depth limits.