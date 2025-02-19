## Algorithm Description
### Key Idea
- Since the linked list is sorted, duplicate values will appear consecutively. This allows us to eliminate duplicates by comparing each node with its next node.
- Modify the list in place by updating the ```next``` pointer of nodes to skip duplicates, ensuring a space-efficient solution.

### Step-by-Step Algorithm
- Step 1: Check if the linked list is ```None``` (empty list).
- Step 2: Initialize a pointer, ```current```, starting at the head of the linked list.
- Step 3: While the ```current``` node and its ```next``` node are not ```None```, iterate through the list:
  - Compare the value of the ```current``` node with the value of its ```next``` node:
    - If they are equal (duplicate found), update the ```next``` pointer of ```current``` to skip the duplicate node (```current.next = current.next.next```).
    - If they are not equal, move the ```current``` pointer to the next node (```current = current.next```).
- Step 4: When the traversal reaches the end of the list (```current``` becomes ```None```), the modified list is returned.

## Algorithmic Complexity
- Time Complexity: O(n)
  - Each node in the linked list is visited exactly once, where n is the number of nodes in the list.
- Space Complexity: O(1)
  - No additional space is used apart from the pointer for traversal, as the list is modified in place.

## Notes on Solving Process
- Edge Cases:
  - Empty list: Handled upfront by returning immediately.
  - Single-node list: No duplicates possible; the traversal loop does not execute.
- In-Place Modification:
  - Updating the ```next``` pointer ensures that no additional memory is used for creating a new list.