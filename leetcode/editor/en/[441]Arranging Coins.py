# You have n coins and you want to build a staircase with these coins. The 
# staircase consists of k rows where the iᵗʰ row has exactly i coins. The last row of 
# the staircase may be incomplete. 
# 
#  Given the integer n, return the number of complete rows of the staircase you 
# will build. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 5
# Output: 2
# Explanation: Because the 3ʳᵈ row is incomplete, we return 2.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 8
# Output: 3
# Explanation: Because the 4ᵗʰ row is incomplete, we return 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics Math Binary Search 👍 4033 👎 1348


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Binary Search Approach
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid

        return ans

    ### 2. Mathematical (Quadratic Formula) Approach
    # def arrangeCoins(self, n: int) -> int:
    #     # The total number of coins needed to form k complete rows is given by Gauss's formula: S = k * (k + 1) / 2.
    #     # We need to find the maximum integer k such that: k * (k + 1) / 2 <= n
    #
    #     # Solve the equation:
    #     # --> k * (k + 1) / 2 <= n --> k * (k + 1) <= 2 * n --> k^2 + k - 2n <= 0
    #     # Using the quadratic formula for a quadratic equation ax^2 + bx + c = 0:
    #     # --> k = (-b ± sqrt(b^2 - 4ac)) / (2a)
    #     # Here, a = 1, b = 1, and c = -2 * n.
    #     # --> k = (-1 ± sqrt(1 + 8*n)) / 2
    #
    #     # Since k must be non-negative, we take the positive root:
    #     k = (-1 + math.sqrt(1 + 8 * n)) / 2
    #
    #     # We need the maximum complete number of rows, so take the floor of k
    #     return int(k)

    ### 3. Simulation Approach
    # def arrangeCoins(self, n: int) -> int:
    #     row = 0
    #     count = 0
    #
    #     while count < n:
    #         row += 1
    #         count += row
    #
    #     return row if count == n else row - 1
# leetcode submit region end(Prohibit modification and deletion)
