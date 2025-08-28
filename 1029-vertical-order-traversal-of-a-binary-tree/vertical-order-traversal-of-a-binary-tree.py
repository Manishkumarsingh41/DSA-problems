class Solution:
    def verticalTraversal(self, root):
        nodes = []  # yaha sab (col, row, val) store karenge
        
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))  # current node info daal diya
            dfs(node.left, row + 1, col - 1)   # left child -> col-1, row+1
            dfs(node.right, row + 1, col + 1)  # right child -> col+1, row+1
        
        dfs(root, 0, 0)
        
        # sort by col -> row -> val
        nodes.sort()
        
        res = []
        prev_col = None
        col_group = []
        
        for col, row, val in nodes:
            if prev_col is None or col == prev_col:  # same col me add karo
                col_group.append(val)
            else:
                res.append(col_group)  # purana column group add kar diya
                col_group = [val]      # naya group shuru
            prev_col = col
        
        if col_group:  # last group bacha hua hoga
            res.append(col_group)
        
        return res
