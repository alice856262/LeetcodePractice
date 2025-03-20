## Algorithm Description
### Key Idea
- Reshape an ```m * n``` matrix into a new matrix of size ```r * c``` while preserving the row-traversing order of the original matrix. If the total number of elements does not equal ```r * c```, return the original matrix.
- Two methods were implemented:
  - List Comprehension and Slicing Approach: Use **list comprehensions** to flatten the matrix and then rebuild the reshaped matrix by slicing the flattened list.
  - Nested Loops with Index Approach: Manually flatten the matrix using nested loops into a temporary list, and then construct the reshaped matrix by iterating with an index pointer through the flattened list.

### Step-by-Step Algorithm
#### Method 1: List Comprehension and Slicing Approach
- Step 1: Compute the dimensions ```m``` and ```n``` of the original matrix.
- Step 2: Check if the total number of elements ```m * n``` equals ```r * c```. If not, return the original matrix.
- Step 3: Flatten the matrix into a single list ```flat``` using a list comprehension that iterates over each row and then each element.
- Step 4: Build the reshaped matrix by slicing the ```flat``` list into chunks of length ```c``` using a list comprehension that runs for ```r``` iterations.
- Step 5: Return the newly constructed matrix.
#### Method 2: Nested Loops with Index Approach
- Step 1: Initialize an empty list ```temp``` to store the flattened matrix.
- Step 2: Use nested loops to iterate through each row and each element, appending every element to ```temp```.
- Step 3: Check if the length of ```temp``` equals ```r * c```. If not, return the original matrix.
- Step 4: Initialize an empty list ```ans``` and a variable ```index = 0``` to track the current position in ```temp```.
- Step 5: Use nested loops: the outer loop runs for ```r``` iterations to construct each row, and the inner loop runs for ```c``` iterations to populate each row with elements from ```temp``` using the index.
- Step 6: Increment ```index``` accordingly and append each constructed row to ```ans```.

## Algorithmic Complexity
- List Comprehension and Slicing Approach
  - Time Complexity: O(m * n)
    - Flattening the matrix using a list comprehension and slicing it into sub-lists both process each element exactly once.
  - Space Complexity: O(m * n)
    - Extra space is required for the flattened list and the output matrix, both proportional to the total number of elements.
- Nested Loops with Index Approach
  - Time Complexity: O(m * n)
    - The nested loops for flattening the matrix and then reconstructing the new matrix both run in linear time relative to the number of elements.
  - Space Complexity: O(m * n)
    - A temporary list to store the flattened matrix and the final reshaped matrix are used, both requiring space proportional to the total number of elements.

## Notes on Solving Process
- List Comprehension and Slicing Approach:
  - The slicing operation directly builds the reshaped matrix without explicitly managing indices in a loop.
  - This method leverages Python's list comprehensions and built-in functions, making it succinct and potentially faster in practice.
- Nested Loops with Index Approach:
  - Implements the flattening and reshaping processes explicitly using nested loops.
  - The manual management of an index pointer offers clear insight into the reshaping process.