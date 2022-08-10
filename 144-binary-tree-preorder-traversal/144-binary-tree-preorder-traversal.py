class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while (stack):
            cur = stack.pop()
            if cur == None:
                continue
            ans.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return ans