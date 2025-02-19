## Algorithm Description
### Key Idea
- Determine if string ```s``` is a subsequence of string ```t```, meaning all characters in ```s``` appear in ```t``` in the same order, though not necessarily consecutively.
- Two methods were implemented:
  - Two Pointer Approach: Use a **two pointer approach** to iterate through both strings simultaneously, advancing the pointer in ```s``` when a matching character is found in ```t```.
  - Preprocessing with Binary Search: Preprocess ```t``` by mapping each character to a list of its indices, then for each character in ```s```, use **binary search** to quickly locate the next occurrence in ```t``` that comes after the previous match.

### Step-by-Step Algorithm
#### Method 1: Two Pointer Approach
- Step 1: Handle Edge Case:
  - If ```len(s) > len(t)```, return ```False``` (```s``` cannot be a subsequence of a shorter string).
  - If ```s``` is empty, return ```True``` (an empty string is a subsequence of any string).
- Step 2: Initialize two pointers: ```s_pointer = 0``` and ```t_pointer = 0```.
- Step 3: While ```s_pointer < len(s)``` and ```t_pointer < len(t)```:
  - If ```s[s_pointer] == t[t_pointer]```, increment ```s_pointer``` (a match is found).
  - Increment ```t_pointer``` (always advance in ```t```).
- Step 4: After the loop, return ```True``` if ```s_pointer == len(s)``` (all characters in ```s``` were matched), otherwise return ```False```.
#### Method 2: Preprocessing with Binary Search
- Step 1: Preprocess ```t``` by storing each character's index in a dictionary (```t_dict```) where keys are characters and values are **lists of indices**.
- Step 2: Initialize a variable ```current``` to 0, which represents the minimum acceptable index in ```t``` for the next character from ```s```.
- Step 3: For each character ```symbol``` in ```s```:
  - Use ```bisect_left``` on ```t_dict[symbol]``` to find the **smallest index** that is **not less than ```current```**.
  - If no such index exists (i.e., ```bisect_left``` returns an index equal to the length of the list), return ```False```.
  - Otherwise, update ```current``` to that found index plus 1 (to ensure subsequent characters appear later in ```t```).
- Step 4: After processing all characters in ```s```, return ```True``` because all characters were found in order in ```t```.

## Algorithmic Complexity
- Two Pointer Approach
  - Time Complexity: O(n + m)
    - ```n = len(s)``` and ```m = len(t)```; each pointer traverses its string at most once.
  - Space Complexity: O(1)
    - Only a fixed number of pointer variables are used.
- Preprocessing with Binary Search
  - Time Complexity: O(m + n log m)
    - Preprocessing: Building the dictionary by iterating over ```t``` takes O(m).
    - Query: For each of the ```n``` characters in ```s```, we perform a binary search on a list of indices in ```t```, which takes O(log m) time in the worst case. This step takes O(n log m).
  - Space Complexity: O(m)
    - The dictionary stores indices for each character in ```t```.

## Notes on Solving Process
- Two Pointer Approach:
  - Efficient for a single query since it requires just one pass through both strings.
  - Not optimized for scenarios with a huge number of queries on the same string ```t```.
- Preprocessing with Binary Search:
  - Ideal for handling many queries efficiently, as ```t``` is preprocessed once. Uses binary search to quickly locate the next occurrence of each character.
  - Slightly more complex due to the preprocessing step and binary search implementation.