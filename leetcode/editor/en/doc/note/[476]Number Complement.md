## Algorithm Description
### Key Idea
- Given an integer ```num```, compute its complement by flipping all bits in its binary representation.
- Two methods were implemented:
  - Bit-by-Bit String Construction Approach: Process the number bit-by-bit. For each bit of ```num```, compute its complement and build a binary string. Finally, convert this string back to an integer.
  - Bitmask and XOR Approach: Compute a mask with the same number of bits as ```num``` (all bits set to ```1```), then use the XOR operation to flip all bits of ```num``` in a single step.

### Step-by-Step Algorithm
#### Method 1: Bit-by-Bit String Construction Approach
- Step 1: Initialize an empty string ```ans``` to store the binary representation of the complement.
- Step 2: While ```num``` is greater than ```0```:
  - Compute the complement of the least significant bit using ```(~num) & 1```.
  - Prepend this bit (converted to a string) to ```ans```.
  - Right shift ```num``` by one (i.e., ```num >>= 1```) to process the next bit.
- Step 3: Convert the binary string ```ans``` to a **base-2 integer** using ```int(ans, 2)``` and return the result.
#### Method 2: Bitmask and XOR Approach
- Step 1: Determine the number of bits in ```num``` using ```num.bit_length()```.
- Step 2: Construct a mask with all bits set to ```1``` for that bit-length using ```(1 << num.bit_length()) - 1```.
- Step 3: Compute the complement by performing an **XOR** between ```num``` and the mask (```num ^ mask```) and return the result.

## Algorithmic Complexity
- Bit-by-Bit String Construction Approach
  - Time Complexity: O(b²)
    - The loop runs for ```b``` iterations where ```b``` is the number of bits.
    - String concatenation creates a new string, and its time cost is proportional to the length of ```ans```. It costs O(1) for the first iteration, O(2) for the second iteration, up to O(b) for the ```bth``` iteration.
  - Space Complexity: O(b)
    - Space is used to store the binary string of length ```b```.
- Bitmask and XOR Approach
  - Time Complexity: O(b)
    - Calculating ```bit_length()```, constructing the mask, and performing an XOR are all linear in the number of bits, which is constant for fixed-width integers.
  - Space Complexity: O(1)
    - Only a few integer variables are used.

## Notes on Solving Process
- Bit-by-Bit String Construction Approach:
  - This approach is more illustrative of the bit-by-bit manipulation process by manually computing the complement of each bit.
  - The use of string concatenation (especially prepending) can be less efficient due to potential O(b) operations per iteration.
- Bitmask and XOR Approach:
  - This method leverages efficient bit manipulation and avoids the overhead of string operations.
  - By constructing a mask that matches the bit-length of ```num``` and using **XOR**, it computes the complement in a concise and efficient manner.