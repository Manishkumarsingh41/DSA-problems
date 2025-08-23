class Solution:
    def hasPathSum(self, root, targetSum):
        # Agar root hi None hai (empty tree) => koi path possible nahi
        if not root:
            return False

        # Agar leaf node (na left hai na right)
        # To check karenge kya targetSum == node ka value
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursively check karenge left aur right subtree me
        # Har step pe targetSum me se current node ka value minus karenge
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
