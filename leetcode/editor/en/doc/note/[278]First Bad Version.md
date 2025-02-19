## Algorithm Description
### Key Idea
- Use **binary search** to efficiently find the first bad version. Binary search works by repeatedly halving the search space.
- By checking whether a version is bad using the ```isBadVersion``` API, determine if the first bad version lies in the left or right half of the current search range.

### Step-by-Step Algorithm
- Step 1: Initialize two pointers, ```left``` and ```right```, to define the search range:
  - ```left = 1``` (first version).
  - ```right = n``` (last version).
- Step 2: While ```left <= right```, calculate the middle version: ```mid = (left + right) // 2```.
- Step 3: Check if ```mid``` is a bad version using the ```isBadVersion``` API:
  - If ```isBadVersion(mid)``` is ```True```, the first bad version is at or before ```mid```, so update ```right = mid - 1```.
  - Otherwise, the first bad version is after ```mid```, so update ```left = mid + 1```.
- Step 4: Exit the loop when ```left > right```. The ```left``` pointer will point to the first bad version.

## Algorithmic Complexity
- Time Complexity: O(log n)
  - Binary search divides the search space in half with each iteration.
  - The number of API calls is proportional to the depth of the binary search.
- Space Complexity: O(1)
  - Use only a constant amount of extra space for the pointers (```left```, ```right```, and ```mid```).

## Notes on Solving Process
- The binary search approach minimizes the number of API calls to ```isBadVersion```, making it efficient.
- The choice of updating ```right = mid - 1``` ensures that the search narrows down correctly without skipping the potential first bad version.
- The loop exits when ```left > right```, ensuring that ```left``` directly points to the first bad version, whereas ```mid``` might not be updated to the correct position in the final iteration.