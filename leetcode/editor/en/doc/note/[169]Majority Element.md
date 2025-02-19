## Algorithm Description
### Key Idea
- The majority element in an array is defined as the element that appears more than ```n/2``` times, where ```n``` is the size of the array.
- Three methods were implemented:
  - Boyer-Moore Voting Algorithm: Use a single pass through the array to find the candidate for the majority element and verify it.
  - Dictionary Approach: Count the occurrences of each element using a hash map.
  - Sorting Approach: Sort the array and return the middle element, as it must be the majority element.

### Step-by-Step Algorithm
#### Method 1: Boyer-Moore Voting Algorithm
- Step 1: Initialize ```candidate``` as ```None``` and ```count``` as ```0```.
- Step 2: Traverse the array:
  - If ```count``` is 0, set ```candidate``` to the current element.
  - Increment ```count``` if the current element equals the ```candidate```; otherwise, decrement ```count```.
- Step 3: After traversing the array, ```candidate``` will hold the majority element.
#### Method 2: Dictionary Approach
- Step 1: Initialize an empty dictionary ```counts``` to store the frequency of each element.
- Step 2: Traverse the array and increment the count for each element in the dictionary.
- Step 3: After traversing the array, iterate through the dictionary and return the element whose count is greater than ```n/2```.
#### Method 3: Sorting Approach
- Step 1: Sort the input array.
- Step 2: The majority element will always occupy the **middle** position of the sorted array. Return the element at index ```n/2```.

## Algorithmic Complexity
- Boyer-Moore Voting Algorithm
  - Time Complexity: O(n)
    - ```n``` is the size of the array, as the array is traversed once.
  - Space Complexity: O(1)
    - No additional space is used.
- Dictionary Approach
  - Time Complexity: O(n)
    - Traverse the array once and check the dictionary.
  - Space Complexity: O(n)
    - The frequency of each unique element is stored in the dictionary.
- Sorting Approach
  - Time Complexity: O(n log n)
    - Due to the list sorting step.
  - Space Complexity: O(1) or O(n)
    - O(1) if the sorting is done in-place, or O(n) if using additional memory for sorting.

## Notes on Solving Process
- Boyer-Moore Voting Algorithm:
  - Most efficient method in terms of both time and space.
  - Relies on the assumption that a majority element always exists in the input.
- Dictionary Approach:
  - Useful for understanding frequency counts but less space-efficient.
- Sorting Approach:
  - Simple to implement and guarantees correctness because the majority element must appear at the middle position.
  - Slightly less efficient due to the sorting step.