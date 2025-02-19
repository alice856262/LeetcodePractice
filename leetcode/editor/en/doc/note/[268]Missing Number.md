## Algorithm Description
### Key Idea
- The problem involves finding the single missing number in a range ```[0, n]``` based on the input array of ```n``` distinct numbers.
- Three methods were implemented:
  - Sum Formula: Use the sum formula for numbers from ```0``` to ```n``` to compute the expected sum and compare it with the actual sum of elements in the array.
  - XOR Method: Use XOR to cancel out numbers that appear in both the range ```[0, n]``` and the array, leaving only the missing number.
  - Brute Force: Use brute force to check every number in the range ```[0, n]``` and identify the one not in the array.

### Step-by-Step Algorithm
#### Method 1: Sum Formula
- Step 1: Compute the expected sum of numbers from ```0``` to ```n``` using the formula: ```expected_sum = n * (n + 1) // 2```
- Step 2: Compute the actual sum of elements in the input array.
- Step 3: Return the difference: ```expected_sum - actual_sum```
#### Method 2: XOR Method
- Step 1: Initialize a variable ```result = 0```.
- Step 2: XOR all numbers in the range ```[0, n]``` and store the result in ```result```.
- Step 3: XOR all elements in the input array with ```result```. Numbers that appear in both the range and the array cancel out due to the XOR property: ```x ⊕ x = 0```.
- Step 4: Return the final value of ```result```, which is the missing number.
#### Method 3: Brute Force
- Step 1: Iterate through all numbers in the range ```[0, n]```.
- Step 2: For each number, check if it exists in the input array.
- Step 3: Return the first number that does not exist in the array.

## Algorithmic Complexity
- Sum Formula
  - Time Complexity: O(n)
    - Computing the sum of the array takes O(n).
  - Space Complexity: Ο(1)
    - Only a few variables are used for calculations.
- XOR Method
  - Time Complexity: O(n)
    - Two loops of size ```n``` are executed for XOR operations.
  - Space Complexity: Ο(1)
    - Only a single variable is used for the XOR operation.
- Brute Force
  - Time Complexity: O(n^2)
    - For each number in the range, a membership check in the array takes O(n).
  - Space Complexity: Ο(1)
    - No additional data structures are used.

## Notes on Solving Process
- Sum Formula:
  - This is the simplest approach, leveraging a mathematical formula to directly compute the missing number. It is efficient and easy to implement.
- XOR Method:
  - The XOR operation cancels out identical bits, so when a number is XORed with itself (```x ⊕ x = 0```), all bits become zero because they match perfectly.
  - This is efficient for large arrays, as it uses bitwise operations to achieve O(n) runtime with constant space.
- Brute Force:
  - This is the least efficient and should be avoided for large inputs due to its O(n^2) complexity.