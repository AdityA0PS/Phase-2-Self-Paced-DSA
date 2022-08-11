# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.res = float("-inf")
        def path(root,res):
            if root is None:
                return 0
            
            l = path(root.left, self.res)
            r = path(root.right , self.res)
            temp = max(max(l,r)+root.val , root.val)
            ans = max(temp , l+r+root.val)
            self.res = max(self.res, ans)
            return temp
        path(root, self.res)
        return self.res
        