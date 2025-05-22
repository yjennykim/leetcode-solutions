"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Pass 1: Create copies of nodes
        # Loop
        mapping = {}
        temp = head
        # Create copy of iterating node
        while temp:
            # Assign original iterating node to its copy
            mapping[temp] = Node(temp.val, None, None)

            # Set to next node
            temp = temp.next

        # Pass 2: Assign pointers
        # Loop

        # Create iterator for both original LL and copied LL
        orig, copied = head, mapping[head]
        while orig:
            if orig.next:
                copied.next = mapping[orig.next]
            
            if orig.random:
                copied.random = mapping[orig.random]
            copied = copied.next
            orig = orig.next

        return mapping[head]
         