## Algorithm Description
### Key Idea
- Postorder traversal visits nodes in the order: **Left Subtree -> Right Subtree -> Root**.
- Two methods were implemented:
  - Recursive Method: Use a helper function that recursively visits the left, right, and root nodes.
  - Iterative Method: Use a stack to simulate the recursion and reverse the result to get the correct postorder sequence.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize an empty list ```result``` to store the traversal.
- Step 2: Define a helper function ```dfs(node)```.
  - Recursively calls ```dfs``` on ```node.left``` (left subtree).
  - Recursively calls ```dfs``` on ```node.right``` (right subtree).
  - Appends ```node.val``` to ```result``` (visit the root). 
- Step 3: Call the helper function ```dfs``` starting with the ```root```.
#### Method 2: Iterative Method
- Step 1: If ```root``` is ```None```, return an empty list.
- Step 2: Initialize a stack and add the ```root``` node to it.
- Step 3: Initialize an empty list ```result``` to store the traversal.
- Step 4: While the stack is not empty:
  - Pop the top node from the stack.
  - Append its value to ```result``` (visit the root).
  - Push the left child onto the stack (if it exists).
  - Push the right child onto the stack (if it exists).
- Step 5: Since the values in ```result``` are in reverse postorder (Root -> Right -> Left), reverse the list to get the correct postorder sequence.

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
  - Avoids recursion stack limitations by explicitly managing a stack.
  - Requires reversing the result to produce the correct postorder sequence.
- Edge cases to consider:
  - An empty tree (```root``` is ```None```).
  - A tree with a single node.
  - Trees with unbalanced structures (e.g., completely skewed trees).