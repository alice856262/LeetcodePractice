# Given an integer rowIndex, return the rowIndexᵗʰ (0-indexed) row of the 
# Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
#  Follow up: Could you optimize your algorithm to use only O(rowIndex) extra 
# space? 
# 
#  Related Topics Array Dynamic Programming 👍 4952 👎 354


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the first row
        row = [1]

        for i in range(1, rowIndex + 1):
            # Update the row in reverse to avoid overwriting
            row.append(1)  # Add a placeholder for the last element

            # Compute the inner values of the row (if applicable)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row
# leetcode submit region end(Prohibit modification and deletion)
