## Algorithm Description
### Key Idea
- Avoid a nested loop and achieve a linear-time solution.
- Use a dictionary to store elements as we iterate through the array.
- For each element, calculate its complement (i.e., ```target - num```).
- Check if the complement exists in the dictionary:
  - If yes, the solution is found.
  - If no, store the current number and its index in the dictionary for future lookups.

### Step-by-Step Algorithm
- Step 1: Create an empty dictionary to store numbers as keys and their indices as values.
- Step 2: Iterate through the array
  - Calculate the complement of the current number.
  - Check if the complement exists in the dictionary. If it does, return the indices of the current number and its complement.
  - If the complement is not found, add the current number and its index to the dictionary.
- Step 3: Continue the process until the solution is found. Since the problem guarantees a single solution, the process will terminate once a match is identified.

## Algorithmic Complexity
- Time Complexity: O(n)
  - The algorithm makes a single pass through the array, with O(1) operations (dictionary insertions and lookups) for each element.
- Space Complexity: O(n)
  - The dictionary requires additional space to store up to ```n``` elements in the worst case.

## Notes on Solving Process
- Focus on Efficiency:
  - Avoid nested loops, as they result in O(n²) time complexity.
  - Use a hash map for constant-time lookups.
- Edge Case Handling:
  - Arrays with minimal length (e.g., 2 elements).
  - Large inputs within the constraint bounds.