## Algorithm Description
### Key Idea
- To check if ```subRoot``` is a subtree of ```root```, verify whether any subtree of ```root``` is identical to ```subRoot```.
- Two methods were implemented:
  - Recursive Method: Traverse the ```root``` tree recursively and check subtree equality at each step.
  - Iterative Method: Use a stack for depth-first traversal and check subtree equality iteratively.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Define a helper function ```isIdentical(root, subRoot)``` to check if two trees are identical:
  - If both ```root``` and ```subRoot``` are ```None```, return ```True```.
  - If one is ```None``` or their values differ, return ```False```.
  - Recursively check equality of left and right subtrees.
- Step 2: For each node in ```root```:
  - Check if ```isIdentical(root, subRoot)``` is ```True```.
  - Recursively call the function on ```root.left``` and ```root.right```.
  - Return ```True``` if any of the recursive calls return ```True```. Otherwise, return ```False```.
#### Method 2: Iterative Method
- Step 1: Define the same ```isIdentical(root, subRoot)``` helper function.
- Step 2: Use a stack to perform depth-first traversal of ```root```:
  - Push the ```root``` node onto the stack.
  - While the stack is not empty:
    - Pop a node from the stack.
    - Check if ```isIdentical(node, subRoot)``` is ```True```. If yes, return ```True```.
    - Push the left and right children of the node onto the stack (if they exist).
- Step 3: Return ```False``` if no match is found after processing all nodes.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n * m)
    - ```n``` is the number of nodes in ```root```, and ```m``` is the number of nodes in ```subRoot```.
    - For each node in ```root```, the ```isIdentical``` function is called, which takes O(m).
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. The recursion stack depth is proportional to the height of the tree.
- Iterative Method
  - Time Complexity: O(n * m)
    - Similar to the recursive method, each node in ```root``` is processed, and ```isIdentical``` is called.
  - Space Complexity: O(h)
    - The stack can hold up to O(h) nodes.

## Notes on Solving Process
- Recursive Method:
  - Simpler and easier to implement.
  - Relies on the call stack for managing state, which may cause stack overflow for very deep trees.
- Iterative Method:
  - Avoids recursion depth issues by explicitly managing the stack.
  - Slightly more verbose but equally effective.