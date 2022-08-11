# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        def helper(node):
            if node is not None:
                helper(node.left)
                self.nodes.append(node.val)
                helper(node.right)

        helper(root)
        self.pointer = 0
    def next(self) -> int:
        self.pointer+=1
        return self.nodes[self.pointer-1]

    def hasNext(self) -> bool:
        if self.pointer > len(self.nodes) - 1:
            return False
        else:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()