## Algorithm Description
### Key Idea
- Find all integers in the range ```[1, n]``` that do not appear in the given array ```nums```, where ```n``` is the length of the array.
- Two methods were implemented:
  - In-place Marking Approach: For each number in the array, use in-place marking to mark its corresponding index (derived from the value) as visited by making the element negative. Then, the indices with positive values indicate missing numbers.
  - Sorting with Pointer Approach: Sort the array and iterate through it with a pointer, comparing each number in the range ```[1, n]``` to the sorted array. Skip duplicates and record the numbers that are missing.

### Step-by-Step Algorithm
#### Method 1: In-place Marking Approach
- Step 1: Initialize an empty list ```missing``` to store the missing numbers.
- Step 2: Iterate over each element ```n``` in ```nums```:
  - Compute the index ```i``` as ```abs(n) - 1```.
  - Mark the element at that index as visited by setting ```nums[i]``` to ```-abs(nums[i])```.
- Step 3: Loop over the array using the index ```i```:
  - If ```nums[i]``` is positive, it means that ```i + 1``` was never marked, so append ```i + 1``` to ```missing```.
- Step 4: Return the list ```missing```.
#### Method 2: Sorting with Pointer Approach
- Step 1: Sort the array ```nums``` in descending order.
- Step 2: Initialize an empty list ```missing``` and a pointer ```pointer = 0```.
- Step 3: Iterate over each number in the range from 1 to ```n```:
  - If the pointer is within bounds and ```nums[pointer]``` equals the current number, advance the pointer (skipping duplicates).
  - Otherwise, append the current number to ```missing```.
- Step 4: Return the list ```missing```.

## Algorithmic Complexity
- In-place Marking Approach
  - Time Complexity: O(n)
    - We traverse the array twice (once for marking and once for collecting missing numbers), so it takes O(2n) time.
  - Space Complexity: O(1)
    - The extra space used is constant, aside from the output list.
- Sorting with Pointer Approach
  - Time Complexity: O(n log n)
    - Sorting the array takes O(n log n) time, plus O(n) for the subsequent iteration.
  - Space Complexity: O(1)
    - Assuming in-place sorting, the extra space is constant (aside from the output list).

## Notes on Solving Process
- In-place Marking Approach:
  - Leverage the fact that numbers in ```nums``` are in the range ```[1, n]``` to use their values as indices.
  - Efficiently mark visited indices in-place by converting them to negative.
- Sorting with Pointer Approach:
  - Use sorting to arrange the numbers, making it easier to iterate and identify gaps.
  - Simpler to understand conceptually, but incur a higher time complexity due to sorting.