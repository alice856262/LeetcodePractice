## Algorithm Description
### Key Idea
- Traverse the array and count consecutive 1's, maintaining a running count.
- When a ```0``` is encountered, compare the current count with the maximum count recorded and reset the current count.

### Step-by-Step Algorithm
- Step 1: Initialize two variables: ```max_count``` (to store the maximum number of consecutive 1's) and ```count``` (to track the current streak of 1's), both set to ```0```.
- Step 2: Iterate over each element ```num``` in the array ```nums```.
- Step 3: If the current element ```num``` is ```1```, increment ```count``` by ```1```.
- Step 4: If the current element ```num``` is ```0```:
  - Update ```max_count``` to be the maximum of ```max_count``` and ```count```.
  - Reset ```count``` to ```0```.
- Step 5: After the loop, compare ```max_count``` with ```count``` one final time, since **the longest streak might occur at the end of the array**.

## Algorithmic Complexity
- Time Complexity: O(n)
  - The algorithm makes a single pass through the array.
- Space Complexity: O(1)
  - Only a constant amount of additional space is used.

## Notes on Solving Process
- By resetting the count on encountering a ```0``` and updating the maximum, it ensures that all possible consecutive sequences of 1's are considered.
- A final check after the loop handles the scenario where the array ends with the longest sequence of 1's.