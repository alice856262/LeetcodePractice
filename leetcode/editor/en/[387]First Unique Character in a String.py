# Given a string s, find the first non-repeating character in it and return its 
# index. If it does not exist, return -1. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "leetcode" 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  The character 'l' at index 0 is the first character that does not occur at 
# any other index. 
# 
#  Example 2: 
# 
#  
#  Input: s = "loveleetcode" 
#  
# 
#  Output: 2 
# 
#  Example 3: 
# 
#  
#  Input: s = "aabb" 
#  
# 
#  Output: -1 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Queue Counting 👍 9172 👎 311


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
        return -1
# leetcode submit region end(Prohibit modification and deletion)
