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
        hm = {None: None}
        
        current = head
        while current:
            copy = Node(current.val)
            hm[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = hm[current]
            copy.next = hm[current.next]
            copy.random = hm[current.random]
            current = current.next
        return hm[head]