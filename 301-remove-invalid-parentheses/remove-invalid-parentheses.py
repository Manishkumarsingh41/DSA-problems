class Solution:
    def removeInvalidParentheses(self, s):
        left_rem = right_rem = 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = []
        seen = set()
        chars = list(s)

        def dfs(idx, lr, rr, open_count, path):
            if idx == len(chars):
                if lr == 0 and rr == 0 and open_count == 0:
                    t = ''.join(path)
                    if t not in seen:
                        seen.add(t)
                        result.append(t)
                return

            if lr + rr > len(chars) - idx:
                return

            c = chars[idx]

            if c == '(':
                if lr > 0:
                    dfs(idx + 1, lr - 1, rr, open_count, path)
                path.append(c)
                dfs(idx + 1, lr, rr, open_count + 1, path)
                path.pop()
            elif c == ')':
                if rr > 0:
                    dfs(idx + 1, lr, rr - 1, open_count, path)
                if open_count > 0:
                    path.append(c)
                    dfs(idx + 1, lr, rr, open_count - 1, path)
                    path.pop()
            else:
                path.append(c)
                dfs(idx + 1, lr, rr, open_count, path)
                path.pop()

        dfs(0, left_rem, right_rem, 0, [])
        return result