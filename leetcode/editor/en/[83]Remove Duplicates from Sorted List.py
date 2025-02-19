# Given the head of a sorted linked list, delete all duplicates such that each 
# element appears only once. Return the linked list sorted as well. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,1,2]
# Output: [1,2]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 300]. 
#  -100 <= Node.val <= 100 
#  The list is guaranteed to be sorted in ascending order. 
#  
# 
#  Related Topics Linked List 👍 8975 👎 324


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # If the list is empty, return None
            return head

        current = head  # Start from the head of the list
        while current and current.next:  # Traverse until the end of the list
            if current.val == current.next.val:  # Check for duplicate
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node if no duplicate
        return head
# leetcode submit region end(Prohibit modification and deletion)
