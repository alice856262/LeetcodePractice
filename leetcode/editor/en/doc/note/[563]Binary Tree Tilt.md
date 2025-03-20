## Algorithm Description
### Key Idea
- Compute the sum of every node's tilt in a binary tree. The tilt of a node is defined as the absolute difference between the sum of values in its left subtree and the sum of values in its right subtree.
- Two methods were implemented:
  - Recursive Method: Use a recursive, post-order traversal to compute the sum of each subtree and update a global variable with the tilt for each node.
  - Iterative Method: Use an iterative post-order traversal with two stacks to process the nodes in post-order, computing subtree sums on the fly using a dictionary, and updating the overall tilt as each node is processed.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Initialize a variable ```difference = 0``` to store the accumulated tilt.
- Step 2: Define a helper function ```getTotal(root)``` that returns the sum of the subtree rooted at ```root```.
- Step 3: For the current node, recursively compute:
  - The sum of the left subtree as ```left_total = getTotal(root.left)```.
  - The sum of the right subtree as ```right_total = getTotal(root.right)```.
- Step 4: Update ```difference``` by adding ```abs(left_total - right_total)```.
- Step 5: Return the sum of the subtree rooted at the current node as ```node.val + left_total + right_total```.
- Step 6: Call ```getTotal(root)``` and then return ```difference``` as the result.
#### Method 2: Iterative Method
- Step 1: Check if ```root``` is ```None```. If it is, return ```0```.
- Step 2: Initialize a variable ```difference = 0```, a dictionary ```subtree_sum``` to store the sum of the subtree for each node, and two stacks: ```stack1``` (initialized with the root) and an empty ```stack2```.
- Step 3: Perform a post-order traversal using two stacks:
  - While ```stack1``` is not empty, pop a node from ```stack1``` and push it onto ```stack2```.
  - Push the node's left and right children (if they exist) onto ```stack1```.
- Step 4: Process nodes from ```stack2``` (which are now in post-order):
  - For each node, retrieve ```left_sum``` from ```subtree_sum``` if the left child exists (or ```0``` otherwise) and similarly for ```right_sum```.
  - Update ```difference``` by adding ```abs(left_sum - right_sum)```.
  - Compute the total subtree sum for the node as ```node.val + left_sum + right_sum``` and store it in ```subtree_sum```.
- Step 5: After processing all nodes, return ```difference```.
  
## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Every node in the tree is visited exactly once during the post-order traversal.
  - Space Complexity: O(h)
    - The recursion stack uses space proportional to the height of the tree ```h```.
    - For a skewed tree, ```h = n```. For a balanced tree, ```h = O(log n)```.
- Iterative Method
  - Time Complexity: O(n)
    - Each node is processed exactly once during the iterative post-order traversal.
  - Space Complexity: O(n)
    - Worst case: Require O(n) space for two stacks and a dictionary to store subtree sums.

## Notes on Solving Process
- Recursive Method:
  - Leverages the natural recursive structure of trees, using post-order traversal to compute subtree sums before processing the current node.
  - Uses a nonlocal variable to accumulate the tilt, resulting in succinct and clear code.
- Iterative Method:
  - Avoids recursion by using two stacks to simulate post-order traversal, which can be beneficial in scenarios where recursion depth might be an issue.
  - Maintains a dictionary for subtree sums to enable efficient computation of each node's tilt.
  - Although it may use more space due to the explicit stacks and dictionary, it is robust for trees with large depths.