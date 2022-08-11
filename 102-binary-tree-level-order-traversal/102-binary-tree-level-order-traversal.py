# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHash(self, root:TreeNode, hasht={}, lvl=0):
        if root is None:
            return []
        if hasht.get(lvl, None):
            hasht[lvl].append(root.val)
        else:
            hasht[lvl] = [root.val]
        if root.left:
            self.getHash(root.left, hasht, lvl+1) 
        if root.right:
            self.getHash(root.right, hasht, lvl+1)
        
        return hasht

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashT = self.getHash(root, {}, 0)
        res = []
        for i in range(len(hashT)):
            res.append(hashT[i])

        return res