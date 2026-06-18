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
        while curr1 != None or curr2 != None:
            if curr2 == None:
                curDum.next = curr1
                curr1 = curr1.next
            elif curr1 == None:
                curDum.next = curr2
                curr2 = curr2.next
            if curr1.val > curr2.val:
                curDum.next = curr1
                curr1 = curr1.next
            else:
                curDum.next = curr2
                curr2 = curr2.next
            curDum = curDum.next
        return dummy
