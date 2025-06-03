from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        queue = deque([(root, None, 0)])
        x_info = y_info = None

        while queue:
            node, parent, depth = queue.popleft()
            if node.val == x:
                x_info = (parent, depth)
            if node.val == y:
                y_info = (parent, depth)
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
            if x_info and y_info:
                break
        
        if x_info and y_info:
            return x_info[1] == y_info[1] and x_info[0] != y_info[0]
        return False
