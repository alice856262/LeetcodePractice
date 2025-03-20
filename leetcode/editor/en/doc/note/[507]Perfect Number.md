## Algorithm Description
### Key Idea
- Divisor Pairing: **Every divisor less than the square root of a number has a corresponding paired divisor greater than the square root**. This allows us to compute the sum of all proper divisors by iterating only up to the square root.
- Avoid Redundancy for Perfect Squares: When the number is a perfect square, ensure the square root is added only once to prevent double counting.

### Step-by-Step Algorithm
- Step 1: Check if ```num <= 1```. If so, return ```False``` since ```1``` is not a perfect number.
- Step 2: Initialize ```total = 1```, because ```1``` is always a proper divisor of any number greater than ```1```. Set a counter ```i = 2```.
- Step 3: Loop while ```i * i <= num```:
  - If ```num % i == 0```, then ```i``` is a divisor:
    - Add ```i``` to ```total```.
    - If ```i * i``` is not equal to ```num```, add ```num // i``` to ```total``` as well (the corresponding paired divisor).
  - Increment ```i```.
- Step 4: After the loop, check if ```total == num```. Return ```True``` if they are equal, otherwise return ```False```.

## Algorithmic Complexity
- Time Complexity: O(√n)
  - The loop runs until ```i * i``` exceeds ```num```, which means it iterates approximately ```√n``` times.
- Space Complexity: O(1)
  - Only a constant amount of extra space is used regardless of the input size.

## Notes on Solving Process
- The algorithm efficiently calculates the sum of proper divisors by leveraging the fact that divisors come in pairs, significantly reducing the number of iterations compared to a naive approach.
- Special handling for perfect squares prevents double counting the square root.
- This method is well-suited for large inputs due to its O(√n) time complexity and constant extra space usage.