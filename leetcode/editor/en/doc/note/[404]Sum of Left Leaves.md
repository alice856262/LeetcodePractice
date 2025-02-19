## Algorithm Description
### Key Idea
- Calculate the sum of all left leaves in a binary tree. A left leaf is defined as a leaf node that is the left child of its parent.
- Two methods were implemented:
  - Recursive Method: Traverse the tree recursively using depth-first search (DFS) while passing a flag (```isLeft```) to indicate whether the current node is a left child. If a node is a leaf and its flag is ```True```, add its value to the sum.
  - Iterative Method: Use an iterative DFS with a stack. Each element in the stack contains a node and a boolean flag indicating if it is a left child. Process each node, adding its value to the sum if it is a left leaf.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize a variable ```left_total``` to accumulate the sum of left leaves.
- Step 2: Define a helper function ```getLeftLeaves(node, isLeft)``` that:
  - Checks if the current ```node``` is ```None```.
  - If the node is a leaf (no left and no right child), checks if ```isLeft``` is ```True```. If so, add ```node.val``` to ```left_total``` and return.
  - Otherwise, recursively call itself for the left child with ```isLeft = True``` and for the right child with ```isLeft = False```.
- Step 3: Start the recursion by calling ```getLeftLeaves(root, False)``` on the root node (since the root is not considered a left child).
- Step 4: Return ```left_total``` as the result.
#### Method 2: Iterative Method
- Step 1: Check if the root is ```None```; if it is, return ```0```.
- Step 2: Initialize a variable ```total``` to 0 and create a stack containing a tuple of the root node and a flag ```False``` (since the root is not a left child).
- Step 3: While the stack is not empty:
  - Pop a tuple ```(node, isLeft)``` from the stack.
  - If the node is a leaf (no left or right child) and ```isLeft``` is ```True```, add ```node.val``` to ```total```.
  - Otherwise, push the right child (if it exists) with ```isLeft = False``` onto the stack.
  - Push the left child (if it exists) with ```isLeft = True``` onto the stack.
- Step 4: Return ```total``` as the final sum.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Every node in the tree is visited once.
  - Space Complexity: O(h)
    - The recursion stack uses space proportional to the height ```h``` of the tree.
    - Worst case (skewed tree): O(n)
    - Balanced tree: O(log n)
- Iterative Method
  - Time Complexity: O(n)
    - Each node is processed exactly once.
  - Space Complexity: O(h)
    - The stack's size is proportional to the height of the tree.
    - Worst case: O(n)
    - Balanced tree: O(log n)

## Notes on Solving Process
- Recursive Method:
  - Easy to implement and understand using recursion, but may lead to a stack overflow if the tree is very deep (skewed tree).
- Iterative Method:
  - Avoid potential recursion depth issues by using an explicit stack and provide similar time complexity while offering more control over the traversal.