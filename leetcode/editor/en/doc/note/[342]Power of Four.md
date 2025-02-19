## Algorithm Description
### Key Idea
- Determine if an integer ```n``` is a power of four.
- Three methods were implemented:
  - Logarithm-based Check: Use logarithms. If log<sub>4</sub>(n) is an integer, then ```n``` is a power of four.
  - Bit Manipulation: Check that ```n``` is positive, has only one set bit (i.e., it is a power of two), and that the set bit is in one of the positions valid for a power of four.
  - Iterative Division: Repeatedly divide ```n``` by 4 as long as it is divisible by 4. If the process reduces ```n``` to 1, then ```n``` is a power of four.

### Step-by-Step Algorithm
#### Method 1: Logarithm-based Check
- Step 1: Check if ```n``` is positive. If not, return ```False```.
- Step 2: Compute log<sub>4</sub>(n) using a logarithm function.
- Step 3: Check if the result of the logarithm has no fractional part (i.e., log<sub>4</sub>(n) % 1 == 0).
  - If true, return ```True```; otherwise, return ```False```.
#### Method 2: Bit Manipulation
- Step 1: Ensure ```n``` is positive.
- Step 2: Check that ```n``` is a power of two. This is done using the condition: ```not(n & (n - 1))```, which returns ```True``` if ```n``` has exactly one set bit.
- Step 3: Confirm that the single set bit is in the correct position for a power of four.
  - Check that ```(n & 1431655765) == n```. If this holds, return ```True```; otherwise, return ```False```.
#### Method 3: Iterative Division
- Step 1: Check if ```n``` is less than or equal to 0. If so, return ```False```.
- Step 2: While ```n``` is greater than 1:
  - Calculate the remainder when dividing ```n``` by 4 (i.e., ```n % 4```).
  - If the remainder is not 0, return ```False``` because ```n``` is not divisible by 4.
  - Update ```n``` by performing integer division by 4 (i.e., ```n = n // 4```).
- Step 3: After the loop, if ```n``` is exactly 1, return ```True``` (indicating ```n``` is a power of four); otherwise, return ```False```.

## Algorithmic Complexity
- Logarithm-based Check
  - Time Complexity: O(1)
    - The logarithm operation and subsequent modulus check are constant-time operations.
  - Space Complexity: O(1)
    - Use a fixed number of variables.
- Bit Manipulation
  - Time Complexity: O(1)
    - Bitwise operations and comparisons are performed in constant time.
  - Space Complexity: O(1)
    - Use only a few extra variables.
- Iterative Division
  - Time Complexity: O(log n)
    - In each iteration, ```n``` is divided by 4, so the number of iterations is proportional to log<sub>4</sub>(n).
  - Space Complexity: O(1)
    - Only a constant amount of extra space is required.

## Notes on Solving Process
- Logarithm-based Check:
  - This approach leverages the mathematical property of logarithms to determine if ```n``` is a power of four.
  - It is simple and efficient, but one must be cautious of floating-point precision issues.
- Bit Manipulation:
  - This method uses bit-level operations to efficiently check if ```n``` is a power of four.
  - The key insight is to first verify that ```n``` is a power of two and then ensure that the single set bit is in the correct position using a bitmask.
- Iterative Division:
  - The iterative division approach is conceptually straightforward by simulating the process of dividing ```n``` by 4 until it reaches 1.
  - It is intuitive and easy to understand but may be less efficient than the other methods for very large ```n```.