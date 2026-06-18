# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        for i in range(n-1):
            curr = curr.next
        if not curr.next:
            curr.next = None
        curr.next = curr.next.next

        return head