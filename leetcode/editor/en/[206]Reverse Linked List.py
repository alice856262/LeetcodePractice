# Given the head of a singly linked list, reverse the list, and return the 
# reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. 
# Could you implement both? 
# 
#  Related Topics Linked List Recursion 👍 22327 👎 486


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ### 1. Recursive Method
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head

        # Reverse the rest of the list
        new_head = self.reverseList(head.next)
        # Reverse the pointer of the next node
        head.next.next = head
        head.next = None

        return new_head

    ### 2. Iterative Method
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     current = head
    #
    #     while current:
    #         next_node = current.next  # Store next node
    #         current.next = prev  # Reverse current node's pointer
    #         prev = current  # Move prev to current node
    #         current = next_node  # Move to next node
    #
    #     return prev
# leetcode submit region end(Prohibit modification and deletion)
