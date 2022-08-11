# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def __init__(self):
		self.ri = []
		self.le = []
	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.left)
			self.le.append(res)
			res.append(root.val)
			res = res + self.inorderTraversal(root.right)
			self.ri.append(res)
		return res
	def isSameTree(self, p, q):
		a = self.inorderTraversal(q)
		x = self.le + self.ri
		self.le = []
		self.ri = []
		b = self.inorderTraversal(p)
		y = self.le + self.ri
		if y != x:
			return False
		if y == x:
			return True    