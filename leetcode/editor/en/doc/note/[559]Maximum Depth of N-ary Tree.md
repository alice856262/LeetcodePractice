## Algorithm Description
### Key Idea
- Compute the maximum depth of an n-ary tree, defined as the number of nodes along the longest path from the root node down to the farthest leaf.
- Two methods were implemented:
  - Recursive Method: Use a recursive depth-first search (DFS) approach to traverse the tree. At each node, recursively determine the maximum depth among its children and add ```1``` to account for the current node.
  - Iterative Method: Use an iterative DFS approach with an explicit stack. Each stack element stores a node along with its current depth. Update the maximum depth encountered as the nodes are processed.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Check if the current node (```root```) is ```None```. If so, return ```0``` because an empty tree has a depth of ```0```.
- Step 2: Initialize a variable ```max_child_depth = 0``` to keep track of the maximum depth among the children.
- Step 3: Iterate over each child in ```root.children``` and recursively compute its depth using ```self.maxDepth(child)```.
- Step 4: Update ```max_child_depth``` with the maximum value returned from the recursive calls.
- Step 5: Return ```max_child_depth + 1``` to account for the current node's level.
#### Method 2: Iterative Method
- Step 1: Check if the root is ```None```. If it is, return ```0```.
- Step 2: Initialize a variable ```max_depth = 0``` and a stack that holds tuples of the form ```(node, current_depth)```, starting with the root at depth ```1```.
- Step 3: While the stack is not empty, pop a tuple ```(node, depth)``` from the stack.
  - Update ```max_depth``` with the maximum of its current value and ```depth```.
  - For each child of the current node, push ```(child, depth + 1)``` onto the stack.
- Step 4: After processing all nodes, return ```max_depth```.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Every node in the tree is visited exactly once during the recursive traversal.
  - Space Complexity: O(h)
    - The recursion stack uses space proportional to the height ```h``` of the tree.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.
- Iterative Method
  - Time Complexity: O(n)
    - Each node is processed exactly once during the iterative traversal.
  - Space Complexity: O(h)
    - The stack's size is proportional to the height of the tree, similar to the recursion stack in the recursive method.

## Notes on Solving Process
- Recursive Method:
  - This method leverages recursion to break down the problem into smaller sub-problems (i.e., finding the maximum depth of each subtree).
  - It can lead to deep recursion which, in a worst-case scenario (skewed tree), might approach O(n) space on the recursion stack.
- Iterative Method:
  - The iterative method avoids recursion by using an explicit stack, which can be advantageous in environments where recursion depth is a concern.
  - It maintains the same time complexity as the recursive method but provides more control over memory usage, which may help avoid stack overflow in very deep trees.