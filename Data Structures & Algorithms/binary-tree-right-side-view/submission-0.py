# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rows = defaultdict(list)

        def bfs(node,row,col):
            if not node:
                return
            
            rows[row].append([node.val,col])
            bfs(node.left,row + 1, col - 1)
            bfs(node.right,row + 1, col + 1)
        
        bfs(root,0,0)

        res = []
        for row in sorted(rows):
            res.append(rows[row][-1][0])
        
        return res