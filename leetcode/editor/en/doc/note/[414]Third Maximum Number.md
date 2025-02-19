## Algorithm Description
### Key Idea
- Find the third distinct maximum number in an integer array. If there are fewer than three distinct numbers, return the maximum number.
- Two methods were implemented:
  - Single-Pass with Three Variables: Use three variables (```first```, ```second```, ```third```) to maintain the top three distinct maximums in a single pass through the array, updating these variables as necessary and skipping duplicates.
  - Sorting and Unique Extraction: Sort the array in descending order, then iterate to collect unique numbers until three distinct numbers are found. Return the third unique number if available; otherwise, return the maximum.

### Step-by-Step Algorithm
#### Method 1: Single-Pass with Three Variables
- Step 1: Initialize three variables (```first```, ```second```, ```third```) to ```None```.
- Step 2: Iterate through each number in the array:
  - If the number is equal to any of ```first```, ```second```, or ```third```, skip it.
  - Otherwise, update the three variables:
    - If ```first``` is ```None``` or the number is greater than ```first```, shift ```first``` to ```second``` and ```second``` to ```third```, then set ```first``` to the current number.
    - Else if ```second``` is ```None``` or the number is greater than ```second```, shift ```second``` to ```third``` and set ```second``` to the current number.
    - Else if ```third``` is ```None``` or the number is greater than ```third```, set ```third``` to the current number.
- Step 3: After processing all numbers, if ```third``` is not ```None```, return ```third```; otherwise, return ```first```.
#### Method 2: Sorting and Unique Extraction
- Step 1: Sort the array in descending order.
- Step 2: Initialize an empty list ```unique_num``` to store unique numbers.
- Step 3: Iterate through the sorted array:
  - If the current number is not already in ```unique_num```, append it.
  - Stop when ```unique_num``` contains 3 distinct numbers or the array is exhausted.
- Step 4: If there are at least 3 unique numbers, return the third one; otherwise, return the first number (which is the maximum).

## Algorithmic Complexity
- Single-Pass with Three Variables
  - Time Complexity: O(n)
    - Each number in the array is processed exactly once.
  - Space Complexity: O(1)
    - Only three extra variables are used regardless of the array size.
- Sorting and Unique Extraction
  - Time Complexity: O(n log n)
    - Sorting the array takes O(n log n) time. Iterating through the sorted array takes O(n) (worst case).
  - Space Complexity: O(n)
    - The sorting operation may require O(n) extra space, and the list for unique numbers stores at most ```n``` elements (though typically much fewer).

## Notes on Solving Process
- Single-Pass with Three Variables:
  - Run in linear time with constant space and avoid the overhead of sorting.
  - More complex logic for updating the three variables.
- Sorting and Unique Extraction:
  - Sorting introduces an O(n log n) time complexity, which is less optimal for large datasets compared to a linear approach.
  - Use additional space for sorting and for storing the unique numbers.