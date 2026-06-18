# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr2 = slow.next
        slow.next = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        curr2 = prev
        curr1 = head
        while curr1 and curr2:
            temp = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp
            curr1 = temp
            curr2 = temp2
        return head


    
