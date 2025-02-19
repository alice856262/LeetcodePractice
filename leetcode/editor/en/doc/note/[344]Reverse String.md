## Algorithm Description
### Key Idea
- Two-Pointer Technique: ```left``` pointer starting at the beginning of the array and ```right``` pointer starting at the end.
- By swapping the elements pointed by ```left``` and ```right``` and then moving the pointers inward, the array is reversed without the need for additional data structures, fulfilling the in-place requirement with O(1) extra space.

### Step-by-Step Algorithm
- Step 1: Initialize two pointers:
  - ```left = 0``` (start of the array)
  - ```right = len(s) - 1``` (end of the array)
- Step 2: While ```left < right```, perform the following:
  - Swap the elements at indices ```left``` and ```right```.
  - Increment ```left``` by 1 to move towards the center.
  - Decrement ```right``` by 1 to move towards the center.
- Step 3: Continue the process until the ```left``` pointer is no longer less than the ```right``` pointer, at which point the entire array has been reversed in place.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the number of characters in the array. Each character is visited at most once.
- Space Complexity: O(1)
  - Only a constant amount of extra space is used for the pointers and temporary variables during swaps.

## Notes on Solving Process
- The two-pointer method efficiently reverses the array by reducing the problem size from both ends simultaneously, ensuring that the characters are swapped until the center is reached.
- Since the swapping occurs directly in the input array, the solution meets the requirement of modifying the array in-place with O(1) extra memory.