## Algorithm Description
### Key Idea
- Use a frequency dictionary to count how many times each character appears in the string.
- Traverse the string in order to identify the first character that appears exactly once by checking the dictionary.

### Step-by-Step Algorithm
- Step 1: Initialize an empty dictionary to hold character counts.
- Step 2: Loop through each character in the string:
  - If the character is already in the dictionary, increment its count.
  - Otherwise, add the character to the dictionary with a count of ```1```.
- Step 3: Loop through the string again using ```enumerate``` to get **both the character and its index**:
  - If the character's count in the dictionary is ```1```, return the current index.
- Step 4: If no character with a count of ```1``` is found, return ```-1```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the length of the string. Two passes are made over the string.
- Space Complexity: O(1)
  - The dictionary stores at most 26 keys for lowercase English letters.

## Notes on Solving Process
- The use of a frequency dictionary allows for constant-time lookups when checking character frequencies.
- Edge cases, such as when no unique character exists, are handled by returning ```-1```.