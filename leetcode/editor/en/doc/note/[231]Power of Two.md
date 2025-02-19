## Algorithm Description
### Key Idea
- A number is a power of two if it has only one bit set in its binary representation.
- Use properties of bitwise operations or iterative division to determine if the number is a power of two.
- Two methods were implemented:
  - Bitwise Manipulation: Leverage the bitwise AND (```&```) operation to efficiently check the binary representation.
  - Iterative Division: Repeatedly divide the number by 2 while checking if it is divisible.

### Step-by-Step Algorithm
#### Method 1: Bitwise Manipulation
- Step 1: If the number is less than or equal to 0, return ```False```.
- Step 2: Use the property ```(n & (n - 1)) == 0``` to check for powers of two.
- Step 3: If the result is 0, ```n``` is a power of two; otherwise, it is not.
#### Method 2: Iterative Division
- Step 1: If the number is less than or equal to 0, return ```False```.
- Step 2: Initialize a variable ```remainder``` to 0.
- Step 3: While ```n > 0``` and ```remainder == 0```:
  - Compute the remainder of ```n``` when divided by 2.
  - Divide ```n``` by 2 and continue.
- Step 4: If ```n``` becomes 0 after the loop, return ```True```. Otherwise, return ```False```.

## Algorithmic Complexity
- Bitwise Manipulation
  - Time Complexity: O(1)
    - Bitwise operations take constant time regardless of the input size.
  - Space Complexity: O(1)
    - No additional memory is used.
- Iterative Division
  - Time Complexity: O(log n)
    - Each iteration divides ```n``` by 2, requiring ```log n``` iterations.
  - Space Complexity: O(1)
    - No additional memory is used.

## Notes on Solving Process
- Bitwise Manipulation:
  - Efficient and uses mathematical properties of powers of two.
  - Best suited for performance-critical scenarios.
- Iterative Division:
  - Simpler and intuitive approach using iterative division.
  - Slower for large numbers due to ```log n``` iterations.