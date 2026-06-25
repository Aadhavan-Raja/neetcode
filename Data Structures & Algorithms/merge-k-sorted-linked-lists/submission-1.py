# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = ListNode()
        curH = newHead
        currNodes = []
        for head in lists:
            if head:
                currNode.append(head)
        while currNodes:
            nextNodes = []  
            smallest = currNodes[0]
            for node in currNodes:
                if node.val < smallest.val:
                    smallest = node
                if node.next:
                    nextNodes.append(node.next)
            currNodes = nextNodes
            curH.next = smallest
            curH = curH.next
        return newHead.next
            

