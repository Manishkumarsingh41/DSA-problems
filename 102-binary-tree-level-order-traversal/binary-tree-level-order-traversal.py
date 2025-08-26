class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = [root]   # simple list ko queue ki tarah use karenge
        res = []

        while q:
            level = []
            size = len(q)  # current level ke nodes count

            for i in range(size):
                node = q.pop(0)  # list me se pehla element nikaalo
                level.append(node.val)

                if node.left:   # left child
                    q.append(node.left)
                if node.right:  # right child
                    q.append(node.right)

            res.append(level)

        return res
