## Algorithm Description
### Key Idea
- Use **Two Pointer Technique** to remove duplicates from a sorted array in-place. 
- The relative order of the elements should be maintained, and the function should return the new length of the array without duplicates.

### Step-by-Step Algorithm
- Step 1: Initialize a pointer ```i``` at index 1 to track the position of the unique elements. The first element is always unique, so start from index 1.
- Step 2: Iterate through the array with a pointer ```j``` starting from index 1.
- Step 3: Compare the current element (```nums[j]```) with the previous unique element (```nums[i - 1]```):
  - If they are different, it indicates a unique element, so place it at the ```i``` index.
  - Move the ```i``` pointer one step forward.
- Step 4: Return the new length of the array.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the array. Both pointers traverse the array once.
- Space Complexity: O(1)
  - The space is used only for a few extra pointers.

## Notes on Solving Process
- In-Place Removal:
  - The solution removes duplicates in place, maintaining the order of unique elements. This approach is efficient both in terms of time and space.
- Pointer Movement:
  - The ```i``` pointer advances only when a unique element is found, reducing unnecessary computations.
- Handling Edge Cases:
  - This method handles edge cases such as an empty array by returning 0 without errors.