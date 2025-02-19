# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lowercase English letters. 
#  
# 
#  Related Topics String Trie 👍 18389 👎 4646


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]
        for s in strs[1:]:
            # Check the prefix against each string
            while not s.startswith(prefix):
                # Reduce the prefix by one character from the end
                prefix = prefix[:-1]
                # If prefix becomes empty, return ""
                if not prefix:
                    return ""
        return prefix
# leetcode submit region end(Prohibit modification and deletion)
