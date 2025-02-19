## Algorithm Description
### Key Idea
- Pascal's Triangle is built row by row, and each row depends only on the previous row.
- By iterating backward while updating the current row, we avoid using additional memory for previous rows.

### Step-by-Step Algorithm
- Step 1: Initialize the first row, which is a list containing a single element ```[1]```.
- Step 2: Iterate to Target Row:
  - Use a loop to generate rows up to the given ```rowIndex```.
  - Add a placeholder ```1``` at the end of the current row to account for the new row's last element.
- Step 3: Update Inner Values:
  - Use another loop to update the inner values of the row.
  - Start from **the "second-to-last" element** and move backward to ensure no overwriting occurs.
  - Compute each element as the sum of the two elements directly above it in the previous row.

## Algorithmic Complexity
- Time Complexity: O(n^2)
  - ```n``` is ```numRows```, as for each of the ```rowIndex``` rows, we perform updates proportional to its size.
- Space Complexity: O(n)
  - Only the current row os stored in memory.

### Notes on Solving Process
- The key optimization is updating the row in **reverse order** to avoid using extra memory for storing previous rows.
- This approach ensures the algorithm maintains linear space complexity while constructing only the required row.