# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots. 
# 
#  Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be 
# planted in the flowerbed without violating the no-adjacent-flowers rule and false 
# otherwise. 
# 
#  
#  Example 1: 
#  Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#  
#  Example 2: 
#  Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= flowerbed.length <= 2 * 10⁴ 
#  flowerbed[i] is 0 or 1. 
#  There are no two adjacent flowers in flowerbed. 
#  0 <= n <= flowerbed.length 
#  
# 
#  Related Topics Array Greedy 👍 6920 👎 1255


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if the left neighbor is empty or this is the first plot
                left_neighbor_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right neighbor is empty or this is the last plot
                right_neighbor_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both neighbors are empty, it's safe to plant a flower here
                if left_neighbor_empty and right_neighbor_empty:
                    flowerbed[i] = 1  # Plant the flower
                    n -= 1
                    # If we've planted all required flowers, return True
                    if n == 0:
                        return True

        # If we finish checking and haven't planted n flowers, return False
        return n <= 0
# leetcode submit region end(Prohibit modification and deletion)
