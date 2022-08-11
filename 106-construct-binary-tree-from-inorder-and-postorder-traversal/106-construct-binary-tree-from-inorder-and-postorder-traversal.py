# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.seen = {}
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return
        
        val = postorder[-1]
        
        if val in self.seen:
            return self.seen[val]
        
        vertex = TreeNode(val=val)
        mid = inorder.index(val)
        
        vertex.left = self.buildTree(inorder[:mid], postorder[:mid])
        vertex.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        self.seen[val] = vertex
        
        return vertex