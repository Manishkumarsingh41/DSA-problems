class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.q = []  # sirf incomplete nodes ka queue
        bfs = [root]
        while bfs:
            node = bfs.pop(0)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
            if not (node.left and node.right):
                self.q.append(node)  # ye node abhi incomplete hai

    def insert(self, val):
        parent = self.q[0]  # front of queue -> parent
        new_node = TreeNode(val)
        if not parent.left:
            parent.left = new_node  # left fill karo
        elif not parent.right:
            parent.right = new_node  # right fill karo
            self.q.pop(0)  # ab parent full ho gaya, queue se hatao
        self.q.append(new_node)  # naya node future me parent ban sakta hai
        return parent.val  # parent ka value return

    def get_root(self):
        return self.root