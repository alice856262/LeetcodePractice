## Algorithm Description
### Key Idea
- Find all common strings between two lists that have the smallest index sum, where the index sum for a common string is the sum of its indices in ```list1``` and ```list2```.
- Two methods were implemented:
  - Dictionary Lookup Approach: Build a dictionary from ```list1``` mapping each string to its index, then iterate over ```list2``` to compute the index sum for each common string. Keep track of the minimum index sum and store the corresponding common strings.
  - Nested Loop Approach: Use nested loops to compare every string in ```list1``` with every string in ```list2```. For each match, compute the index sum and store it in a dictionary. Then, determine the minimum index sum from the dictionary and return all keys that have that sum.

### Step-by-Step Algorithm
#### Method 1: Dictionary Lookup Approach
- Step 1: Create a dictionary (```index_map```) from ```list1``` where each string is mapped to its index.
- Step 2: Initialize ```min_sum``` to infinity and an empty list ```result``` to store the common strings with the minimum index sum.
- Step 3: Iterate over ```list2``` with index ```j```. For each string:
  - Check if the string exists in ```index_map``` (i.e., it is common to both lists).
  - Compute the index sum as ```index_map[s] + j```.
  - If index sum is less than ```min_sum```, update ```min_sum``` and reset ```result``` to contain this string.
  - If the index sum equals ```min_sum```, append the string to ```result```.
- Step 4: Return ```result```.
#### Method 2: Nested Loop Approach
- Step 1: Initialize an empty dictionary (```common```) to store common strings and their index sums.
- Step 2: Use nested loops, iterate index ```i``` in ```list1``` and index ```j``` in ```list2```.
  - If ```list1[i] == list2[j]```, store the pair in ```common``` with key ```list1[i]``` and value ```i + j```.
- Step 3: Initialize ```min_sum``` to infinity and iterate through the dictionary to find the minimum index sum.
- Step 4: Iterate over the dictionary items and collect all keys whose associated index sum equals ```min_sum```.

## Algorithmic Complexity
- Dictionary Lookup Approach
  - Time Complexity: O(n + m)
    - ```n``` and ```m``` is the length of ```list1``` and ```list2```. Building the dictionary takes O(n) and iterating over ```list2``` takes O(m).
  - Space Complexity: O(n)
    - The dictionary stores each element from ```list1```, which takes up to O(n) space.
- Nested Loop Approach
  - Time Complexity: O(n * m)
    - Every element in ```list1``` is compared with every element in ```list2``` using nested loops.
  - Space Complexity: O(k)
    - The dictionary stores ```k``` common strings.
    - Worst case: O(k) could be O(n) if every element is common.

## Notes on Solving Process
- Dictionary Lookup Approach:
  - Use efficient dictionary lookups to reduce the number of comparisons.
  - This approach is more concise and suitable for larger input sizes due to its linear time complexity.
- Nested Loop Approach:
  - This is a brute-force approach using nested loops to explicitly compare each pair from ```list1``` and ```list2```, which is less efficient due to the quadratic time complexity.
  - May be acceptable for smaller input sizes but is not scalable for larger lists.