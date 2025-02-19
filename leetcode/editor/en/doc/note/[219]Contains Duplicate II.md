## Algorithm Description
### Key Idea
- Use a dictionary to efficiently store and track the last seen index of each unique number in the array.
- For each number, check if it has already been seen and whether the difference between its current index and the last seen index is ```≤ k```.
- This approach ensures that the algorithm efficiently detects nearby duplicates without performing unnecessary comparisons.

### Step-by-Step Algorithm
- Step 1: Initialize an empty dictionary ```index_dict``` to store the last seen index of each number.
- Step 2: Iterate through the array using both index ```i``` and value ```num```.
  - Return ```True``` if the number ```num``` is in ```index_dict```, and the difference between the current index ```i``` and the stored index ```index_dict[num]``` is ```≤ k```.
  - Update ```index_dict[num]``` with the current index ```i```.
- Step 3: If the loop completes without finding any nearby duplicates, return ```False```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the array, as each element is processed once and dictionary operations (lookup and update) are O(1) on average.
- Space Complexity: O(n)
  - The dictionary stores at most ```n``` entries, one for each unique number in the array.

## Notes on Solving Process
- The dictionary-based approach is optimal for large input sizes due to its linear time complexity.
- The use of a dictionary allows constant-time checks for previously seen numbers and quick updates for the current index.
- This method effectively handles edge cases, including:
  - Arrays with no duplicates.
  - Arrays where all duplicates are farther apart than ```k```.
  - Small ```k``` values where duplicates must be close to satisfy the condition.