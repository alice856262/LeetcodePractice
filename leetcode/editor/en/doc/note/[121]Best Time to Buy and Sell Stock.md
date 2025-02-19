## Algorithm Description
### Key Idea
- Use a single pass through the ```prices``` array to find the maximum profit.
- Keep track of the minimum price encountered so far to calculate potential profits efficiently.
- Continuously update the maximum profit when a higher profit is found.

### Step-by-Step Algorithm
- Step 1: Initialize ```min_price``` to a very large value (infinity) and ```max_profit``` to 0.
- Step 2: Iterate over the ```prices``` array:
  - Update ```min_price``` if the current price is lower than the previously recorded minimum price.
  - Calculate the profit by subtracting ```min_price``` from the current price.
  - Update ```max_profit``` if the calculated profit is greater than the current ```max_profit```.
- Step 3: After the loop, return the ```max_profit``` value.

## Algorithmic Complexity
- Time Complexity: O(n)
  - ```n``` is the number of elements in the ```prices``` array. The algorithm involves a single pass through the array.
- Space Complexity: O(1)
  - Only two variables, ```min_price``` and ```max_profit```, are used, requiring constant space.

### Notes on Solving Process
- This approach avoids the inefficiency of nested loops in the brute force method (O(n^2)).
- By calculating potential profits during the same loop, the algorithm ensures both time and space efficiency.
- It leverages the property that the maximum profit can be determined by maintaining a running minimum price and comparing profits dynamically.