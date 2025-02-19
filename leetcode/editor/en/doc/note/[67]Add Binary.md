## Algorithm Description
### Key Idea
- To add two binary strings, we must handle the addition digit by digit from the least significant bit to the most significant bit, accounting for any carry from previous additions.
- Two methods were implemented:
  - Iterative Addition: Iterative addition using pointers and a carry.
  - Built-in Function: Conversion to integers, summing, and converting back to binary.

### Step-by-Step Algorithm
#### Method 1: Iterative Addition
- Step 1: Initialize Variables:
  - Create an empty list result to store the binary digits of the sum.
  - Set carry to 0 to manage overflow during addition.
  - Define two pointers pointing to the last characters of strings ```a``` and ```b```.
- Step 2: Iterate Through the Strings:
  - Retrieve the current digits from ```a``` and ```b```, and compute the total as the sum of ```digit_a```, ```digit_b```, and ```carry```.
  - Append the least significant bit of total (```total % 2```) to the result.
  - Update carry as the most significant bit of total (```total // 2```).
- Step 3: Reverse the result list to obtain the correct binary sum order, and convert the list to a string.
#### Method 2: Built-in Function
- Step 1: Convert binary strings ```a``` and ```b``` to integers using ```int(a, 2)``` and ```int(b, 2)```.
- Step 2: Compute the sum, and convert the resulting sum back to a binary string using Python's ```bin()``` function.
- Step 3: Remove the "0b" prefix added by the ```bin()``` function when converting an integer to its binary representation.

## Algorithmic Complexity
- Iterative Addition
  - Time Complexity: O(n)
    - n is the maximum length of a and b. The loop runs for the maximum length of the two strings.
  - Space Complexity: O(n)
    - The result list stores all the digits of the binary sum, which has a size proportional to O(n).
- Built-in Function
  - Time Complexity: O(n)
    - Convert the strings to integers and back to binary both take O(n), and summation is a constant-time operation for these sizes.
  - Space Complexity: O(n)
    - The intermediate integer and binary representations require O(n) space.

## Notes on Solving Process
- Iterative Addition:
  - More manual but ensure deeper understanding of binary arithmetic.
  - More suitable for scenarios where bit-level operations are required.
- Built-in Function:
  - Leverage Python’s built-in capabilities for rapid implementation.
  - For extremely large inputs, leveraging string handling may result in slightly better performance due to reduced overhead.