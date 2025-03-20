# In MATLAB, there is a handy function called reshape which can reshape an m x 
# n matrix into a new one with a different size r x c keeping its original data. 
# 
#  You are given an m x n matrix mat and two integers r and c representing the 
# number of rows and the number of columns of the wanted reshaped matrix. 
# 
#  The reshaped matrix should be filled with all the elements of the original 
# matrix in the same row-traversing order as they were. 
# 
#  If the reshape operation with given parameters is possible and legal, output 
# the new reshaped matrix; Otherwise, output the original matrix. 
# 
#  
#  Example 1: 
#  
#  
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#  
# 
#  Example 2: 
#  
#  
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 100 
#  -1000 <= mat[i][j] <= 1000 
#  1 <= r, c <= 300 
#  
# 
#  Related Topics Array Matrix Simulation 👍 3586 👎 424


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. List Comprehension and Slicing Approach
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        # Flatten the matrix while preserving row-traversing order
        flat = [num for row in mat for num in row]

        # Build the new reshaped matrix by slicing the flattened list
        return [flat[i * c:(i + 1) * c] for i in range(r)]

    ### 2. Nested Loops with Index Approach
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     temp = []
    #     for i in mat:
    #         for j in i:
    #             temp.append(j)
    #
    #     if len(temp) != r * c:
    #         return mat
    #
    #     ans = []
    #     index = 0  # This index tracks the current position in the flattened list
    #     for i in range(r):
    #         row = []
    #         for j in range(c):
    #             row.append(temp[index])
    #             index += 1  # Move to the next element for the next cell
    #         ans.append(row)
    #
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
