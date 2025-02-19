# Write a function that reverses a string. The input string is given as an 
# array of characters s. 
# 
#  You must do this by modifying the input array in-place with O(1) extra 
# memory. 
# 
#  
#  Example 1: 
#  Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  
#  Example 2: 
#  Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is a printable ascii character. 
#  
# 
#  Related Topics Two Pointers String 👍 8877 👎 1187


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1
# leetcode submit region end(Prohibit modification and deletion)
