## Algorithm Description
### Key Idea
- Find the last word in the string and avoid extra spaces or trailing spaces that might interfere with the result.
- Two methods were implemented:
  - Built-in Function: Utilize Python's built-in string manipulation functions for simplicity and efficiency.
  - Manual Traversal: Traverse the string from the end to locate the last word and counting its length.

### Step-by-Step Algorithm
#### Method 1: Built-in Function
- Step 1: Trim any trailing and leading spaces using the ```strip()``` method.
- Step 2: Split the string into a list of words using the ```split()``` method.
- Step 3: Return the length of the last word using the ```len()``` function.
#### Method 2: Manual Traversal
- Step 1: Initialize a counter (```blank```) to count trailing spaces.
- Step 2: Traverse the string from the end to count the number of trailing spaces.
- Step 3: Create a new string excluding the trailing spaces.
- Step 4: Initialize a counter (```count```) for the length of the last word.
- Step 5: Traverse the string from the end until encountering a space to count the characters in the last word.
- Step 6: Return the value of the ```count```.

## Algorithmic Complexity
- Built-in Function
  - Time Complexity: O(n)
    - ```n``` is the length of the string. Both ```strip()``` and ```split()``` traverse the string once.
  - Space Complexity: O(k)
    - ```k``` is the number of words in the string (space used for the list of words).
- Manual Traversal
  - Time Complexity: O(n)
    - The string is traversed twice (once to count trailing spaces and once to count the length of the last word).
  - Space Complexity: O(1)
    - The algorithm uses constant extra space.

## Notes on Solving Process
- Built-in Function:
  - It is concise and leverages Python's built-in functions for simplicity.
- Manual Traversal:
  - It avoids creating additional data structures, making it more space-efficient.
- Edge Cases Considered in both methods:
  - Strings with multiple trailing spaces.
  - Strings with only one word.
  - Strings with no spaces at all.