## Algorithm Description
### Key Idea
- Solve the problem without converting the number into a string.
- Use mathematical operations to reverse half of the digits of the number.
- Compare the reversed half to the remaining half of the number to check for equality.
- Reduce unnecessary computation and avoid the use of extra space for a string conversion.

### Step-by-Step Algorithm
- Step 1: Handle Edge Cases
  - Negative numbers: These cannot be palindromes because of the leading ```-```.
  - Numbers ending in 0 (except 0 itself): These cannot be palindromes.
- Step 2: Reverse Half of the Number
  - Use a while loop to reverse digits from the end of the number until the remaining half is less than or equal to the reversed half.
  - In each iteration:
    - Extract the last digit (```x % 10```) and append it to the reversed half.
    - Remove the last digit from the original number (```x //= 10```).
- Step 3: Compare the Two Halves
  - For even-length numbers: The two halves should be equal.
  - For odd-length numbers: Disregard the middle digit by dividing the reversed half by 10.
- Step 4: Check if the original half and the reversed half satisfy the palindrome condition.

## Algorithmic Complexity
- Time Complexity: O(log₁₀(n))
  - The number of digits determines the number of iterations.
- Space Complexity: O(1)
  - The algorithm uses constant extra space.

## Notes on Solving Process
- Mathematical Approach:
  - Eliminates the need for extra memory or string manipulation.
  - Reversing half the digits improves efficiency.
- Edge Case Handling:
  - Ensure negative numbers and trailing zeros are appropriately excluded.