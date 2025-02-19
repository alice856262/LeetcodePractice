## Algorithm Description
### Key Idea
- Determine whether a binary tree is symmetric by comparing the left and right subtrees at each level to ensure their structures and node values are mirror images of each other.
- Two methods were implemented:
  - Recursive Method: The symmetry check is done via recursive calls comparing the corresponding nodes in the left and right subtrees.
  - Iterative Method: Use a stack to simulate the recursive process and compare nodes iteratively.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Return True if the root node is ```None``` (an empty tree is symmetric).
- Step 2: Define Recursive Function ```isMirror(left, right)```:
  - If both nodes (```left``` and ```right```) are ```None```, return True (mirror images).
  - If one of the nodes is ```None``` or their values do not match, return False.
  - Otherwise, recursively check: **"```left.left``` with ```right.right```"** and **"```left.right``` with ```right.left```"**.
- Step 3: Return True if all these checks pass for every pair of nodes.
#### Method 2: Iterative Method
- Step 1: Return True if the root node is ```None```.
- Step 2: Initialize a stack with a tuple containing the left and right children of the root node.
- Step 3: While the stack is not empty:
  - Pop a pair of nodes (```left```, ```right```) from the stack.
  - If both are ```None```, continue.
  - If one is ```None``` or their values do not match, return False.
  - Push the node pairs to the stack: **"```left.left``` with ```right.right```"** and **"```left.right``` with ```right.left```"**.
- Step 4: If all pairs pass the checks, return True.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once.
  - Space Complexity: O(h)
    - ```h``` is the height of the tree. This accounts for the recursive call stack.
- Iterative Method
  - Time Complexity: O(n)
    - ```n``` is the number of nodes in the tree. Each node is visited once.
  - Space Complexity: O(n)
    - Worst case: ```n``` is the number of nodes. This accounts for the stack used to store pairs of nodes.

## Notes on Solving Process
- Recursive Method:
  - Writing helper functions ```isMirror()``` enhances code readability and modularity.
  - Simpler to implement and understand but may cause a stack overflow for very deep trees.
- Iterative Method:
  - Avoid stack overflow issue but requires careful handling of the stack.