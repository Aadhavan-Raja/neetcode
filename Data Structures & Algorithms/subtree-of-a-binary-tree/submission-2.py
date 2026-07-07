# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        hasSubRoot = False
        def sameTree(rootP, rootQ):
            if not rootP and not rootQ:
                return True
            if not rootP or not rootQ:
                return False
            if rootP.val != rootQ.val:
                return False
            return sameTree(rootP.left, rootQ.left) and sameTree(rootP.right, rootQ.right)    

        def dfs(root):
            nonlocal hasSubRoot
            if not root:
                return None
            
            right = dfs(root.right)
            left = dfs(root.left)
            if sameTree(root, subRoot):
                hasSubRoot = True
        
        dfs(root)
        return hasSubRoot
        

            

    
