## Algorithm Description
### Key Idea
- An anagram is defined as two strings containing the same characters with the same frequency, regardless of their order.
- Two methods were implemented:
  - Dictionary Approach: Use dictionaries to count character frequencies and compare the counts.
  - Sorting Approach: Sort both strings and check if they are identical.

### Step-by-Step Algorithm
#### Method 1: Dictionary Approach
- Step 1: Check if the lengths of ```s``` and ```t``` are equal. If not, return ```False```.
- Step 2: Initialize two dictionaries (```dic_s``` and ```dic_t```) to store character frequencies for ```s``` and ```t```.
- Step 3: Traverse string ```s```. For each character, increment its frequency in ```dic_s```.
- Step 4: Traverse string ```t```. For each character, increment its frequency in ```dic_t```.
- Step 5: Return ```True``` if ```dic_s``` and ```dic_t``` are equal. Otherwise, return ```False```.
#### Method 2: Sorting Approach
- Step 1: Check if the lengths of ```s``` and ```t``` are equal. If not, return ```False```.
- Step 2: Sort both strings.
- Step 3: Compare the sorted strings. Return ```True``` if they are equal. Otherwise, return ```False```.

## Algorithmic Complexity
- Dictionary Approach
  - Time Complexity: O(n + k)
    - Building the frequency dictionaries takes O(n), where ```n = len(s)```.
    - Comparing the dictionaries takes O(k), where ```k``` is the number of unique characters.
  - Space Complexity: O(k)
    - Two dictionaries are used, each storing up to ```k``` entries.
- Sorting Approach
  - Time Complexity: O(n log n)
    - Sorting both strings takes O(n log n). 
    - Comparing the sorted strings takes O(n).
  - Space Complexity: O(n)
    - Sorting requires O(n) additional space if not done in-place.

## Notes on Solving Process
- Dictionary Approach:
  - More efficient for large inputs with a small character set (e.g., lowercase English letters).
  - Handles Unicode characters seamlessly with the same logic.
- Sorting Approach:
  - Simpler and intuitive but less efficient due to the sorting step.
  - Useful for quick implementation when performance is not critical.
- Both methods ensure correctness and work efficiently within the given constraints.