# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdep = 0
        def depth(root, dep):
            nonlocal maxdep
            if not root:
                return
            dep += 1
            maxdep = max(maxdep, dep)
            depth(root.left, dep)
            depth(root.right, dep)
        depth(root, 0)
        return maxdep