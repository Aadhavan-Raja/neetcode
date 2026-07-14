# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxSoFar = root
        goodNodes = 0
        def dfs(root):
            nonlocal maxSoFar
            nonlocal goodNodes
            if not root:
                return 0
            if root.val >= maxSoFar:
                goodNodes += 1
            maxSoFar = max(maxSoFar, root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return goodNodes