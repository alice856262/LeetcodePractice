# Given an array of strings words, return the words that can be typed using 
# letters of the alphabet on only one row of American keyboard like the image below. 
# 
#  Note that the strings are case-insensitive, both lowercased and uppercased 
# of the same letter are treated as if they are at the same row. 
# 
#  In the American keyboard: 
# 
#  
#  the first row consists of the characters "qwertyuiop", 
#  the second row consists of the characters "asdfghjkl", and 
#  the third row consists of the characters "zxcvbnm". 
#  
#  
#  
#  Example 1: 
# 
#  
#  Input: words = ["Hello","Alaska","Dad","Peace"] 
#  
# 
#  Output: ["Alaska","Dad"] 
# 
#  Explanation: 
# 
#  Both "a" and "A" are in the 2nd row of the American keyboard due to case 
# insensitivity. 
# 
#  Example 2: 
# 
#  
#  Input: words = ["omk"] 
#  
# 
#  Output: [] 
# 
#  Example 3: 
# 
#  
#  Input: words = ["adsdf","sfd"] 
#  
# 
#  Output: ["adsdf","sfd"] 
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 20 
#  1 <= words[i].length <= 100 
#  words[i] consists of English letters (both lowercase and uppercase). 
#  
# 
#  Related Topics Array Hash Table String 👍 1682 👎 1149


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {1: 'qwertyuiop', 2: 'asdfghjkl', 3: 'zxcvbnm'}
        ans = []

        for word in words:
            isSameRow = True
            first = [key for key, val in keyboard.items() if word[0].lower() in val]
            for i in word:
                next = [key for key, val in keyboard.items() if i.lower() in val]
                if next != first:
                    isSameRow = False
            if isSameRow:
                ans.append(word)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
