## Algorithm Description
### Key Idea
- The task is to convert a sorted array into a **height-balanced binary search tree (BST)**, ensuring minimal height and balanced subtrees (for example: https://i.imgur.com/p7i22Kx.gif).
- Use a divide-and-conquer approach to recursively split the array and assign the middle element as the root, ensuring balance.

### Step-by-Step Algorithm
- Step 1: Base Case:
  - If the range of indices (```left > right```) is invalid, return ```None```.
  - Handle leaf nodes and terminate recursion for empty subarrays.
- Step 2: Compute the middle index as ```(left + right + 1) // 2``` to bias towards the right for even-sized arrays. This ensures the resulting tree is balanced.
- Step 3: Create a new ```TreeNode``` instance using the middle element.
- Step 4: Recursive Subtree Construction:
  - Recursively construct the left subtree using the range ```[left, mid - 1]```.
  - Recursively construct the right subtree using the range ```[mid + 1, right]```.
- Step 5: Attach left and right subtrees to the current node and return it.
- Step 6: Call the recursive helper function with the full array range ```[0, len(nums) - 1]```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - Each element is processed exactly once to construct the tree.
- Space Complexity: O(logn)
  - The recursive depth corresponds to the height of the tree, which is O(logn) for a balanced BST.

## Notes on Solving Process
- A height-balanced BST ensures that the height difference between the left and right subtrees of any node does not exceed 1.
- Choosing the middle element optimally splits the array, ensuring minimal tree height.
- By biasing the middle index towards the right for even-sized subarrays, the solution adheres to specific requirements for expected output.