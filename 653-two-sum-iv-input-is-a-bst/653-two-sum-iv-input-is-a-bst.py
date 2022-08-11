# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = []
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dfs(root)
        left = 0
        right = len(self.nums) - 1
        while left < right:
            if self.nums[left] + self.nums[right] > k:
                right -= 1
            elif self.nums[left] + self.nums[right] < k:
                left += 1
            else:
                return True
        return False
        
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.nums.append(root.val)
        self.dfs(root.right)
