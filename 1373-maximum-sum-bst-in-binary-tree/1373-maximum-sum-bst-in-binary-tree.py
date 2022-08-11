# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        #return (low, high,sum, isValid)
        def dfs(node):
            if not node:
                return (float("infinity"),float("-infinity"),0,True)
            left_low,left_high,left_sum,left_valid=dfs(node.left)
            right_low,right_high,right_sum,right_valid=dfs(node.right)
            
            subtree_valid=left_valid and right_valid and node.val>left_high and node.val<right_low
            if subtree_valid:
                subtree_sum=left_sum+right_sum+node.val
            else:
                subtree_sum=-1
            self.answer=max(self.answer,subtree_sum)
            return(min(node.val,left_low),max(node.val,right_high),subtree_sum,subtree_valid)
            
        
        self.answer=0
        dfs(root)
        return self.answer

        