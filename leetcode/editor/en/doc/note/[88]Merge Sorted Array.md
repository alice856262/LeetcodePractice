## Algorithm Description
### Key Idea
- Merge two sorted arrays, ```nums1``` and ```nums2```, into a single sorted array in-place within ```nums1```.
- Two methods were implemented:
  - Two Pointer Approach from Back: Merge elements in reverse order, starting from the largest, to avoid overwriting existing elements in ```nums1```.
  - Combine and Sort: Combine valid elements of ```nums1``` and all elements of ```nums2``` into a temporary array, sorts it, and copies it back to ```nums1```.

### Step-by-Step Algorithm
#### Method 1: Two Pointer Approach from Back
- Step 1: Initialize three pointers:
  - ```p1``` pointing to the last valid element in ```nums1```.
  - ```p2``` pointing to the last element in ```nums2```.
  - ```p``` pointing to the last position in ```nums1``` (where the next largest element will be placed).
- Step 2: Compare the elements at ```p1``` and ```p2```, and repeat until either ```p1 < 0``` or ```p2 < 0```.
  - Place the larger element at position ```p``` in ```nums1```.
  - Decrement the pointer (```p1``` or ```p2```) and ```p```.
- Step 3: If elements remain in ```nums2```, copy them to the start of ```nums1```.
#### Method 2: Combine and Sort
- Step 1: Create a new array combining the first ```m``` elements of ```nums1``` and all ```n``` elements of ```nums2```.
- Step 2: Sort the combined array.
- Step 3: Copy the sorted array back into ```nums1```.

## Algorithmic Complexity
- Two Pointer Approach from Back
  - Time Complexity: O(m+n)
    - Each element is processed once as we iterate through both arrays.
  - Space Complexity: O(1)
    - No additional storage is used.
- Combine and Sort
  - Time Complexity: O((m+n)log(m+n))
    - Sorting the combined array dominates the complexity.
  - Space Complexity: O(m+n)
    - Additional storage is used for the combined array.

## Notes on Solving Process
- Two Pointer Approach from Back:
  - Efficient for large datasets as it avoids additional memory allocation and ensures linear runtime.
  - It requires careful pointer manipulation but achieves optimal performance.
- Combine and Sort:
  - Simpler to implement and easier to understand but less efficient due to sorting overhead and additional memory usage.
  - Suitable for small datasets or when simplicity is more important than efficiency.