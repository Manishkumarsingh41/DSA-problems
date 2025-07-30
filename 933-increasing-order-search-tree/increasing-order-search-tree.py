class Solution:
    def increasingBST(self, root):

        def inorder(node):
            if not node:
                return
            inorder(node.left)   # left subtree visit karna hai
            vals.append(node)        # current node ko list me daalna hai
            inorder(node.right)       # ab right subtree visit karna hai

        vals = []                      # sorted order ke liye list banayi
        inorder(root)                   # inorder se sab node visit kar liye

        dummy = TreeNode(0)    # ek dummy node banaya start point ke liye
        curr = dummy                  # curr ko dummy pe point kiya

        for node in vals:
            node.left = None         # left null karna hai kyunki line mein jodna hai
            curr.right = node       # right mein node ko jod diya
            curr = node       # curr aage badh gaya next jodne ke liye

        return dummy.right        # dummy ke right mein final answer milta hai
