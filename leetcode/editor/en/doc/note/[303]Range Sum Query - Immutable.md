## Algorithm Description
### Key Idea
- The goal is to efficiently compute the sum of a subarray given by indices ```left``` to ```right``` for multiple queries.
- Two methods were implemented:
  - Prefix Sum Approach: Use a **Prefix Sum Array** to precompute cumulative sums so that each query can be answered in constant time.
  - Iterative Summation Approach: Directly compute the sum by iterating over the specified subarray for each query.

### Step-by-Step Algorithm
#### Method 1: Prefix Sum Approach
- Step 1: Initialize a prefix sum array of size ```len(nums) + 1``` with all elements set to 0.
- Step 2: Iterate through the input array ```nums```:
  - For each index ```i``` from ```1``` to ```len(nums)```, compute ```prefix[i] = prefix[i - 1] + nums[i - 1]```.
- Step 3: For a query ```sumRange(left, right)```, compute the subarray sum as ```result = prefix[right + 1] - prefix[left]```.
- Step 4: Return the computed result.
#### Method 2: Iterative Summation Approach
- Step 1: Store the input array ```nums``` as is.
- Step 2: For a query ```sumRange(left, right)```, initialize a variable ```total``` to 0.
- Step 3: Iterate over the indices from ```left``` to ```right``` (inclusive):
  - Add each element ```nums[i]``` to ```total```.
- Step 4: Return the value of ```total```.

## Algorithmic Complexity
- Prefix Sum Approach
  - Time Complexity: O(n + m)
    - Preprocessing: O(n), where ```n``` is the length of ```nums```.
    - Each ```sumRange``` query: O(1) (constant time). For multiple ```sumRange``` calls (with m queries), the time complexity is O(m).
  - Space Complexity: O(n)
    - For the additional prefix sum array.
- Iterative Summation Approach
  - Time Complexity: O(n * m)
    - Each ```sumRange``` query: O(n) in the worst case (if the range covers the entire array). For multiple ```sumRange``` calls (with m queries), the time complexity is O(n * m).
  - Space Complexity: O(1)
    - The summation is computed on the fly without extra storage.

## Notes on Solving Process
- Prefix Sum Approach:
  - This method is more efficient for handling multiple queries because the heavy lifting is done during the initialization by precomputing the prefix sum array.
  - The trade-off is that it uses extra space (O(n)), but this is generally acceptable for improved query performance.
- Iterative Summation Approach:
  - This method is straightforward and simpler to implement, but it may lead to inefficient performance when there are many queries or when queries cover large subarrays.
  - It is suitable for scenarios with a small number of queries or small input arrays, where the simplicity outweighs the potential performance cost.