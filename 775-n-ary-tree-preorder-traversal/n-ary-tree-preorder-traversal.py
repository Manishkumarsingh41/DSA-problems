class Solution:
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + sum([self.preorder(child) for child in root.children], [])
