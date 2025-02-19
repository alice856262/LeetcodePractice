## Algorithm Description
### Key Idea
- Determine if a given integer ```num``` is a perfect square without using built-in functions.
- Two methods were implemented:
  - Binary Search Approach: Use a binary search approach to efficiently narrow down the potential square root by repeatedly halving the search interval.
  - Iterative Approach: Use an iterative approach by incrementing a candidate ```root``` from 1 upward until ```root²``` meets or exceeds ```num```.

### Step-by-Step Algorithm
#### Method 1: Binary Search Approach
- Step 1: Initialize two pointers: ```left = 1``` and ```right = num```.
- Step 2: While ```left``` is less than or equal to ```right```:
  - Calculate ```mid = (left + right) // 2``` and ```square = mid * mid```.
  - Compare ```square``` and ```num```:
    - If ```square``` is less than ```num```, set ```left = mid + 1``` (the candidate must be larger).
    - If ```square``` is greater than ```num```, set ```right = mid - 1``` (the candidate must be smaller).
    - If ```square``` equals ```num```, return ```True``` (a perfect square is found).
- Step 3: If the loop ends without finding an exact square, return ```False```.
#### Method 2: Iterative Approach
- Step 1: Initialize ```root = 1```.
- Step 2: While ```root**2``` is less than ```num```, increment ```root``` by 1.
- Step 3: After the loop, if ```root**2``` equals ```num```, return ```True```. Otherwise, return ```False```.
  
## Algorithmic Complexity
- Binary Search Approach
  - Time Complexity: O(log(num))
    - Each iteration halves the search space, leading to a logarithmic number of iterations.
  - Space Complexity: O(1)
    - Only a few constant-space variables are used.
- Iterative Approach
  - Time Complexity: O(√num)
    - Worst case: the loop runs until ```root``` reaches approximately ```√num```.
  - Space Complexity: O(1)
    - Use a constant amount of extra space.

## Notes on Solving Process
- Binary Search Approach:
  - By narrowing down the candidate range using binary search, it is efficient for large numbers due to its logarithmic time complexity.
- Iterative Approach:
  - As ```num``` increases, it's time complexity ```√num``` grows much faster than ```log₂(num)```.