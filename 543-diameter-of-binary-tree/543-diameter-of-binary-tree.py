# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, height):
        if (root == None):
            return (0)
        left = self.dfs(root.left, height + 1)
        right = self.dfs(root.right, height + 1)
        if (left + right > self.ans):
            self.ans = left + right
        if (left > right):
            return (left + 1)
        return right + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        if root == None:
            return (0)
        self.dfs(root, 0)
        return self.ans