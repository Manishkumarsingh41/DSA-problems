class Solution:
    def rightSideView(self, root):
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):  # first node at this depth
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
