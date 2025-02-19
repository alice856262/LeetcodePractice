## Algorithm Description
### Key Idea
- Determine the maximum number of complete rows that can be formed in a staircase where the ```i```th row has exactly ```i``` coins, given a total of ```n``` coins.
- Three methods were implemented:
  - Binary Search Approach: Use **binary search** to find the largest integer ```k``` such that the sum of the first ```k``` natural numbers, given by Gauss's formula ```k * (k + 1) / 2```, is less than or equal to ```n```.
  - Mathematical (Quadratic Formula) Approach: Use a **mathematical approach** by solving the quadratic inequality derived from Gauss's formula ```k * (k + 1) / 2 <= n```. This leads to ```k = (-1 + sqrt(1 + 8*n)) / 2```; the answer is the floor of this value.
  - Simulation Approach: Use a **simulation approach** by iteratively adding row numbers until the total exceeds ```n```, then return the number of complete rows.

### Step-by-Step Algorithm
#### Method 1: Binary Search Approach
- Step 1: Initialize two pointers: ```left = 1``` and ```right = n```, and a variable ```ans = 0``` to store the maximum complete row count.
- Step 2: While ```left``` is less than or equal to ```right```:
  - Compute ```mid = (left + right) // 2```.
  - Calculate the total number of coins needed for ```mid``` rows using Gauss's formula: ```coins = mid * (mid + 1) // 2```.
  - If ```coins > n```, then the current mid is too high; update ```right = mid - 1```.
  - Otherwise, move the left pointer: ```left = mid + 1``` and update ```ans = mid```.
- Step 3: After the loop terminates, return ```ans``` as the maximum number of complete rows.
#### Method 2: Mathematical (Quadratic Formula) Approach
- Step 1: Recognize that the total coins needed for ```k``` rows is given by Gauss's formula: ```k * (k + 1) / 2 <= n```.
- Step 2: Multiply both sides by ```2``` and form the quadratic equation: ```k^2 + k - 2n <= 0```.
- Step 3: Solve for ```k``` using the quadratic formula: ```k = (-1 + sqrt(1 + 8n)) / 2```.
- Step 4: Since ```k``` must be an integer, return the floor of the result, i.e., ```int(k)```.
#### Method 3: Simulation Approach
- Step 1: Initialize two variables: ```row = 0``` to count the current row and ```count = 0``` to track the total coins used.
- Step 2: While ```count``` is less than or equal to ```n```:
  - Increment ```row``` by 1.
  - Add ```row``` to ```count``` (simulating placing coins in the next row).
- Step 3: If ```count == n```, return ```row```. If ```count``` exceeds ```n```, return ```row - 1``` (since the last row cannot be completed).

## Algorithmic Complexity
- Binary Search Approach
  - Time Complexity: O(log n)
    - The binary search iterates in logarithmic time.
  - Space Complexity: O(1)
    - Only a fixed number of variables are used.
- Mathematical (Quadratic Formula) Approach
  - Time Complexity: O(1)
    - Direct computation using the square root and arithmetic operations.
  - Space Complexity: O(1)
    - Only a few variables are needed.
- Simulation Approach
  - Time Complexity: O(k)
    - ```k``` is the number of complete rows (worst case: approximately O(√n)).
  - Space Complexity: O(1)
    - Only constant extra space is required.

## Notes on Solving Process
- Binary Search Approach:
  - Efficiently narrow down the potential number of rows by leveraging the monotonic nature of the coin sum.
- Mathematical (Quadratic Formula) Approach:
  - Extremely efficient with constant time, but require handling of floating-point arithmetic and proper flooring.
- Simulation Approach:
  - Simple and intuitive by simulating the actual process of building rows.
  - Slightly less efficient for very large n, but acceptable given the input constraints.