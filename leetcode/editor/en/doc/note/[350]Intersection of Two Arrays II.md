## Algorithm Description
### Key Idea
- Find the intersection of two integer arrays such that each element in the result appears as many times as it does in both arrays.
- Two methods were implemented:
  - Frequency Dictionary Approach: Build a frequency dictionary from the smaller array, and iterate through the larger array. For each element, check if it exists in the frequency dictionary with a positive count.
  - Two Pointer Approach: Sort both arrays. Use two pointers (one for each array) to traverse them simultaneously, adding common elements to the result when both pointers point to the same value.

### Step-by-Step Algorithm
#### Method 1: Frequency Dictionary Approach
- Step 1: If one array is larger than the other, swap them so that the smaller array is used to build the frequency dictionary.
- Step 2: Create a frequency dictionary ```dict``` from the elements of the smaller array, counting how many times each element appears.
- Step 3: Iterate over the elements of the larger array.
  - For each element, check if it exists in ```dict``` and its count is greater than zero.
  - If so, add the element to the ```ans``` list and decrement its count in ```dict```.
#### Method 2: Two Pointer Approach
- Step 1: Sort both arrays.
- Step 2: Initialize two pointers, one for each sorted array (```i = 0``` for ```nums1``` and ```j = 0``` for ```nums2```).
- Step 3: Traverse the arrays using the two pointers:
  - If the element at ```nums1[i]``` is less than ```nums2[j]```, increment pointer ```i```.
  - If ```nums1[i]``` is greater than ```nums2[j]```, increment pointer ```j```.
  - If the elements are equal, add the element to ```ans``` and increment both pointers.
- Step 4: Continue until one of the pointers reaches the end of its array, then return ```ans```.

## Algorithmic Complexity
- Frequency Dictionary Approach
  - Time Complexity: O(n + m)
    - ```n``` is the length of the smaller array and ```m``` is the length of the larger array.
  - Space Complexity: O(n + min(n, m)) (worst case: O(n + m))
    - Frequency dictionary: O(n)
    - ```ans``` list: O(min(n, m))
- Two Pointer Approach
  - Time Complexity: O(n log n + m log m) (if not sorted) or O(n + m) (if sorted)
    - Sorting: O(n log n + m log m)
    - Two pointer traversal: O(n + m)
  - Space Complexity: O(1) extra space
    - Sorting in-place requires O(1) extra space (apart from the output).

## Notes on Solving Process
- Frequency Dictionary Approach:
  - Efficient for unsorted arrays, and optimized by using the smaller array for building the frequency dictionary.
  - Requires additional space for the dictionary.
- Two Pointer Approach:
  - Very efficient if the arrays are already sorted, using only O(1) extra space.
  - Sorting introduces extra overhead if arrays are initially unsorted.
- Follow-ups: 
  - If ```nums1``` And ```nums2``` Are Sorted:
    - **Two Pointer Approach** is preferable due to its linear time traversal (O(n + m)) and minimal extra space usage.
  - If ```nums1```'s Size Is Small Compared to ```nums2```'s Size:
    - **Frequency Dictionary Approach** is better since building the dictionary on the smaller array minimizes space usage and overall time.
  - If Elements of ```nums2``` Are Stored on Disk with Limited Memory:
    - If memory is limited, and one array is much smaller, the **Frequency Dictionary Approach** is beneficial. It stores all elements of the smaller array in the dictionary, and then sequentially loads and processes the larger array.
    - If neither ```nums1``` nor ```nums2``` fits into the memory, we split the numeric range into numeric sub-ranges that fit into the memory. Then, modify the **Frequency Dictionary Approach** to count only elements which belong to the given numeric sub-range.
    - If arrays are already sorted or can be sorted with low overhead, the **Two Pointer Approach** is optimal.