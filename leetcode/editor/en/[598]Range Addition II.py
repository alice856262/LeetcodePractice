# You are given an m x n matrix M initialized with all 0's and an array of 
# operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one 
# for all 0 <= x < ai and 0 <= y < bi. 
# 
#  Count and return the number of maximum integers in the matrix after 
# performing all the operations. 
# 
#  
#  Example 1: 
#  
#  
# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So 
# return 4.
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2
# ,2],[3,3],[3,3],[3,3]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: m = 3, n = 3, ops = []
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 4 * 10⁴ 
#  0 <= ops.length <= 10⁴ 
#  ops[i].length == 2 
#  1 <= ai <= m 
#  1 <= bi <= n 
#  
# 
#  Related Topics Array Math 👍 977 👎 978


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        # Initialize a_min and b_min to m and n respectively
        a_min, b_min = m, n

        # Iterate through each operation
        for a, b in ops:
            a_min = min(a_min, a)
            b_min = min(b_min, b)

        # The number of maximum elements equals the area of the intersecting region
        return a_min * b_min
# leetcode submit region end(Prohibit modification and deletion)
