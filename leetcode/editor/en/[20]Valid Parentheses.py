# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "()" 
#  
# 
#  Output: true 
# 
#  Example 2: 
# 
#  
#  Input: s = "()[]{}" 
#  
# 
#  Output: true 
# 
#  Example 3: 
# 
#  
#  Input: s = "(]" 
#  
# 
#  Output: false 
# 
#  Example 4: 
# 
#  
#  Input: s = "([])" 
#  
# 
#  Output: true 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  Related Topics String Stack 👍 24861 👎 1833


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        # Define a dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop the top element from the stack if it exists; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the required opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched; otherwise, return False
        return not stack
# leetcode submit region end(Prohibit modification and deletion)
