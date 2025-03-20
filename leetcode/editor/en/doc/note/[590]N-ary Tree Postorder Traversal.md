## Algorithm Description
### Key Idea
- Return a list of node values obtained by performing a postorder traversal on an n-ary tree.
- Two methods were implemented:
  - Recursive Method: Use recursion to traverse the tree. Process all children first, then process the current node.
  - Iterative Method: Use an explicit stack to perform a modified preorder traversal, then **reverse the result to obtain the postorder sequence**.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize an empty list ```result``` to store the traversal output.
- Step 2: Define a helper function ```traverse(node)```:
  - If ```node``` is ```None```, return immediately.
  - For each child in ```node.children```, recursively call ```traverse(child)```.
  - Append ```node.val``` to ```result``` after processing all its children.
- Step 3: Call ```traverse(root)``` to initiate the recursive traversal.
- Step 4: Return the list ```result``` which now contains the postorder traversal.
#### Method 2: Iterative Method
- Step 1: If ```root``` is ```None```, return an empty list.
- Step 2: Initialize an empty list ```result``` to store the node values.
- Step 3: Initialize a stack with the ```root``` node.
- Step 4: While the stack is not empty:
  - Pop a node from the stack, and append ```node.val``` to ```result```.
  - For each child in ```node.children```, push the child onto the stack.
- Step 5: Reverse the ```result``` list to obtain the correct postorder traversal and return the list.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Each node in the tree is visited exactly once.
  - Space Complexity: O(h)
    - The recursion stack uses space proportional to the height ```h``` of the tree.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.
- Iterative Method
  - Time Complexity: O(n)
    - Each node is processed once in the while loop, and the reversal of the result list takes O(n).
  - Space Complexity: O(n)
    - Worst case: the stack can hold up to ```n``` nodes.
    - The result list requires O(n) space.

## Notes on Solving Process
- Recursive Method:
  - Leverages recursion to naturally follow the postorder pattern (children first, then node).
  - May face limitations with deep trees due to recursion stack limits.
- Iterative Method:
  - Avoids recursion by using an explicit stack, which is beneficial in avoiding potential recursion depth issues.
  - Performs a modified preorder traversal (process node then children) and then reverses the result to achieve postorder.