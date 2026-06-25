# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(root):
            if root and root:
                temp = root.right
                root.right = root.left
                root.left = root.right
            if root.right and root.left:
                reverse(root.right)
                reverse(root.left)
        reverse(root)
        
        
