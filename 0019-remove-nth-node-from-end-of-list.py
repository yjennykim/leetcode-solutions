# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        
        if len(arr) == n:
            return head.next
            
        to_remove = arr[len(arr) - n]
        prev = arr[len(arr) - n - 1]
        prev.next = to_remove.next
        to_remove = None

        return head