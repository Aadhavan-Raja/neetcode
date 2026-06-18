# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr1 = head
        curr2 = curr
        while curr1 and curr2:
            temp = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp
            curr1 = temp
            curr2 = temp2
        if temp2:
            curr1.next = temp2
        return head


    
