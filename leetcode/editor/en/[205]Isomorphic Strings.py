# Given two strings s and t, determine if they are isomorphic. 
# 
#  Two strings s and t are isomorphic if the characters in s can be replaced to 
# get t. 
# 
#  All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same 
# character, but a character may map to itself. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "egg", t = "add" 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  The strings s and t can be made identical by: 
# 
#  
#  Mapping 'e' to 'a'. 
#  Mapping 'g' to 'd'. 
#  
# 
#  Example 2: 
# 
#  
#  Input: s = "foo", t = "bar" 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  The strings s and t can not be made identical as 'o' needs to be mapped to 
# both 'a' and 'r'. 
# 
#  Example 3: 
# 
#  
#  Input: s = "paper", t = "title" 
#  
# 
#  Output: true 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  t.length == s.length 
#  s and t consist of any valid ascii character. 
#  
# 
#  Related Topics Hash Table String 👍 9452 👎 2165


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for s_char, t_char in zip(s, t):
            # Check if mapping already exists in s_dict
            if s_char in s_dict:
                if s_dict[s_char] != t_char:
                    return False
            else:
                s_dict[s_char] = t_char

            # Check if mapping already exists in t_dict
            if t_char in t_dict:
                if t_dict[t_char] != s_char:
                    return False
            else:
                t_dict[t_char] = s_char
        return True
# leetcode submit region end(Prohibit modification and deletion)
