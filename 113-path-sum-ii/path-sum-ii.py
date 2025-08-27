class Solution:
    def pathSum(self, root, targetSum):
        res = []

        def dfs(node, path, total):
            if not node:
                return

            # current node ko path me add karo
            path.append(node.val)
            total += node.val

            # agar leaf node aur sum match kare
            if not node.left and not node.right and total == targetSum:
                res.append(list(path))   # ek copy store karna hoga

            # left aur right me jao
            dfs(node.left, path, total)
            dfs(node.right, path, total)

            # backtrack (last element hata do)
            path.pop()

        dfs(root, [], 0)
        return res