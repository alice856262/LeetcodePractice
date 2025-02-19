## Algorithm Description
### Key Idea
- Maximize the number of content children by assigning cookies such that each child gets at most one cookie, and a child is content if the cookie's size is at least the child's greed factor.
- The approach is to sort both the greed factors (g) and the cookie sizes (s). Then, use a **two-pointer greedy technique** to match each child with the smallest available cookie that satisfies their greed.

### Step-by-Step Algorithm
- Step 1: Sort the array ```g``` (children's greed factors) and ```s``` (cookie sizes) in ascending order.
- Step 2: Initialize two pointers:
  - ```child = 0``` (to track the current child in ```g```)
  - ```cookie = 0``` (to track the current cookie in ```s```)
- Step 3: Iterate with a loop while both pointers are within the bounds of their arrays:
  - If the current cookie ```s[cookie]``` is greater than or equal to the current child's greed factor ```g[child]```, increment ```child``` (i.e., assign the cookie to the child).
  - In every iteration, increment the ```cookie``` pointer to consider the next cookie.
- Step 4: When the loop terminates, the pointer ```child``` represents the number of content children. Return this value.

## Algorithmic Complexity
- Time Complexity: O(n log n + m log m)
  - Sorting ```g``` takes O(n log n) and sorting ```s``` takes O(m log m), where ```n``` is the length of ```g``` and ```m``` is the length of ```s```.
  - The two-pointer iteration takes O(n + m).
  - For large inputs, the linear term O(n + m) is dominated by the O(n log n + m log m) sorting operations, so the overall time complexity simplifies to O(n log n + m log m).
- Space Complexity: O(1)
  - Take O(1) extra space if sorting is done in place.

## Notes on Solving Process
- By sorting both arrays, we can ensure that each child is given the smallest available cookie that meets their greed, which maximizes the total number of satisfied children.
- The use of two pointers allows us to efficiently traverse both arrays without additional data structures.
- Edge Handling: If a cookie is too small for the current child, we simply move to the next cookie, ensuring no cookie is wasted and maximizing the number of content children.