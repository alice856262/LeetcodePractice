## Algorithm Description
### Key Idea
- The binary search algorithm is used to find the target in a sorted array with O(log n) time complexity.
- The algorithm divides the search space in half at each step by comparing the target value with the middle element of the current search range.

### Step-by-Step Algorithm
- Step 1: Initialize two pointers:
  - ```left``` pointing to the start of the array.
  - ```right``` pointing to the end of the array.
- Step 2: Enter a loop that continues while ```left <= right```:
  - Compute the middle index ```mid```.
  - Compare `nums[mid]` with the `target`.
    - If ```nums[mid] == target```, return ```mid``` (target found).
    - If ```nums[mid] > target```, update ```right = mid - 1``` to search the left half.
    - If ```nums[mid] < target```, update ```left = mid + 1``` to search the right half.
- Step 3: If the loop exits without finding the target, return ```-1``` (target not found).

## Algorithmic Complexity
- Time Complexity: O(log n)
  - Each iteration reduces the search space by half, resulting in O(log n) iterations for an array of size ```n```.
- Space Complexity: O(1)
  - The algorithm uses constant extra space for pointers and variables.

## Notes on Solving Process
- The binary search is highly efficient for sorted arrays due to its logarithmic reduction in search space.
- Properly shrinking the search space by excluding the middle index (```mid - 1``` or ```mid + 1```) ensures correctness and avoids infinite loops.