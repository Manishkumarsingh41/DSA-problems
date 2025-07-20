class Solution:
    def simplifyPath(self, p):
        s = []
        for x in p.split('/'):
            if x == '' or x == '.':
                continue
            elif x == '..':
                if s: s.pop()
            else:
                s.append(x)
        return '/' + '/'.join(s)
