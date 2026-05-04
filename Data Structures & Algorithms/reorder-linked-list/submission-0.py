# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        # Reverse second half (l1)
        reverse = l1.next
        previous = l1.next = None
        while reverse:
            tmp = reverse.next
            reverse.next = previous
            previous = reverse
            reverse = tmp

        reverse = previous
        first = head
        while reverse:
            tmp1, tmp2 = first.next, reverse.next
            first.next = reverse
            reverse.next = tmp1
            first, reverse = tmp1, tmp2
