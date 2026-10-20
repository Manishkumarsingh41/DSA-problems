class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False
        dot = False
        e = False
        digit_after_e = True
        for i, c in enumerate(s):
            if c.isdigit():
                digit = True
                digit_after_e = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if dot or e:
                    return False
                dot = True
            elif c in 'eE':
                if e or not digit:
                    return False
                e = True
                digit_after_e = False
            else:
                return False
        return digit and digit_after_e
        