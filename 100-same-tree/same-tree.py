class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q: continue
            if not p or not q or p.val != q.val: return False
            stack.extend([(p.left, q.left), (p.right, q.right)])
        return True
