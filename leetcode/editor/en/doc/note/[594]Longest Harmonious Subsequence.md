## Algorithm Description
### Key Idea
- The goal is to determine the length of the longest harmonious subsequence from an integer array, where a harmonious subsequence is one whose maximum and minimum values differ by exactly ```1```.
- Use a dictionary to count the frequency of each element and then iterate over the dictionary's keys to identify pairs of consecutive integers. The sum of frequencies for any such pair represents the length of a harmonious subsequence, and the maximum such sum is returned.

### Step-by-Step Algorithm
- Step 1: Initialize an empty dictionary ```nums_dict```.
- Step 2: Iterate over each element in ```nums``` and update ```nums_dict``` to count the frequency of each number.
- Step 3: Initialize a variable ```max_length``` to ```0``` to track the maximum harmonious subsequence length.
- Step 4: Iterate through each key in ```nums_dict``` and check if ```key + 1``` exists in the dictionary:
  - If it does, update ```max_length``` to be the maximum of ```max_length``` and the sum of the frequencies of ```key``` and ```key + 1```.
- Step 5: Return ```max_length```.

## Algorithmic Complexity
- Time Complexity: O(n)
  - Building the dictionary requires scanning the array once.
  - Iterating over the dictionary keys takes O(u) where ```u``` is the number of unique elements, at most O(n).
- Space Complexity: O(n)
  - Worst case: all elements are unique, the dictionary will store ```n``` key-value pairs.

## Notes on Solving Process
- This approach avoids sorting by using a dictionary to directly count the frequency of each element.
- Iterating over the dictionary keys allows us to quickly check for consecutive numbers and compute the corresponding subsequence lengths.