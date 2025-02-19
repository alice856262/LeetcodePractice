## Algorithm Description
### Key Idea
- Use **Two Pointer Technique** to remove all occurrences of a specified value (```val```) from a given array (```nums```) in-place.
- The goal is to return the number of elements in the array that are not equal to val.
- The order of the remaining elements in the array should be maintained.

### Step-by-Step Algorithm
- Step 1: Initialize a pointer ```i``` at the start of the array (i = 0). This pointer will be used to place non-```val``` elements in their appropriate positions.
- Step 2: Iterate through the array with a pointer ```j``` that goes from the start to the end.
- Step 3: For each element at position ```j```:
  - If the element is not equal to val, place it at the ```i``` position and increment ```i```.
- Step 4: Continue this process until all elements have been checked.
- Step 5: The value of ```i``` after the loop indicates the number of non-```val``` elements.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the array. Both pointers traverse the array once.
- Space Complexity: O(1)
  - The space is used only for a few extra pointers.

## Notes on Solving Process
- In-Place Removal:
  - The solution modifies the array in place, without using extra space for another array. This is efficient in terms of both time and space.
- Pointer Movement:
  - The ```i``` pointer is incremented only when a non-```val``` element is found, allowing the function to place non-```val``` elements efficiently.
- Edge Cases:
  - This method handles edge cases such as an empty array (```nums = []```) or when ```val``` is not present in the array.