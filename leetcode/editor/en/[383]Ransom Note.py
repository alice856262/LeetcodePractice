# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting 👍 5236 👎 520


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        dict = {}
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for j in ransomNote:
            if j not in dict or dict[j] <= 0:
                return False
            elif j in dict and dict[j] > 0:
                dict[j] -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
