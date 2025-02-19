# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "anagram", t = "nagaram" 
#  
# 
#  Output: true 
# 
#  Example 2: 
# 
#  
#  Input: s = "rat", t = "car" 
#  
# 
#  Output: false 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 12628 👎 418


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Dictionary Approach
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}
        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1
        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1

        return dic_s == dic_t

    ### 2. Sorting Approach
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     return sorted(s) == sorted(t)
# leetcode submit region end(Prohibit modification and deletion)
