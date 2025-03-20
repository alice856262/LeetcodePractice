## Algorithm Description
### Key Idea
- Determine if the capitalization usage in a given word is correct. A word is considered valid if: all letters are uppercase/lowercase, or only the first letter is uppercase and the remaining letters are lowercase.
- Two methods were implemented:
  - Manual Comparison: Manually compare the word against its uppercase and lowercase versions. For the mixed-case scenario, check that the first letter is uppercase and every subsequent letter matches the lowercase version.
  - Built-in String Method: Use Python's built-in string methods (```isupper()```, ```islower()```, and slicing) to directly check if the word satisfies one of the valid capitalization patterns.

### Step-by-Step Algorithm
#### Method 1: Manual Comparison
- Step 1: Compute ```upper_word``` as the uppercase version of ```word``` and ```lower_word``` as the lowercase version of ```word```.
- Step 2: If ```word``` is equal to ```upper_word``` or ```lower_word```, return ```True``` because the word is either all uppercase or all lowercase.
- Step 3: Otherwise, check if the first character of ```word``` is uppercase (i.e., ```word[0] == upper_word[0]```).
  - If the first character is uppercase, iterate from the second character (index ```1```) to the end of the word.
  - For each character, check if it matches the corresponding character in ```lower_word```.
  - If any character does not match, return ```False```. If all characters from index ```1``` match, return ```True```.
- Step 4: Any other pattern is invalid, return ```False```.
#### Method 2: Built-in String Method
- Step 1: Use the built-in method ```word.isupper()``` and ```word.islower()``` to check if the word is all uppercase/lowercase.
- Step 2: Use ```word[0].isupper()``` and ```word[1:].islower()``` to check if only the first letter is uppercase and the rest are lowercase.
- Step 3: Return ```True``` if any of these conditions hold; otherwise, return ```False```.

## Algorithmic Complexity
- Manual Comparison
  - Time Complexity: O(n)
    - The algorithm processes each character in the word once, either in the equality check or during the loop for the mixed-case scenario.
  - Space Complexity: O(n)
    - Extra space is used for storing ```upper_word``` and ```lower_word```, each of which is O(n) in size.
- Built-in String Method
  - Time Complexity: O(n)
    - The built-in methods ```isupper()```, ```islower()```, and the slicing operation iterate over the word once.
  - Space Complexity: O(n)
    - The slicing operation ```word[1:]``` creates a new substring of size O(n), contributing to the space usage.

## Notes on Solving Process
- Manual Comparison:
  - Provides a manual and explicit approach for determining valid capital usage by comparing the word against its uppercase and lowercase forms.
  - Uses a loop to check each character for the mixed-case scenario, which is straightforward but requires extra temporary string storage.
- Built-in String Method:
  - Leverages Python's built-in string functions for a more concise and idiomatic solution.
  - Although the operations are built-in, they still operate in linear time, leading to the same asymptotic complexity.