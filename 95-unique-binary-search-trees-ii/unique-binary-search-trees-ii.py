class Solution:
    def generateTrees(self, n):
        # Helper function: given start..end, return all unique BSTs
        def generate(start, end):
            if start > end:
                return [None]  # Empty tree valid hai

            all_trees = []
            # Har number ko root maan kar try karenge
            for root in range(start, end+1):
                left_trees = generate(start, root-1)   # Left subtree
                right_trees = generate(root+1, end)   # Right subtree

                # Har left aur right ko combine karo
                for l in left_trees:
                    for r in right_trees:
                        current = TreeNode(root)  # Naya root
                        current.left = l
                        current.right = r
                        all_trees.append(current)

            return all_trees

        return generate(1, n) if n else []
