class Solution:
    def postorder(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.insert(0, node.val)
            if node.children:
                stack.extend(node.children)

        return result
