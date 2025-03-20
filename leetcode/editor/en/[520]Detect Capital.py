# We define the usage of capitals in a word to be right when one of the 
# following cases holds: 
# 
#  
#  All letters in this word are capitals, like "USA". 
#  All letters in this word are not capitals, like "leetcode". 
#  Only the first letter in this word is capital, like "Google". 
#  
# 
#  Given a string word, return true if the usage of capitals in it is right. 
# 
#  
#  Example 1: 
#  Input: word = "USA"
# Output: true
#  
#  Example 2: 
#  Input: word = "FlaG"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 100 
#  word consists of lowercase and uppercase English letters. 
#  
# 
#  Related Topics String 👍 3465 👎 464


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Manual Comparison
    def detectCapitalUse(self, word: str) -> bool:
        upper_word = word.upper()
        lower_word = word.lower()

        if word == upper_word or word == lower_word:
            return True

        if word[0] == upper_word[0]:
            for i in range(1, len(word)):
                if word[i] != lower_word[i]:
                    return False
            return True

        return False

    ### 2. Built-in String Method
    # def detectCapitalUse(self, word: str) -> bool:
    #     # Check if all letters are uppercase, all letters are lowercase, or only the first letter is uppercase (and the rest lowercase)
    #     return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
# leetcode submit region end(Prohibit modification and deletion)
