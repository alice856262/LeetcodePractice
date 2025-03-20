## Algorithm Description
### Key Idea
- Return a list of node values obtained by performing a preorder traversal on an n-ary tree.
- Two methods were implemented:
  - Recursive Method: Use recursion to traverse the tree in preorder. Process the current node, then recursively traverse each of its children.
  - Iterative Method: Use an explicit stack to simulate the recursive preorder traversal. Process the current node, then **push its children in reverse order onto the stack** so that they are processed in the original left-to-right order.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize an empty list ```result``` to store the node values.
- Step 2: Define a helper function ```traverse(node)```:
  - If ```node``` is ```None```, return.
  - Append ```node.val``` to ```result```.
  - For each child in ```node.children```, call ```traverse(child)```.
- Step 3: Call ```traverse(root)``` to begin the preorder traversal from the root.
- Step 4: Return the list ```result```.
#### Method 2: Iterative Method
- Step 1: If the ```root``` is ```None```, return an empty list.
- Step 2: Initialize an empty list ```result``` to store the node values.
- Step 3: Initialize a stack with the ```root``` node.
- Step 4: While the stack is not empty:
  - Pop the top node from the stack, and append its value to ```result```.
  - Push the node's children onto the stack in reverse order (so that the leftmost child is processed first).
- Step 5: Return the list ```result```.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Every node is visited exactly once during the recursion.
  - Space Complexity: O(h)
    - The recursion stack uses space proportional to the height of the tree ```h```.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.
- Iterative Method
  - Time Complexity: O(n)
    - Every node is processed exactly once in the while loop.
  - Space Complexity: O(h)
    - The explicit stack holds at most ```h``` nodes at a time, similar to the recursion stack in the recursive method.

## Notes on Solving Process
- Recursive Method:
  - The helper function processes the current node before recursively visiting its children, ensuring a preorder sequence.
  - While simple and elegant, recursion can lead to deep call stacks in very tall trees.
- Iterative Method:
  - This method avoids recursion by using an explicit stack, which is advantageous in environments where recursion depth is a concern.
  - By pushing children onto the stack **in reverse order**, the original left-to-right order is preserved in the traversal.