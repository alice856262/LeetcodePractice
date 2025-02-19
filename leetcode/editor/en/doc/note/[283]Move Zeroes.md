## Algorithm Description
### Key Idea
- Use a two-pointer approach to efficiently move all zeros to the end of the array while maintaining the relative order of non-zero elements.
- The ```non_zero_pos``` pointer keeps track of the position where the next non-zero element should be placed.

### Step-by-Step Algorithm
- Step 1: Initialize a pointer ```non_zero_pos``` to 0. This pointer indicates the position where the next non-zero element should be placed.
- Step 2: Iterate through the array using a loop with index ```i```.
- Step 3: If the current element ```nums[i]``` is non-zero:
  - Swap ```nums[i]``` with ```nums[non_zero_pos]``` to move the non-zero element to the correct position.
  - Increment the ```non_zero_pos``` pointer by 1.
- Step 4: At the end of the loop, all non-zero elements will be at the front, and all zeros will be at the back of the array.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the array, as we iterate through the array once.
- Space Complexity: O(1)
  - The operation is done in-place without using extra space.

## Notes on Solving Process
- The algorithm efficiently separates non-zero and zero elements using a single loop and minimal swaps.
- The use of the ```non_zero_pos``` pointer ensures that each non-zero element is placed in the correct position immediately, avoiding unnecessary operations.
- This approach maintains the relative order of non-zero elements, which is crucial for correctness.