class Solution:
    def preorder(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                stack.extend(reversed(node.children))

        return result
