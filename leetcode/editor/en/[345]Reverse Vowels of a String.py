# Given a string s, reverse only all the vowels in the string and return it. 
# 
#  The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
# lower and upper cases, more than once. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "IceCreAm" 
#  
# 
#  Output: "AceCreIm" 
# 
#  Explanation: 
# 
#  The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes 
# "AceCreIm". 
# 
#  Example 2: 
# 
#  
#  Input: s = "leetcode" 
#  
# 
#  Output: "leotcede" 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s consist of printable ASCII characters. 
#  
# 
#  Related Topics Two Pointers String 👍 4838 👎 2822


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Two Pointer In-Place Swapping
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s_list) - 1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)

    ### 2. Collect and Rebuild
    # def reverseVowels(self, s: str) -> str:
    #     vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #     s_vowel = []
    #     ans = ''
    #
    #     for i in range(len(s)):
    #         if s[i] in vowel:
    #             s_vowel.append(s[i])
    #
    #     for i in range(len(s)):
    #         if s[i] in vowel:
    #             last_vowel = s_vowel.pop(-1)
    #             ans += last_vowel
    #         else:
    #             ans += s[i]
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
