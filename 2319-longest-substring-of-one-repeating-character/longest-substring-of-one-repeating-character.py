class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        chars = list(s)
        
        length = [1] * (4*n)
        pref = [1] * (4*n)
        suff = [1] * (4*n)
        
        def build(node, l, r):
            if l == r: return
            mid = (l+r)//2
            build(node*2, l, mid)
            build(node*2+1, mid+1, r)
            merge(node, l, mid, r)
        
        def merge(node, l, mid, r):
            left, right = node*2, node*2+1
            pref[node] = pref[left]
            suff[node] = suff[right]
            length[node] = max(length[left], length[right])
            if chars[mid] == chars[mid+1]:
                length[node] = max(length[node], suff[left] + pref[right])
                if pref[left] == mid-l+1:
                    pref[node] = pref[left] + pref[right]
                if suff[right] == r-mid:
                    suff[node] = suff[right] + suff[left]
        
        def update(node, l, r, pos):
            if l == r: return
            mid = (l+r)//2
            if pos <= mid: update(node*2, l, mid, pos)
            else: update(node*2+1, mid+1, r, pos)
            merge(node, l, mid, r)
        
        build(1, 0, n-1)
        ans = []
        
        for c, i in zip(queryCharacters, queryIndices):
            chars[i] = c
            update(1, 0, n-1, i)
            ans.append(length[1])
        
        return ans