# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def helper(root):
            nonlocal isBalanced
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            if (left-right) >= 2 or (right-left) >= 2:
                isBalanced = False
            
            return max(left, right)+1
        helper(root)
        return isBalanced
