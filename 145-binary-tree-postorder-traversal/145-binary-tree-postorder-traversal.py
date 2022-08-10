class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return None
        elements = []
        if root.left:
            elements += self.postorderTraversal(root.left)
        if root.right:
            elements += self.postorderTraversal(root.right)

        elements.append(root.val)

        return elements