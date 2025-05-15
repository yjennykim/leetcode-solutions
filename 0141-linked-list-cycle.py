# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head:
            if head.val == '$':
                return True
            
            head.val = '$'
            head = head.next
        
        return False