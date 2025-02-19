## Algorithm Description
### Key Idea
- The goal is to convert a given 32-bit integer (which can be negative) to its hexadecimal representation using two's complement for negative numbers.
  - Masking with ```0xFFFFFFFF```:
    - ```0xFFFFFFFF``` in hexadecimal equals a binary number with 32 ones (i.e., ```11111111 11111111 11111111 11111111```).
    - When perform ```num &= 0xFFFFFFFF```, the bitwise AND operation retains only the lowest 32 bits of ```num``` and clears any higher bits.
    - This simulates a 32-bit integer representation, ensuring that even negative numbers (which in Python have infinite sign extension) are correctly represented in 32-bit two's complement form.
  - Using Bitwise **AND** to Extract a Digit:
    - A hexadecimal digit is represented by 4 bits. The mask ```0xF``` in binary is ```1111```, which corresponds to 15 in decimal.
    - When perform ```num & 0xF```, it extracts the last 4 bits of ```num```, yielding a value between 0 and 15.
    - This value directly maps to a hexadecimal digit (using a lookup string or dictionary, e.g., ```0123456789abcdef```).
- Two methods were implemented:
  - Bitwise Approach: Use bitwise operations to extract 4 bits at a time (using bitwise AND with ```0xf```) and right shift the number. Prepend the corresponding hexadecimal digit to the result string.
  - Division and Modulo Approach: Use arithmetic operations (modulo 16 and integer division by 16) to extract hexadecimal digits, append them to the result string, and then reverse the string.

### Step-by-Step Algorithm
#### Method 1: Bitwise Approach
- Step 1: Initialize ```hex_digits``` as the string ```0123456789abcdef``` and an empty string ```ans```.
- Step 2: If ```num``` is 0, return ```0```.
- Step 3: If ```num``` is negative, convert it to its **32-bit two's complement representation** using ```num &= 0xFFFFFFFF```.
- Step 4: While ```num``` is not zero:
  - Extract the last 4 bits using ```num & 0xf```.
  - Prepend the corresponding digit from ```hex_digits``` to ```ans```.
  - Right shift ```num``` by 4 bits (```num >>= 4```).
- Step 5: Return the resulting string ```ans```.
#### Method 2: Division and Modulo Approach
- Step 1 ~ 3: same as Bitwise Approach.
- Step 4: While ```num``` is greater than 0:
  - Compute ```remainder = num % 16``` to get the last hexadecimal digit.
  - Update ```num``` by performing integer division by 16 (```num //= 16```).
  - Append the character corresponding to ```remainder``` (using ```hex_digits[remainder]```) to ```ans```.
- Step 5: Reverse the string ```ans``` (since the digits were collected in reverse order) and return the result.

## Algorithmic Complexity
- Bitwise Approach
  - Time Complexity: O(1)
    - The while loop processes 4 bits at a time for a 32-bit number, leading to at most 8 iterations.
  - Space Complexity: O(1)
    - Only a constant amount of extra space is used.
- Division and Modulo Approach
  - Time Complexity: O(1)
    - The loop iterates a fixed number of times (at most 8 iterations for a 32-bit number).
  - Space Complexity: O(1)
    - Use a constant amount of extra space.

## Notes on Solving Process
- Bitwise Approach:
  - Directly manipulates bits using bitwise operations, which are typically fast.
  - Prepending the digit avoids the need for reversing the final string.
- Division and Modulo Approach:
  - Easy to understand, but involve an extra step of reversing the string.