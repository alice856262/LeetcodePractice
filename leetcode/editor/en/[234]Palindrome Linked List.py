# Given the head of a singly linked list, return true if it is a palindrome or 
# false otherwise. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,2,1]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 10⁵]. 
#  0 <= Node.val <= 9 
#  
# 
#  
# Follow up: Could you do it in 
# O(n) time and 
# O(1) space?
# 
#  Related Topics Linked List Two Pointers Stack Recursion 👍 17022 👎 916


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ### 1. Convert to Array
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums == nums[::-1]

    ### 2. Efficient Reverse and Compare
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     if not head or not head.next:
    #         return True
    #
    #     # Step 1: Find the middle
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #     # Step 2: Reverse the second half
    #     prev, curr = None, slow
    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #
    #     # Step 3: Compare the two halves
    #     first_half, second_half = head, prev
    #     while second_half:  # Only need to compare until the end of second_half
    #         if first_half.val != second_half.val:
    #             return False
    #         first_half = first_half.next
    #         second_half = second_half.next
    #     return True
# leetcode submit region end(Prohibit modification and deletion)
