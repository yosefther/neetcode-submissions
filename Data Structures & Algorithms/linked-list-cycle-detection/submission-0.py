# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        index = 0 
        while head != None : 
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False 