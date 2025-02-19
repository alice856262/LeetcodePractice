# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
# 
#  Related Topics Two Pointers String String Matching 👍 6299 👎 464


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Manual Sliding Window Comparison
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0  # An empty needle is always found at index 0
        for i in range(n - m + 1):  # Iterate only where `needle` can fit
            if haystack[i:i + m] == needle:  # Check if substring matches `needle`
                return i
        return -1  # No match found

    ### 2. Built-in Function
    # def strStr(self, haystack: str, needle: str) -> int:
    #     return haystack.find(needle)
# leetcode submit region end(Prohibit modification and deletion)
