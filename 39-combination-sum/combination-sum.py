class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, curr, total):
            # base case
            if total == target:
                res.append(list(curr))  # valid combo mila
                return
            if total > target:
                return  # invalid, sum exceed

            for i in range(start, len(candidates)):
                # number choose karo
                curr.append(candidates[i])
                # same index se call (repeat allowed)
                backtrack(i, curr, total + candidates[i])
                # backtrack (last number hatao)
                curr.pop()

        backtrack(0, [], 0)
        return res
