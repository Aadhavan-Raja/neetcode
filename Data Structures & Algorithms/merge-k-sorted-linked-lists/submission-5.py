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
                currNodes.append(head)
        while currNodes:
            smallest = currNodes[0]
            smallInd = 0
            for i in range(len(currNodes)):
                if currNodes[i].val < smallest.val:
                    smallest = currNodes[i]
                    smallInd = i
            if currNodes[smallInd]:
                currNodes[smallInd] = currNodes[smallInd].next
            else:
                currNodes.pop(smallInd)
            curH.next = smallest
            curH = curH.next
        return newHead.next
            

