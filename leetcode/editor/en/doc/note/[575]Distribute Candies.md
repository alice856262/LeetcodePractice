## Algorithm Description
### Key Idea
- Determine the maximum number of distinct candy types Alice can eat given that she can only consume half of the total candies.
- Two methods were implemented:
  - Set Method: Use a set to quickly obtain the number of distinct candy types, then return the minimum of this count and ```n/2```.
  - Dictionary Method: Use a dictionary to count occurrences of each candy type, and use the number of unique keys to determine the distinct types. Return the minimum between this number and ```n/2```.

### Step-by-Step Algorithm
#### Method 1: Set Method
- Step 1: Convert the input list ```candyType``` to a **set** to extract unique candy types.
- Step 2: Compute ```distinct_types``` as the size of the set.
- Step 3: Calculate ```max_candies``` as ```len(candyType) // 2```.
- Step 4: Return the minimum of ```distinct_types``` and ```max_candies```.
#### Method 2: Dictionary Method
- Step 1: Initialize an empty dictionary ```candy_dict``` to store the frequency of each candy type.
- Step 2: Calculate ```max_candies``` as ```len(candyType) // 2```.
- Step 3: Iterate over each candy in ```candyType```:
  - If the candy is not in ```candy_dict```, add it with a count of ```1```.
  - Otherwise, increment its count.
- Step 4: Return ```max_candies``` if the number of distinct candy types is greater than or equal to ```max_candies```; otherwise, return the number of distinct candy types.

## Algorithmic Complexity
- Set Method
  - Time Complexity: O(n)
    - Building a set from the list requires scanning through all ```n``` elements.
  - Space Complexity: O(n)
    - Worst case: all candy types are unique, the set will contain ```n``` elements.
- Dictionary Method
  - Time Complexity: O(n)
    - Each candy is processed once to update the dictionary.
  - Space Complexity: O(n)
    - Worst case: the dictionary will have ```n``` keys if every candy is unique.

## Notes on Solving Process
- Set Method:
  - It leverages Python's optimized set implementation to directly obtain the count of distinct elements.
  - The set method is generally faster in practice due to its lower constant-factor overhead.
- Dictionary Method:
  - Although it achieves the **same asymptotic complexity**, the dictionary method introduces a **slight overhead due to extra operations (checking key existence and updating counts)**.