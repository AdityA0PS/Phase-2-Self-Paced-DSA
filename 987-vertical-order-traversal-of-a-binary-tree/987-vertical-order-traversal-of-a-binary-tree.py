# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        queue = collections.deque([])
        queue.append((root, 0))
        colList = defaultdict(list)
        levelTemp = defaultdict(list)
        minCol = maxCol = 0

        while queue:
            n = len(queue)
            for i in range(n):
                node, col = queue.popleft()
                if node:
                    levelTemp[col].append(node.val)
                    minCol = min(minCol, col)
                    maxCol = max(maxCol, col)

                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
                if i == n - 1:
                    for column in levelTemp:
                        if len(levelTemp[column]) > 1:
                            levelTemp[column].sort()
                        colList[column] += levelTemp[column]
                    levelTemp.clear()                    

        result = []
        for i in range(minCol, maxCol + 1):
            result.append(colList[i])

        return result
        