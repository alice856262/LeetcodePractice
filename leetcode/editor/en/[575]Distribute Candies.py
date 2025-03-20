# Alice has n candies, where the iᵗʰ candy is of type candyType[i]. Alice 
# noticed that she started to gain weight, so she visited a doctor. 
# 
#  The doctor advised Alice to only eat n / 2 of the candies she has (n is 
# always even). Alice likes her candies very much, and she wants to eat the maximum 
# number of different types of candies while still following the doctor's advice. 
# 
#  Given the integer array candyType of length n, return the maximum number of 
# different types of candies she can eat if she only eats n / 2 of them. 
# 
#  
#  Example 1: 
# 
#  
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 
# types, she can eat one of each type.
#  
# 
#  Example 2: 
# 
#  
# Input: candyType = [1,1,2,3]
# Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2
# ], [1,3], or [2,3], she still can only eat 2 different types.
#  
# 
#  Example 3: 
# 
#  
# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 
# candies, she only has 1 type.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == candyType.length 
#  2 <= n <= 10⁴ 
#  n is even. 
#  -10⁵ <= candyType[i] <= 10⁵ 
#  
# 
#  Related Topics Array Hash Table 👍 1602 👎 1407


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Set Method
    def distributeCandies(self, candyType: List[int]) -> int:
        # Count the number of distinct candy types
        distinct_types = len(set(candyType))
        max_candies = len(candyType) // 2
        # The maximum number of different types is the minimum of distinct_types and max_candies
        return min(distinct_types, max_candies)

    ### 2. Dictionary Method
    # def distributeCandies(self, candyType: List[int]) -> int:
    #     candy_dict = {}
    #     max_candies = len(candyType) // 2
    #
    #     for candy in candyType:
    #         if candy not in candy_dict:
    #             candy_dict[candy] = 1
    #         else:
    #             candy_dict[candy] += 1
    #
    #     return max_candies if len(candy_dict) >= max_candies else len(candy_dict)
# leetcode submit region end(Prohibit modification and deletion)
