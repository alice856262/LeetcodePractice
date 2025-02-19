## Algorithm Description
### Key Idea
- Leverage Python's built-in ```split()``` method to automatically split the input string into non-empty segments using whitespace as the delimiter.
- The length of the list returned by ```split()``` directly represents the number of segments (i.e., contiguous sequences of non-space characters) in the string.

### Step-by-Step Algorithm
- Step 1: Apply ```s.split()``` to the input string ```s```. This will divide the string into a list of substrings, **automatically ignoring any extra spaces**.
- Step 2: Compute the length of the resulting list using ```len()```, and return it as the final result.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the string ```s```, since the ```split()``` method iterates over the entire string.
- Space Complexity: O(n) (worst case)
  - The split operation may create a list containing up to ```n/2``` substrings (in the scenario of no spaces) or fewer if there are many spaces.

## Notes on Solving Process
- Using the built-in ```split()``` function significantly simplifies the solution by **handling all whitespace issues (multiple spaces, leading/trailing spaces) internally**, and ```s.split()``` would already return an empty list for a string that only contains spaces.
- The approach is efficient for the problem constraints since the string length is small (≤300), and built-in functions in Python are optimized.