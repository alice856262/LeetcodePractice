## Algorithm Description
### Key Idea
- The goal is to repeatedly sum the digits of an integer until the result is a single-digit number.
- Two methods were implemented:
  - Iterative Method: Simulate the digit-summing process using a loop by repeatedly calculating the sum of the digits until the number is reduced to a single digit.
  - Mathematical Method: Use the digital root formula to directly compute the result in constant time without iterative computation.

### Step-by-Step Algorithm
#### Method 1: Iterative Method
- Step 1: If the input number is already a single digit (```< 10```), return it directly.
- Step 2: Convert the number to a string to iterate through its digits.
- Step 3: Sum Digits
  - Use a loop to calculate the sum of the digits of the number.
  - Convert the sum back to a string and repeat until its length is 1.
- Step 4: When the length of the number string is 1, return the computed sum.
#### Method 2: Mathematical Method
- Step 1: If the number is 0, return 0.
- Step 2: Digital Root Calculation
  - Use the formula ```1 + (num - 1) % 9``` to compute the single-digit result directly.
- Step 3: Return the result of the formula.

## Algorithmic Complexity
- Iterative Method
  - Time Complexity: O(log<sub>10</sub> num)
    - Each iteration reduces the number by summing its digits, proportional to O(log<sub>10</sub> num).
  - Space Complexity: Ο(1)
    - No additional space is used beyond variables for the computation.
- Mathematical Method
  - Time Complexity: Ο(1)
    - The formula computes the result in constant time.
  - Space Complexity: Ο(1)
    - No additional space is used.

## Notes on Solving Process
- Iterative Method:
  - Useful for understanding the iterative process of summing digits.
  - Slower than the mathematical approach but conceptually simpler.
- Mathematical Method:
  - Highly efficient due to its constant-time computation.
  - Leverages the properties of modular arithmetic to compute the digital root directly.