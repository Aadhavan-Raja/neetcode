"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        curr = head
        newHead = Node(curr.val, curr.next, curr.random)
        newCurr = newHead
        while curr:
            newCurr.next = Node(curr.next.val, curr.next.next, curr.next.random)
            newCurr = newCurr.next
            curr = curr.next
        return newHead

        