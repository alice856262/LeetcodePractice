## Algorithm Description
### Key Idea
- The algorithm uses binary search to efficiently narrow down the search space for the target number.
- It leverages the ```guess(num)``` API, which informs whether the current guess is too high, too low, or correct, to adjust the search boundaries.

### Step-by-Step Algorithm
- Step 1: Initialize two pointers: ```left``` is set to ```1``` and ```right``` is set to ```n```.
- Step 2: Enter a loop that continues while ```left``` is less than or equal to ```right```.
- Step 3: Compute the middle point ```mid = (left + right) // 2```.
- Step 4: Call the API ```guess(mid)``` and evaluate the result:
  - If ```guess(mid)``` returns ```-1```, update ```right``` to ```mid - 1``` (the target is lower than ```mid```).
  - If ```guess(mid)``` returns ```1```, update ```left``` to ```mid + 1``` (the target is higher than ```mid```).
  - If ```guess(mid)``` returns ```0```, return ```mid``` as it is the correct guess.

## Algorithmic Complexity
- Time Complexity: O(log n)
  - Each iteration halves the search space.
- Space Complexity: O(1)
  - Only a constant amount of extra space is used.

## Notes on Solving Process
- Binary search significantly reduces the number of guesses needed compared to a linear search, making it optimal for large values of ```n```.
- By adjusting the pointers appropriately with each API call, the algorithm guarantees that it will converge on the correct number.