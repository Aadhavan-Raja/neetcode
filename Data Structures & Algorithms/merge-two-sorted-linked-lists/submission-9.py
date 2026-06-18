# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr1 = list1
        curr2 = list2
        curDum = dummy
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curDum.next = curr1
                curr1 = curr1.next
            else:
                curDum.next = curr2
                curr2 = curr2.next
            curDum = curDum.next
        if list1:
            currDum.next = list1
        elif list2:
            currDum.next = list2
        return dummy.next
