# You are given the heads of two sorted linked lists list1 and list2. 
# 
#  Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes of the first two lists. 
# 
#  Return the head of the merged linked list. 
# 
#  
#  Example 1: 
#  
#  
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = [], list2 = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both lists is in the range [0, 50]. 
#  -100 <= Node.val <= 100 
#  Both list1 and list2 are sorted in non-decreasing order. 
#  
# 
#  Related Topics Linked List Recursion 👍 22523 👎 2203


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ### 1. Iterative Merge
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy  # Pointer to the last node in the merged list

        # Traverse both lists until one becomes empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Attach list1's current node
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Attach list2's current node
                list2 = list2.next  # Move to the next node in list2
            current = current.next  # Advance the pointer in the merged list
        # Attach the remaining nodes of the non-empty list
        current.next = list1 if list1 else list2

        return dummy.next  # Return the merged list, skipping the dummy node

    ### 2. Sorting-based Merge
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     # Extract all node values into a list
    #     values = []
    #     while list1:
    #         values.append(list1.val)
    #         list1 = list1.next
    #     while list2:
    #         values.append(list2.val)
    #         list2 = list2.next
    #
    #     # Sort the values
    #     values.sort()
    #
    #     # Create a new linked list from the sorted values
    #     dummy = ListNode()
    #     current = dummy
    #     for val in values:
    #         current.next = ListNode(val)
    #         current = current.next
    #     return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
