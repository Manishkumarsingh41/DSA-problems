class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        
        def dfs(node, path):
            if not node:
                return
            # current path me add karo
            path += str(node.val)
            # leaf node
            if not node.left and not node.right:
                res.append(path)
                return
            # non-leaf -> add '->' aur continue
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return res