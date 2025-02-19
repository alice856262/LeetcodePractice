## Algorithm Description
### Key Idea
- Symbols are typically added unless a smaller-value symbol precedes a larger-value symbol, indicating subtraction.
- Process the string one character at a time, deciding whether to add or subtract the value based on the relative order of symbols.

### Step-by-Step Algorithm
- Step 1: Create a dictionary (```roman_to_int```) to store the integer values of Roman numeral symbols.
- Step 2: Initialize Variables
  - Use ```result``` to store the cumulative integer value.
  - Use ```n``` to represent the length of the input string ```s```.
- Step 3: Iterate Through Each character ```i``` in the String:
  - Check if ```i``` is followed by a larger-value symbol.
  - If so, subtract the value of the current symbol (```result -= roman_to_int[s[i]]```).
  - Otherwise, add the value of the current symbol (```result += roman_to_int[s[i]]```).
- Step 4: After the loop completes, result contains the final integer equivalent of the Roman numeral.

## Algorithmic Complexity
- Time Complexity: O(n)
  - Iterates through the string once.
- Space Complexity: O(1)
  - Uses a fixed dictionary and constant space for computation.

## Notes on Solving Process
- Iterative Decision Making:
  - The algorithm decides at each step whether to add or subtract, based on the relative order of the current and next symbols.
- Efficient Processing:
  - A single loop processes the entire string in O(n) time, where n is the length of the Roman numeral string.
  - Space complexity is O(1), as the algorithm uses only a fixed dictionary and integer variables.