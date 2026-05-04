# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        he = ListNode(0, head)
        first, second = head, he
        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        # Second is just before node to be removed
        second.next = second.next.next
        return he.next