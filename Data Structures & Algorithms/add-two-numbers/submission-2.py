# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tmp = result
        offset = 0
        while l1 and l2:
            sum = l1.val + l2.val
            if sum > 9:
                # result.append(sum % 10 + offset)
                tmp.val = sum % 10 + offset
                offset = 1
            else:
                tmp.val = sum
                # result.append(sum)
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                tmp.next = ListNode()
                tmp = tmp.next
        
        while l1:
            if offset == 1:
                sum = l1.val + offset
                if sum > 9:
                    tmp.val = sum % 10
                    offset = 1
                else:
                    tmp.val = sum
                    offset = 0
            else:
                tmp.val = l1.val
            l1 = l1.next
            if l1:
                tmp.next = ListNode()
                tmp = tmp.next

        while l2:
            if offset == 1:
                sum = l2.val + offset
                if sum > 9:
                    tmp.val = sum % 10
                    offset = 1
                else:
                    tmp.val = sum
                    offset = 0
            else:
                tmp.val = l2.val
            l2 = l2.next
            if l2:
                tmp.next = ListNode()
                tmp = tmp.next

        if offset == 1:
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = 1

        return result
