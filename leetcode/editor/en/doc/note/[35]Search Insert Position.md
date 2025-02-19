## Algorithm Description
### Key Idea
- Utilize the **binary search** algorithm to achieve O(log n) runtime complexity by repeatedly dividing the search range in half.
- Leverage the properties of a sorted array to determine whether the target is in the left or right half of the current range.

### Step-by-Step Algorithm
- Step 1: Set two pointers: ```left``` to the start of the array (```0```) and ```right``` to the end of the array (```len(nums) - 1```).
- Step 2: Iterate until the search space is exhausted:
  - Calculate the middle index.
  - Compare ```nums[mid]``` with the ```target```:
    - If ```nums[mid]``` == ```target```, return ```mid``` (target found).
    - If ```nums[mid]``` < ```target```, move the ```left``` pointer to ```mid + 1``` (search in the right half).
    - If ```nums[mid]``` > ```target```, move the ```right``` pointer to ```mid - 1``` (search in the left half).
- Step 3: Return insertion index:
  - If the target is not found, the ```left``` pointer will point to the position where the target should be inserted to maintain sorted order.

## Algorithmic Complexity
- Time Complexity: O(log n)
  - The search range is halved with each iteration.
- Space Complexity: O(1)
  - No additional data structures are used; only pointers are maintained.

## Notes on Solving Process
- Midpoint Calculation:
  - The formula ```(left + right) // 2``` is common but could cause overflow in some languages with fixed-size integers. In Python, this isn't an issue since integers can grow arbitrarily large.
- Returning ```left```:
  - If the target isn’t found, the ```left``` pointer represents the smallest index where the target could be inserted while preserving the sorted order. This simplifies the handling of edge cases.