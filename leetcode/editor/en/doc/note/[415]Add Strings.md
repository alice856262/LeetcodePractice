## Algorithm Description
### Key Idea
- Simulate Manual Addition: Instead of converting the strings to integers, add the numbers digit by digit, starting from the least significant digit.
- Handle Carry and Different Lengths: Use a carry variable to handle sums greater than 9 and ensure that the algorithm correctly handles numbers of different lengths by treating out-of-bound digits as 0.

### Step-by-Step Algorithm
- Step 1: Initialize two pointers, ```i1``` and ```i2```, to point to the last character (least significant digit) of ```num1``` and ```num2``` respectively, set ```carry``` to 0, and initialize an empty string ```ans``` to store the result.
- Step 2: Loop while at least one pointer is within bounds or there is a non-zero carry:
  - Retrieve the current digit from ```num1``` using pointer ```i1``` (if ```i1``` is out of bounds, use 0) and similarly for ```num2``` using pointer ```i2```.
- Step 3: Calculate the sum of the two digits plus the ```carry``` from the previous iteration.
- Step 4: Update the ```carry``` by taking the integer division of the total by 10.
- Step 5: Determine the current digit (the remainder when divided by 10) and prepend it to ```ans```.
- Step 6: Decrement both pointers to move to the next significant digit.
- Step 7: Once the loop ends, return the resulting string ```ans``` as the sum.

## Algorithmic Complexity
- Time Complexity: O(n + m)
  - ```n``` and ```m``` are the lengths of ```num1``` and ```num2``` respectively, since each digit is processed exactly once.
- Space Complexity: O(n + m)
  - The result string's length is proportional to the number of digits processed, which may be one more than the length of the longest input string.

## Notes on Solving Process
- The approach mimics manual addition, handling digits from right to left while correctly managing the carry.
- Out-of-bound indexes are handled by treating missing digits as 0, ensuring that numbers of unequal length are processed correctly.
- The result is built by prepending digits to ensure that the final string is in the correct order, as digits are processed from least to most significant.