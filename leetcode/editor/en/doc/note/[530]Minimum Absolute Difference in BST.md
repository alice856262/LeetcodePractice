## Algorithm Description
### Key Idea
- The goal is to compute the minimum absolute difference between values of any two nodes in a BST.
- An in-order traversal of a BST produces a sorted sequence of node values. Thus, the minimum difference will be found between consecutive nodes in this sorted order.
- Two methods were implemented:
  - Recursive Method: Use a recursive in-order traversal to process nodes in order, keeping track of the previous node's value to update the minimum difference.
  - Iterative Method: Use an iterative in-order traversal with an explicit stack to achieve the same result without recursion.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize ```min_diff``` to infinity and ```prev``` to ```None```.
- Step 2: Define a helper function ```inorder(node)```:
  - Traverse the left subtree by calling ```inorder(node.left)```.
  - At the current node:
    - If ```prev``` is not ```None```, compute the difference ```node.val - prev``` and update ```min_diff``` if this difference is smaller.
    - Set ```prev``` to the current node's value.
  - Traverse the right subtree by calling ```inorder(node.right)```.
- Step 3: Call ```inorder(root)``` to process all nodes in the BST.
- Step 4: Return ```min_diff```.
#### Method 2: Iterative Method
- Step 1: Initialize ```min_diff``` to infinity, ```prev``` to ```None```, an empty stack, and set ```current``` to ```root```.
- Step 2: Use a loop that continues while ```stack``` is not empty or ```current``` is not ```None```:
  - While ```current``` is not ```None```, push ```current``` onto the stack and set ```current``` to ```current.left``` (traverse left).
  - Pop a node from the stack and process it:
    - If ```prev``` is not ```None```, update ```min_diff``` with ```min(min_diff, current.val - prev)```.
    - Set ```prev``` to the current node's value.
  - Set ```current``` to the right child of the popped node.
- Step 3: After the loop completes, return ```min_diff```.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Each node is visited exactly once in the in-order traversal.
  - Space Complexity: O(h)
    - The recursion stack space is proportional to the height of the tree, ```h```.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.
- Iterative Method
  - Time Complexity: O(n)
    - Each node is visited exactly once during the iterative traversal.
  - Space Complexity: O(h)
    - The stack uses space proportional to the height of the tree.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.

## Notes on Solving Process
- Recursive Method:
  - It leverages recursion to naturally perform an in-order traversal of the BST.
  - The BST property ensures that the nodes are processed in sorted order, so **only adjacent nodes need to be compared** to find the minimum difference.
- Iterative Method:
  - It uses an explicit stack to avoid recursion, which can be beneficial in environments where deep recursion might cause a stack overflow.
  - The iterative approach mirrors the recursive logic but manages the traversal state explicitly.