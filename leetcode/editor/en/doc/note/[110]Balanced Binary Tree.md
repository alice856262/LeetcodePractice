## Algorithm Description
### Key Idea
- Use a bottom-up approach to determine if the tree is height-balanced.
- Traverse the tree recursively, starting from the leaf nodes, and calculate the height of each subtree while checking the height difference for the balance condition.
- Propagate an unbalanced signal (```-1```) up the recursion stack if any subtree is unbalanced.

### Step-by-Step Algorithm
- Step 1: Base Case:
  - If the current node is ```None``` (an empty subtree), return a height of 0.
- Step 2: Recursive Height Calculation:
  - Compute the height of the left subtree (```left_height```) by recursively calling ```height(node)```.
  - Compute the height of the right subtree (```right_height```) by recursively calling ```height(node)```.
- Step 3: Unbalanced Situation:
  - If either ```left_height``` or ```right_height``` is ```-1```, it means one of the subtrees is unbalanced, so propagate the unbalanced signal (```-1```).
  - If the absolute difference between ```left_height``` and ```right_height``` exceeds 1, mark the current subtree as unbalanced by returning ```-1```.
- Step 4: Balanced Situation:
  - Return the height of the subtree as ```max(left_height, right_height) + 1```.
- Step 5: The root is balanced if the height of the entire tree is not ```-1```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - Each node is visited once to compute its height, which ensures that we do not re-compute subtree heights unnecessarily.
- Space Complexity: O(h)
  - The space complexity is proportional to the height of the tree (h), as the recursive calls stack up to the height of the tree.

## Notes on Solving Process
- The bottom-up approach avoids redundant calculations of subtree heights, improving efficiency compared to a top-down approach.
- Propagating the unbalanced signal (```-1```) ensures that we terminate early for unbalanced trees, reducing unnecessary computation.
- The algorithm remains linear in complexity, making it suitable for large trees with up to n = 5000 nodes.