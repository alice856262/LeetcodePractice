## Algorithm Description
### Key Idea
- Calculate the ```n```-th Fibonacci number, where ```F(0) = 0```, ```F(1) = 1```, and for ```n > 1```, ```F(n) = F(n - 1) + F(n - 2)```.
- Two methods were implemented:
  - Iterative Approach: Build the Fibonacci sequence from the bottom up by iterating from ```2``` to ```n```, updating two variables that represent the last two Fibonacci numbers.
  - Naive Recursive Approach: Compute the Fibonacci number using the direct recursive formula, which naturally follows the definition but results in many redundant calculations.

### Step-by-Step Algorithm
#### Method 1: Iterative Approach
- Step 1: Check if ```n``` is less than ```2```. If true, return ```n``` (since ```F(0) = 0``` and ```F(1) = 1```).
- Step 2: Initialize two variables, ```a``` and ```b```, to represent ```F(0)``` and ```F(1)``` respectively.
- Step 3: Loop from ```2``` up to and including ```n```:
  - Update ```a``` and ```b``` such that ```a``` becomes the previous ```b```, and ```b``` becomes ```a + b``` (the next Fibonacci number).
- Step 4: After the loop completes, return ```b``` as ```F(n)```.
#### Method 2: Naive Recursive Approach
- Step 1: If ```n == 0```, return ```0```; if ```n == 1```, return ```1```.
- Step 2: Recursively compute ```F(n - 1)``` and ```F(n - 2)``` and return their sum as ```F(n)```.

## Algorithmic Complexity
- Iterative Approach
  - Time Complexity: O(n)
    - The algorithm iterates from ```2``` to ```n```, performing a constant amount of work per iteration.
  - Space Complexity: O(1)
    - Only a fixed number of variables are used, independent of ```n```.
- Naive Recursive Approach
  - Time Complexity: O(2<sup>n</sup>)
    - Each call to ```fib``` generates two recursive calls, leading to exponential growth in the number of calls.
  - Space Complexity: O(n)
    - Worst case: the recursion stack can grow to a depth of ```n```.

## Notes on Solving Process
- Iterative Approach:
  - This approach avoids the exponential blow-up seen in the recursive approach, which is preferred when performance is a concern.
  - By keeping only two variables to store intermediate results, it achieves constant space usage.
- Naive Recursive Approach:
  - This approach directly mirrors the mathematical definition of Fibonacci numbers. However, it suffers from many repeated calculations due to overlapping sub-problems.
  - For larger values of ```n```, this method becomes impractical unless optimized with memoization or dynamic programming.