## Algorithm Description
### Key Idea
- To find the intersection of two singly linked lists, the goal is to determine if there is a common node (by reference, not value) between the two lists.
- Two methods were implemented:
  - Two Pointers: Use two pointers that traverse both lists and synchronize their traversal lengths.
  - Hash Set: Use a hash set to store nodes from one list and check if any node in the other list exists in the set.

### Step-by-Step Algorithm
#### Method 1: Two Pointers
- Step 1: Initialize two pointers ```pA``` and ```pB``` at the heads of ```listA``` and ```listB```, respectively.
- Step 2: Traverse both lists:
  - If ```pA``` reaches the end of ```listA```, move it to the head of ```listB```.
  - If ```pB``` reaches the end of ```listB```, move it to the head of ```listA```.
  - Continue traversing until ```pA``` and ```pB``` meet or both reach ```None```.
- Step 3: If ```pA``` and ```pB``` meet, the intersection node is found. Otherwise, return ```None``` (no intersection).
#### Method 2: Hash Set
- Step 1: Initialize an empty hash set ```visited```.
- Step 2: Traverse ```listA``` and add each node to the ```visited``` set.
- Step 3: Traverse ```listB```:
  - If a node exists in the ```visited``` set, it is the intersection node. Return it.
  - If no such node is found, return ```None``` (no intersection).

## Algorithmic Complexity
- Two Pointers
  - Time Complexity: O(m + n)
    - Traversing each list takes O(m + n), where ```m``` and ```n``` are the lengths of ```listA``` and ```listB```.
  - Space Complexity: O(1)
    - Uses constant space.
- Hash Set
  - Time Complexity: O(m + n)
    - Traversing ```listA``` and ```listB``` takes O(m + n). Checking membership in the hash set is O(1) on average.
  - Space Complexity: O(m)
    - The hash set requires O(m) space for storing nodes of ```listA```.

## Notes on Solving Process
- Two Pointers:
  - Aligns traversal lengths by switching heads, ensuring the two pointers traverse an equal number of nodes.
  - Most efficient in terms of space and avoids additional data structures.
- Hash Set:
  - Tracks visited nodes explicitly, which simplifies intersection detection but uses extra space.
- Both methods handle edge cases like disjoint lists, lists of unequal lengths, and lists with no intersection.