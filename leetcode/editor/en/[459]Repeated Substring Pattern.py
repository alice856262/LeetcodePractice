# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" 
# twice.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics String String Matching 👍 6552 👎 540


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s in (s + s)[1:-1]:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
