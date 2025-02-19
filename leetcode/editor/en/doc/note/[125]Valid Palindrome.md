## Algorithm Description
### Key Idea
- A palindrome reads the same forward and backward, ignoring case and non-alphanumeric characters.
- Preprocess the string to retain only alphanumeric characters and then check if it reads the same forward and backward.
- Two methods were implemented:
  - Regular Expression and String Manipulation: Use a regular expression (`re.sub`) to remove all non-alphanumeric characters and compare the string to its reverse.
  - Character Filtering and Reverse Construction: Filter valid characters from the input string and construct two strings: one for the forward traversal and another for the reverse traversal.

### Step-by-Step Algorithm
#### Method 1: Regular Expression and String Manipulation
- Step 1: Remove all non-alphanumeric characters using ```re.sub``` with a pattern that matches everything except letters and numbers.
- Step 2: Convert the cleaned string to lowercase.
- Step 3: Reverse the cleaned string using slicing (```[::-1]```), and compare with its reversed version.
#### Method 2: Character Filtering and Reverse Construction
- Step 1: Define a string of valid alphanumeric characters (```abcdefghijklmnopqrstuvwxyz0123456789```).
- Step 2: Convert the input string to lowercase.
- Step 3: Iterate through the string and filter out non-alphanumeric characters to build the forward string.
- Step 4: Iterate backward through the forward string to construct the reversed string, and compare the forward and backward strings.

## Algorithmic Complexity
- Regular Expression and String Manipulation
  - Time Complexity: O(n)
    - ```n``` is the length of the string. Cleaning the string with ```re.sub``` takes O(n), and reversing the string also takes O(n).
  - Space Complexity: O(n)
    - The cleaned string and its reverse each take O(n) space.
- Character Filtering and Reverse Construction
  - Time Complexity: O(n)
    - Filtering valid characters while iterating through the string takes O(n). Constructing the reverse string also takes O(n).
  - Space Complexity: O(n)
    - The forward and backward strings each take O(n) space.

## Notes on Solving Process
- Regular Expression and String Manipulation:
  - This method is concise and leverages built-in Python functions for efficiency and simplicity.
- Character Filtering and Reverse Construction:
  - This method involves manual filtering and string construction, offering more control but requiring additional code.
- Both methods achieve the same result, but Method 1 is generally preferred for its readability and minimal code complexity.