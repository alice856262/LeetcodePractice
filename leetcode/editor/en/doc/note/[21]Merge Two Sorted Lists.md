## Algorithm Description
### Key Idea
- Merge two sorted linked lists into a single sorted linked list while maintaining the order.
- Two methods were implemented:
  - Iterative Merge: Traverse both lists simultaneously and merge nodes based on their values.
  - Sorting-based Merge: Extract all values into a list, sort them, and reconstruct the linked list.

### Step-by-Step Algorithm
#### Method 1: Iterative Merge
- Step 1: Create a dummy node to simplify handling the head of the merged list.
- Step 2: Use a pointer (current) initialized at the dummy node to track the last node in the merged list.
- Step 3: Traverse both lists using two pointers:
  - Compare the current values of the two lists.
  - Attach the smaller value to the merged list and advance the pointer in that list.
- Step 4: Attach the remaining nodes from the non-empty list to the merged list, and return the merged list.
#### Method 2: Sorting-based Merge
- Step 1: Extract all node values from both linked lists into a single list.
- Step 2: Sort the extracted values.
- Step 3: Create a new dummy node and initialize a pointer to construct the merged list.
- Step 4: Traverse the sorted values and create new nodes for each value, appending them to the merged list, and return it.

## Algorithmic Complexity
- Iterative Merge
  - Time Complexity: O(n+m)
    - ```n``` and ```m``` are the lengths of the two lists. Each node is visited once.
  - Space Complexity: O(1)
    - No additional data structures are used beyond the pointers.
- Sorting-based Merge
  - Time Complexity: O((n+m)log(n+m))
    - Due to sorting the extracted values.
  - Space Complexity: O(n+m)
    - For storing all values in a list and creating new nodes.

## Notes on Solving Process
- Iterative Merge:
  - Efficient for merging directly while preserving memory usage.
  - Handles edge cases such as empty lists inherently.
  - Simpler implementation for maintaining linked list structure.
- Sorting-based Merge:
  - Provides an alternate approach by decoupling the sorting and merging steps.
  - Useful when working with more general data structures or when extracting values is a necessity.
  - Less efficient in terms of space and time compared to iterative merging.