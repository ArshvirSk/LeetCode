# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0

        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10

            curr.next = ListNode(columnSum % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummyHead.next
        dummyHead.next = None
        return result