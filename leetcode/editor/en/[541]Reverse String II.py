# Given a string s and an integer k, reverse the first k characters for every 2
# k characters counting from the start of the string. 
# 
#  If there are fewer than k characters left, reverse all of them. If there are 
# less than 2k but greater than or equal to k characters, then reverse the first 
# k characters and leave the other as original. 
# 
#  
#  Example 1: 
#  Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  
#  Example 2: 
#  Input: s = "abcd", k = 2
# Output: "bacd"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics Two Pointers String 👍 2095 👎 4024


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)  # Convert the string into a list for in-place modification

        # Process the string in blocks of 2k characters
        for i in range(0, len(s_list), 2 * k):
            # Reverse the first k characters in the current block
            # If there are fewer than k characters left, reverse all of them
            s_list[i:i + k] = s_list[i:i + k][::-1]

        return "".join(s_list)
# leetcode submit region end(Prohibit modification and deletion)
