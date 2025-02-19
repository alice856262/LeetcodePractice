# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric 
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s consists only of printable ASCII characters. 
#  
# 
#  Related Topics Two Pointers String 👍 9899 👎 8480


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Regular Expression and String Manipulation
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Check if the cleaned string reads the same forwards and backwards
        return cleaned == cleaned[::-1]

    ### 2. Character Filtering and Reverse Construction
    # def isPalindrome(self, s: str) -> bool:
    #     # Use only alphanumeric characters and ignore cases
    #     alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
    #     lower_s = s.lower()
    #     forward_s = ""
    #     backward_s = ""
    #
    #     for i in lower_s:
    #         if i in alphanumeric:
    #             forward_s += i
    #
    #     for i in range(len(forward_s) - 1, -1, -1):
    #         backward_s += forward_s[i]
    #
    #     # Compare the string with its reverse
    #     return forward_s == backward_s
# leetcode submit region end(Prohibit modification and deletion)
