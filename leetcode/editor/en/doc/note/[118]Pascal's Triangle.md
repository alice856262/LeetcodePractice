## Algorithm Description
### Key Idea
- Pascal's Triangle is constructed row by row, where each row is based on the values of the previous row.
- The first and last elements of every row are always ```1```.
- The inner elements of a row are the sum of the two elements directly above it in the previous row.

### Step-by-Step Algorithm
- Step 1: Initialize an empty list ```triangle``` to store all rows of Pascal's Triangle.
- Step 2: Iterate Over Rows:
  - Iterate through row indices from ```0``` to ```numRows - 1```, and initialize each row as a list of ```1```s with length ```i + 1```.
- Step 3: Compute Inner Values:
  - For each row, use another loop to compute the values of the inner elements.
  - Update each inner element as the sum of two elements from the previous row.
- Step 4: Append the fully constructed row to the ```triangle``` list.

## Algorithmic Complexity
- Time Complexity: O(n^2)
  - ```n``` is ```numRows```, as we compute up to ```i``` elements for each of the ```n``` rows.
- Space Complexity: O(n^2)
  - All ```n``` rows are stored in memory.

### Notes on Solving Process
- The key is recognizing that each element (except the edges) is derived from two specific elements in the previous row.
- Using a loop to iterate through each row and updating its elements based on the previous row makes the solution intuitive and efficient.
- Handling edge cases (like the first row or a single row) is managed by initializing all rows with ```1```s.