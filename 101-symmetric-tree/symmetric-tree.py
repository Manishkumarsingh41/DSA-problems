class Solution:
    def isMirror(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (a.val == b.val and
                self.isMirror(a.left, b.right) and
                self.isMirror(a.right, b.left))

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
