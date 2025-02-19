## Algorithm Description
### Key Idea
- Compute the number of 1's in the binary representation for each integer from 0 to ```n```.
- Two methods were implemented:
  - Bit Manipulation: Use a dynamic programming approach based on the observation that the number of 1's in ```i``` is equal to the number of 1's in ```i >> 1``` (i.e., ```i``` divided by 2) plus the value of the least significant bit (```i & 1```).
  - Iterative Method: Count the bits by manually iterating through each bit of the number using arithmetic operations (i.e., repeatedly taking ```i % 2``` and dividing ```i``` by 2).

### Step-by-Step Algorithm
#### Method 1: Bit Manipulation
- Step 1: Initialize an answer array ```ans``` of length ```n + 1``` with all elements set to 0.
- Step 2: Iterate through the numbers from ```1``` to ```n```:
  - Compute ```i >> 1``` to obtain the number ```i``` divided by 2, which effectively removes the least significant bit.
  - Compute ```(i & 1)``` to determine if the least significant bit of ```i``` is 1.
  - Set ```ans[i] = ans[i >> 1] + (i & 1)```.
#### Method 2: Iterative Method
- Step 1: Initialize an answer array ```ans``` of length ```n + 1``` with all elements set to 0.
- Step 2: Iterate through each number ```i``` from ```0``` to ```n```:
  - Initialize a counter ```count``` to 0 and set a temporary variable ```temp``` to ```i```.
  - While ```temp``` is greater than 0:
    - Increment ```count``` by ```temp % 2``` (this checks whether the current least significant bit is 1).
    - Update ```temp``` with ```temp //= 2``` to remove the least significant bit.
  - Set ```ans[i]``` to the computed ```count```.

## Algorithmic Complexity
- Bit Manipulation
  - Time Complexity: O(n)
    - Each number from 1 to ```n``` is processed in constant time (using bit shift and bitwise AND).
  - Space Complexity: O(n)
    - An additional array of size ```n + 1``` is used to store the results.
- Iterative Method
  - Time Complexity: O(n log n)
    - For each number ```i```, the while loop iterates approximately O(log i) times (since the number of bits in ```i``` is proportional to ```log(i)```).
  - Space Complexity: O(n)
    - An additional array of size ```n + 1``` is used to store the results.

## Notes on Solving Process
- Bit Manipulation:
  - Leverage previously computed results by recognizing that the bit count of ```i``` can be quickly derived from that of ```i >> 1```.
  - Use bit manipulation operations which are efficient and executed in constant time.
- Iterative Method:
  - Implement the fundamental approach of counting bits by repeatedly checking the least significant bit.
  - Although more intuitive, this method is less efficient when dealing with large inputs due to the logarithmic factor in each number's bit processing.