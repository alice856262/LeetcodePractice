## Algorithm Description
### Key Idea
- Compute the integer square root of a non-negative integer x, which is the largest integer r such that r² ≤ x.
- Two methods were implemented: 
  - Binary Search: Leverage the properties of sorted numbers to narrow down the range of possible square root values efficiently.
  - Iterative Incremental Search: Check each number from 0 up to the input value until the square exceeds the given number.

### Step-by-Step Algorithm
#### Method 1: Binary Search
- Step 1: Set ```left = 1``` and ```right = x``` (since the square root of x cannot be greater than x).
- Step 2: Perform Binary Search:
  - Compute the midpoint ```mid = (left + right) // 2```.
  - Compare ```mid²``` with ```x```:
    - If ```mid² == x```, return ```mid```.
    - If ```mid² < x```, move the left pointer up: ```left = mid + 1```.
    - If ```mid² > x```, move the right pointer down: ```right = mid - 1```.
- Step 3: When the loop exits, ```right``` will be the integer square root of x.
#### Method 2: Iterative Incremental Search
- Step 1: If ```x = 0``` or ```x = 1```, return x directly as the square root equals the input in these cases.
- Step 2: Iterate Over Possible Values (from 0 to x + 1):
  - For each ```i```, check the value of ```i²```:
    - If ```i² > x```, the square root is ```i − 1```, so break the loop and return ```i − 1```.
    - If ```i² == x```, the square root is ```i```, so break the loop and return ```i```.

## Algorithmic Complexity
- Binary Search
  - Time Complexity: O(log(x))
    - The range of possible values is halved at each step, resulting in a logarithmic time complexity.
  - Space Complexity: O(1)
    - Only a fixed amount of extra space is used for variables like ```left```, ```right```, and ```mid```.
- Iterative Incremental Search
  - Time Complexity: O(√x)
    - The loop iterates up to √x times since ```i² > x``` breaks the loop.
  - Space Complexity: O(1)
    - Only a fixed amount of extra space is used for variables like ```i``` and ```ans```.

## Notes on Solving Process
- Binary Search:
  - Efficient for large inputs due to its logarithmic time complexity.
  - Suitable for problems where the solution space can be narrowed down systematically.
- Iterative Incremental Search:
  - Simpler to implement and understand but very inefficient for large inputs.
  - Useful when the range of possible solutions is small.