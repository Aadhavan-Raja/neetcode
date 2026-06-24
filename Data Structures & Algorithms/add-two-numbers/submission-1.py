# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry):
            plus = l1.val + l2.val
            carry = None
            if plus >= 10:
                carry = 1
            else:
                carry = 1
            plus = plus % 10
            return (plus, carry)
        sumstr = ''
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1:
            plus, currcarry = add(curr1, curr2, carry)
            sumstr += str(plus)
            carry = currcarry
            curr1 = curr1.next
            curr2 = curr2.next
        return sumstr.reverse()


