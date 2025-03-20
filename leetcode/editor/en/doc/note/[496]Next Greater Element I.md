## Algorithm Description
### Key Idea
- For each element in ```nums1``` (which is a subset of ```nums2```), determine its next greater element in ```nums2``` and return an array with these values.
- Two methods were implemented:
  - Monotonic Stack Approach: Use a monotonic decreasing stack to process ```nums2``` in one pass, mapping each element to its next greater element.
  - Brute-Force Nested Loops: For each element in ```nums2```, scan the elements to its right until the first greater element is found and build a mapping accordingly.

### Step-by-Step Algorithm
#### Method 1: Monotonic Stack Approach
- Step 1: Initialize an empty dictionary (```mapping```) to store the next greater element for each number in ```nums2```, and an empty stack.
- Step 2: Iterate over each element in ```nums2```:
  - While the stack is not empty and the current element is greater than the element at the top of the stack, pop the stack and set its next greater element in ```mapping``` to the current element.
  - Push the current element onto the stack.
- Step 3: After the iteration, assign ```-1``` as the next greater element for any remaining elements in the stack.
- Step 4: For each element in ```nums1```, use the ```mapping``` to get its next greater element and form the result array.
#### Method 2: Brute-Force Nested Loops
- Step 1: Initialize an empty dictionary (```dict2```) to store the next greater element for each number in ```nums2```.
- Step 2: For each index ```i``` in ```nums2```:
  - Set the default next greater element for ```nums2[i]``` to ```-1```.
  - Iterate from index ```i + 1``` to the end of ```nums2```.
  - If a number greater than ```nums2[i]``` is found, update the dictionary with that number as the next greater element and **break the inner loop**.
- Step 3: For each element in ```nums1```, use the ```dict2``` to get its next greater element and form the result array.

## Algorithmic Complexity
- Monotonic Stack Approach
  - Time Complexity: O(n + m)
    - Processing all ```n``` elements in ```nums2``` to build the mapping takes O(n), and then constructing the result for ```m``` elements in ```nums1``` takes O(m).
  - Space Complexity: O(n + m)
    - The mapping and stack require O(n) space, and the result array requires O(m) space.
- Brute-Force Nested Loops
  - Time Complexity: O(n² + m)
    - Worst case: for each of the ```n``` elements in ```nums2```, a scan of the remaining elements takes O(n) time, leading to O(n²). Constructing the result for ```m``` elements adds an additional O(m).
  - Space Complexity: O(n + m)
    - The dictionary stores up to ```n``` elements, and the result array uses O(m) space.

## Notes on Solving Process
- Monotonic Stack Approach:
  - This approach leverages a monotonic stack to efficiently compute the next greater element in one pass. It is well-suited for larger arrays since it avoids nested iterations.
  - The use of a dictionary allows constant-time lookups when building the final result for ```nums1```.
- Brute-Force Nested Loops:
  - The brute-force approach is straightforward and easier to understand but suffers from poor performance on larger inputs due to its nested loop structure.
  - While simpler, it is not optimal in terms of time complexity compared to the stack-based method.