# Given a string s consisting of words and spaces, return the length of the 
# last word in the string. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only English letters and spaces ' '. 
#  There will be at least one word in s. 
#  
# 
#  Related Topics String 👍 5469 👎 303


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Built-in Function
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])

    ### 2. Manual Traversal
    # def lengthOfLastWord(self, s: str) -> int:
    #     blank = 0
    #     for i in range(len(s), 0, -1):
    #         j = i - 1
    #         if s[j] != ' ':
    #             break
    #         else:
    #             blank += 1
    #     new_s = s[:-blank]
    #
    #     count = 0
    #     for i in range(len(new_s), 0, -1):
    #         j = i - 1
    #         if new_s[j] != ' ':
    #             count += 1
    #         else:
    #             break
    #     return count
# leetcode submit region end(Prohibit modification and deletion)
