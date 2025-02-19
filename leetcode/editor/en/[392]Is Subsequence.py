# Given two strings s and t, return true if s is a subsequence of t, or false 
# otherwise. 
# 
#  A subsequence of a string is a new string that is formed from the original 
# string by deleting some (can be none) of the characters without disturbing the 
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
# "abcde" while "aec" is not). 
# 
#  
#  Example 1: 
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#  
#  Example 2: 
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10⁴ 
#  s and t consist only of lowercase English letters. 
#  
# 
#  
# Follow up: Suppose there are lots of incoming 
# s, say 
# s1, s2, ..., sk where 
# k >= 10⁹, and you want to check one by one to see if 
# t has its subsequence. In this scenario, how would you change your code?
# 
#  Related Topics Two Pointers String Dynamic Programming 👍 10055 👎 570


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Two Pointer Approach
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        s_pointer, t_pointer = 0, 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == len(s)

    ### 2. Preprocessing with Binary Search --> for follow up question
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     t_dict = defaultdict(list)
    #     for i, symbol in enumerate(t):
    #         t_dict[symbol].append(i)
    #
    #     current = 0
    #     for symbol in s:
    #         index = bisect.bisect_left(t_dict[symbol], current)
    #         if index >= len(t_dict[symbol]):
    #             return False
    #         current = t_dict[symbol][index] + 1
    #
    #     return True
# leetcode submit region end(Prohibit modification and deletion)
