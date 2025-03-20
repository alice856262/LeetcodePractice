## Algorithm Description
### Key Idea
- Leverage the BST property where an in-order traversal produces a sorted sequence, ensuring that duplicate values appear consecutively.
- Count the frequency of consecutive values during traversal, and update the mode(s) by comparing the current frequency with the maximum frequency seen so far.

### Step-by-Step Algorithm
- Step 1: Initialize tracking variables:
  - ```prev``` to keep track of the previous node's value.
  - ```curr_count``` to count the frequency of the current value.
  - ```max_count``` to record the maximum frequency encountered.
  - ```res``` to store the mode(s).
- Step 2: Define an **in-order traversal function** that:
  - Recursively traverses the **left subtree**.
  - Processes the current node:
    - If ```prev``` is ```None``` or the current value is different from ```prev```, reset ```curr_count``` to ```1```.
    - Otherwise, increment ```curr_count```.
  - Updates the mode(s):
    - If ```curr_count``` exceeds ```max_count```, update ```max_count``` and set ```res``` to a new list containing the current value.
    - If ```curr_count``` equals ```max_count```, append the current value to ```res``` (avoiding duplicates).
  - Sets ```prev``` to the current node's value.
  - Recursively traverses the **right subtree**.
- Step 3: Call the in-order traversal function starting from the root.
- Step 4: Return the list ```res``` containing the mode(s).

## Algorithmic Complexity
- Time Complexity: O(n)
  - Each node in the BST is visited exactly once during the in-order traversal.
- Space Complexity: O(1)
  - The extra space used by this solution is O(1), assuming that the **implicit recursion stack (which depends on the height of the tree) is not counted**.
  - All the additional variables (```prev```, ```curr_count```, ```max_count```, and ```res```) require constant space regardless of the input size.

## Notes on Solving Process
- The algorithm takes advantage of the BST's sorted order to simplify frequency counting of consecutive duplicate values.
- By updating the mode(s) on the fly during the traversal, the solution efficiently determines the most frequent elements in one pass.
- The approach avoids additional data structures for counting frequencies beyond the constant-space tracking variables.