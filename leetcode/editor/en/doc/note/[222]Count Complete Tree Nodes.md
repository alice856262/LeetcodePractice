## Algorithm Description
### Key Idea
- This algorithm leverages the structure of a **complete binary tree** to count nodes efficiently in less than O(n) time complexity.
- By comparing the heights of the left and right subtrees, it determines whether the left or right subtree is a full binary tree and reduces the problem size accordingly.

### Step-by-Step Algorithm
- Step 1: Base Case
  - If the node is empty, return count as 0.
- Step 2: Calculate Subtree Height
  - Define the ```getHeight``` helper function to calculate the height of the **leftmost path** of the **left and right subtrees**.
- Step 3: Calculate total nodes from the full subtree, the recursively computed subtree, and the root node.
  - If the left and right subtree heights are equal:
    - The left subtree is a **full binary tree** with 2<sup>left_height</sup> - 1 nodes.
    - Add the root node and recursively calculate the nodes in the right subtree.
  - Otherwise:
    - The right subtree is a **full binary tree** with 2<sup>right_height</sup> - 1 nodes.
    - Add the root node and recursively calculate the nodes in the left subtree.

## Algorithmic Complexity
- Time Complexity: O(log<sup>2</sup> n)
  - Calculating the height takes O(log n) and recursive calls are made O(log n) times.
  - Total = O(log n) * O(log n) = O(log<sup>2</sup> n).
- Space Complexity: O(log n)
  - Space required for the recursive call stack.

## Notes on Solving Process
- The ```getHeight``` function only traverses the leftmost nodes, ensuring O(log n) height calculation.
- The algorithm efficiently reduces the problem size by identifying full binary subtrees at each step.
- This method works specifically for **complete binary trees**, leveraging their structural properties to achieve better-than-linear time complexity.