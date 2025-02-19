## Algorithm Description
### Key Idea
- Find the first occurrence of a string (```needle```) within another string (```haystack```) or return -1 if ```needle``` is not present.
- Two methods were implemented:
  - Manual Sliding Window Comparison: Iterating through all possible starting indices of ```haystack``` where ```needle``` could fit and checking for a substring match.
  - Built-in Function: Using Python's ```str.find()``` method, which directly returns the first occurrence.

### Step-by-Step Algorithm
#### Method 1: Manual Sliding Window Comparison
- Step 1: Determine the lengths of ```haystack``` (```n```) and ```needle``` (```m```).
- Step 2: Handle edge cases where ```needle``` is empty (return 0).
- Step 3: Iterate over **all valid starting indices** in ```haystack``` (i from 0 to n - m).
  - For each ```i```, extract the substring of length ```m``` starting from ```i``` and compare it to ```needle```.
  - If a match is found, return ```i```.
- Step 4: If no match is found after all iterations, return -1.
#### Method 2: Built-in Function
- Step 1: Use ```str.find()``` method on ```haystack``` with ```needle``` as the argument.

## Algorithmic Complexity
- Manual Sliding Window Comparison
  - Time Complexity: O((n−m+1)⋅m)
    - Worst case: every starting index in ```haystack``` is checked, and each substring comparison takes O(m).
  - Space Complexity: O(1)
    - No additional data structures are used beyond variables.
- Built-in Function
  - Time Complexity: O(n+m)
    - ```str.find()``` is optimized for string searching, potentially using algorithms like Knuth-Morris-Pratt (KMP).
  - Space Complexity: O(1)
    - The built-in method does not use additional space for operations.

## Notes on Solving Process
- Edge Cases: 
  - Both methods handle edge cases like an empty needle and needle not being found.
- Comparison:
  - While the manual method demonstrates understanding of substring search, the built-in method is recommended for production use due to its simplicity and efficiency.