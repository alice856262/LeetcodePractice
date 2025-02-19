## Algorithm Description
### Key Idea
- Reverse only the vowels in the string while leaving all other characters in their original positions.
- Two methods were implemented:
  - Two Pointer In-Place Swapping: Use the two-pointer technique on the string (after converting it to a list) to find and swap vowels in-place.
  - Collect and Rebuild: Extract all vowels from the string into a separate collection and then rebuild the string by replacing each vowel with the vowels from the extracted collection in reverse order.

### Step-by-Step Algorithm
#### Method 1: Two Pointer In-Place Swapping
- Step 1: Create a set of vowels for lookup.
- Step 2: Convert the input string to a list (```s_list```) to allow in-place modifications.
- Step 3: Initialize two pointers: ```left``` at the beginning of the list and ```right``` at the end.
- Step 4: While ```left``` is less than ```right```:
  - Increment the ```left``` pointer until it points to a vowel.
  - Decrement the ```right``` pointer until it points to a vowel.
  - Swap the vowels at the ```left``` and ```right``` positions, and move both pointers inward (increment ```left``` and decrement ```right```).
- Step 5: After the pointers meet or cross, join the list back into a string and return it.
#### Method 2: Collect and Rebuild
- Step 1: Define a list of vowels for lookup.
- Step 2: Iterate through the input string and collect every vowel encountered into a list (```s_vowel```).
- Step 3: Iterate through the input string **again**:
  - If the current character is a vowel, remove the last vowel from the ```s_vowel``` list (which gives the vowels in reverse order) and append it to ```ans```.
  - If the current character is not a vowel, append it unchanged to ```ans```.
- Step 4: Return the constructed string ```ans```.

## Algorithmic Complexity
- Two Pointer In-Place Swapping
  - Time Complexity: O(n)
    - Each character is inspected at most once as the two pointers converge.
  - Space Complexity: O(n)
    - The string is converted to a list to allow in-place modifications, which requires additional space proportional to the string length.
- Collect and Rebuild
  - Time Complexity: O(n)
    - **Two passes** over the string are performed (one to collect vowels and one to rebuild the string).
  - Space Complexity: O(n)
    - Extra space is used for the vowel collection (```s_vowel```) and for constructing the output string.

## Notes on Solving Process
- Two Pointer In-Place Swapping:
  - In-place swapping avoids the need for building the output string through concatenation, which is efficient and commonly used for similar in-place reversal problems.
  - Require converting the string to a list, which still uses O(n) space. Slightly more complex to understand due to pointer manipulation.
- Collect and Rebuild:
  - Conceptually straightforward: first isolate the vowels, then reconstruct the string.
  - Need to use two passes over the string, and building the output string using repeated concatenation can be inefficient in Python for very large strings.
- **Two Pointer In-Place Swapping** method is generally more efficient for large inputs compared to **Collect and Rebuild** method that requires two passes and repeated string concatenation.