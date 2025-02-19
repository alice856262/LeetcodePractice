## Algorithm Description
### Key Idea
- Reversing a singly linked list involves changing the direction of the ```next``` pointers for each node.
- Two methods were implemented:
  - Recursive Method: Use recursion to reverse the rest of the list and adjust pointers during the unwinding phase.
  - Iterative Method: Use two pointers (```prev``` and ```current```) to reverse the list in-place within a loop.

### Step-by-Step Algorithm
#### Method 1: Recursive Method
- Step 1: Base Case:
  - If the list is empty or has only one node (```head``` is ```None``` or ```head.next``` is ```None```), return ```head```.
- Step 2: Recursive Step:
  - Recursively reverse the rest of the list starting from ```head.next```.
  - Adjust the pointers:
    - Set ```head.next.next``` to ```head``` to reverse the link.
    - Set ```head.next``` to ```None``` to detach the original link.
- Step 3: Return the new head of the reversed list.
#### Method 2: Iterative Method
- Step 1: Initialize two pointers:
  - ```prev``` as ```None``` to represent the end of the reversed list.
  - ```current``` pointing to the ```head``` of the list.
- Step 2: Traverse the list:
  - Store the ```next``` node of ```current``` in a temporary variable ```next_node```.
  - Reverse the ```next``` pointer of ```current``` to point to ```prev```.
  - Move ```prev``` to ```current```.
  - Move ```current``` to ```next_node```.
- Step 3: At the end of the traversal, ```prev``` will point to the new head of the reversed list.

## Algorithmic Complexity
- Recursive Method
  - Time Complexity: O(n)
    - Traverses the list once takes O(n), where ```n``` is the number of nodes.
  - Space Complexity: O(n)
    - The recursion stack requires space proportional to the depth of recursion, which is O(n) in the worst case.
- Iterative Method
  - Time Complexity: O(n)
    - Traverses the list once takes O(n).
  - Space Complexity: O(1)
    - Uses constant extra space for pointers.

## Notes on Solving Process
- Recursive Method:
  - Intuitive and elegant but uses extra memory for the recursion stack.
  - Handles the reversal during the unwinding phase of recursion.
- Iterative Method:
  - Efficient in terms of both time and space, as it does not use extra memory for recursion.
  - Preferred for larger lists or when recursion depth is a concern.
- Both methods preserve the original structure of the list while reversing the links.