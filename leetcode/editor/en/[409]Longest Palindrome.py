# Given a string s which consists of lowercase or uppercase letters, return the 
# length of the longest palindrome that can be built with those letters. 
# 
#  Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose 
# length is 7.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 
# 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s consists of lowercase and/or uppercase English letters only. 
#  
# 
#  Related Topics Hash Table String Greedy 👍 6058 👎 423


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = {}
        ans = 0
        isOdd = False

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for key in s_dict:
            if s_dict[key] % 2 == 0:
                ans += s_dict[key]
            else:
                isOdd = True
                odd = (s_dict[key]) - 1
                ans += odd

        return ans + 1 if isOdd else ans
# leetcode submit region end(Prohibit modification and deletion)
