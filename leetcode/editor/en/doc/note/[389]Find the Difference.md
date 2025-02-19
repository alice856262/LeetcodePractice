## Algorithm Description
### Key Idea
- Identify the extra one letter in string ```t``` that is not present in string ```s```.
- Two methods were implemented:
  - XOR Approach: Leverage the XOR operator's property where a number XORed with itself cancels out (i.e., ```a ^ a = 0```) and any number XORed with 0 remains unchanged. By XORing all the characters in ```s``` and ```t``` (using their ASCII values), matching letters cancel each other, leaving only the extra letter.
  - Frequency Dictionary Approach: Build a frequency dictionary for the letters in ```s```, and iterate through ```t``` to find the letter that cannot be matched or whose count falls below 1.

### Step-by-Step Algorithm
#### Method 1: XOR Approach
- Step 1: Initialize a variable ```result``` to 0.
- Step 2: Loop through each character in ```s```:
  - Convert the character to its ASCII value using ```ord(ch)``` and XOR it with ```result```.
- Step 3: Loop through each character in ```t```:
  - Convert the character to its ASCII value using ```ord(ch)``` and XOR it with ```result```.
- Step 4: Convert the final ```result``` (which is the ASCII value of the extra letter) back to a character using ```chr(result)``` and return it.
#### Method 2: Frequency Dictionary Approach
- Step 1: Create an empty dictionary ```s_dict``` to store the frequency of each character in ```s```.
- Step 2: Iterate over ```s``` and update ```s_dict``` with the count of each character.
- Step 3: Iterate over each character in ```t```:
  - If the character exists in ```s_dict``` and its count is greater than 0, decrement the count.
  - If the character is not present or its count is zero, return that character as it is the extra letter.

## Algorithmic Complexity
- XOR Approach
  - Time Complexity: O(n)
    - ```n``` is the total number of characters in ```s``` and ```t``` (i.e., O(len(s) + len(t)))
  - Space Complexity: O(1)
    - Only a constant amount of extra space is used for the variable ```result```.
- Frequency Dictionary Approach
  - Time Complexity: O(n)
    - Building the dictionary takes O(len(s)) and iterating through ```t``` takes O(len(t)).
  - Space Complexity: O(1)
    - The dictionary holds at most 26 keys since the strings consist of lowercase English letters, which is considered constant space.

## Notes on Solving Process
- XOR Approach:
  - Use XOR, a bit manipulation technique, to cancel out matching characters efficiently.
  - This approach is typically more efficient in practice due to fewer operations and its concise nature.
- Frequency Dictionary Approach:
  - This approach is intuitive but slightly more verbose due to dictionary management.