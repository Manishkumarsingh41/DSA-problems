class Solution(object):
    def balanceBST(self, root):
        ans = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        def build(l, r):
            if l > r:
                return None 
            mid = (l + r) // 2
            new_node = TreeNode(ans[mid])
            new_node.left = build(l, mid - 1)
            new_node.right = build(mid + 1, r)
            return new_node
            
        return build(0, len(ans) - 1)
