## Algorithm Description
### Key Idea
- The problem involves finding a single unique element in an array where every other element appears twice.
- Two methods were implemented:
  - Dictionary Approach: Use a hash map to count the occurrences of each number and identify the one with a count of 1.
  - Bit Manipulation (XOR) Approach: Leverage the XOR operation to cancel out paired numbers, leaving only the unique number.

### Step-by-Step Algorithm
#### Method 1: Dictionary Approach
- Step 1: Initialize an empty dictionary ```counts```.
- Step 2: Iterate through each number, and increment the count of the number in ```counts``` using ```counts.get(num, 0) + 1```.
- Step 3: Iterate through the dictionary to find the number with a count of 1.
#### Method 2: Bit Manipulation (XOR) Approach
- Step 1: Initialize a variable ```result``` to ```0```.
- Step 2: Iterate through each number, and update ```result``` with the XOR of ```result``` and the current number using ```result ^= num```.
- Step 3: After the loop, ```result``` will contain the single number because all paired numbers cancel out.

## Algorithmic Complexity
- Dictionary Approach
  - Time Complexity: O(n)
    - ```n``` is the length of the array, and populating the dictionary takes O(n).
  - Space Complexity: O(n)
    - The dictionary requires O(n) space to store counts.
- Bit Manipulation (XOR) Approach
  - Time Complexity: O(n)
    - Iterating through the array once takes O(n).
  - Space Complexity: O(1)
    - Only a single variable ```result``` is used.

## Notes on Solving Process
- Dictionary Approach:
  - Intuitive and easy to understand but requires extra space for the dictionary.
- Bit Manipulation (XOR) Approach:
  - Efficient in both time and space, leveraging the mathematical properties of XOR.