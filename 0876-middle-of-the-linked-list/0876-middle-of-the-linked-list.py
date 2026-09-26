# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        headC = head
        while headC.next != None:
            count+=1
            headC = headC.next
        
        for i in range(count//2):
            head = head.next

        return head