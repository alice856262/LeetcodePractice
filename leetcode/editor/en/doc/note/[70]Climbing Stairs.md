## Algorithm Description
### Key Idea
- The problem is essentially finding the n-th Fibonacci number with initial conditions ```f(1) = 1``` and ```f(2) = 2```.
- To climb ```n``` steps, either take 1 step after climbing ```n−1``` steps or take 2 steps after climbing ```n−2``` steps.
- This gives the recurrence relation: ```f(n) = f(n−1) + f(n−2)```, and the goal is to compute ```f(n)``` efficiently.

### Step-by-Step Algorithm
- Step 1: Initialize Base Cases:
  - If ```n = 1```, return 1 (only one way to climb).
  - If ```n = 2```, return 2 (two distinct ways to climb).
- Step 2: Iterative Dynamic Programming:
  - Use two variables to keep track of ```f(n−1)``` and ```f(n−2)```.
  - Iterate from 3 to ```n``` and compute ```f(n)``` as ```f(n−1) + f(n−2)```.
- Step 3: After the loop, the result is stored in the variable representing ```f(n)```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - The solution iterates from 3 to ```n```, performing O(1) work per iteration.
- Space Complexity: O(1)
  - Only a constant amount of space is used for variables ```prev1``` and ```prev2```.

## Notes on Solving Process
- Dynamic Programming:
  - The iterative approach is more efficient than a recursive solution, as it avoids recomputing overlapping subproblems.
- Scalability:
  - The algorithm can handle the constraint 1 ≤ ```n``` ≤ 45 comfortably within linear time and constant space.