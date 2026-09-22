class SegmentTree:
    def __init__(self, nums, k):
        self.k = k
        self.n = len(nums)
        self.prod = [1] * (4 * self.n)
        self.cnt = [[0] * k for _ in range(4 * self.n)]
        self._build(1, 0, self.n - 1, nums)

    def _set_leaf(self, node, value):
        r = value % self.k
        self.prod[node] = r
        self.cnt[node] = [0] * self.k
        self.cnt[node][r] = 1

    def _merge(self, node, left, right):
        lp, rp = self.prod[left], self.prod[right]
        lc, rc = self.cnt[left], self.cnt[right]
        self.prod[node] = (lp * rp) % self.k
        c = self.cnt[node]
        for v in range(self.k):
            c[v] = lc[v]
        for v in range(self.k):
            if rc[v]:
                c[(lp * v) % self.k] += rc[v]

    def _build(self, node, l, r, nums):
        if l == r:
            self._set_leaf(node, nums[l])
            return
        m = (l + r) // 2
        self._build(node * 2, l, m, nums)
        self._build(node * 2 + 1, m + 1, r, nums)
        self._merge(node, node * 2, node * 2 + 1)

    def update(self, node, l, r, i, value):
        if l == r:
            self._set_leaf(node, value)
            return
        m = (l + r) // 2
        if i <= m:
            self.update(node * 2, l, m, i, value)
        else:
            self.update(node * 2 + 1, m + 1, r, i, value)
        self._merge(node, node * 2, node * 2 + 1)

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.prod[node], self.cnt[node]
        m = (l + r) // 2
        if qr <= m:
            return self.query(node * 2, l, m, ql, qr)
        if ql > m:
            return self.query(node * 2 + 1, m + 1, r, ql, qr)

        lp, lc = self.query(node * 2, l, m, ql, qr)
        rp, rc = self.query(node * 2 + 1, m + 1, r, ql, qr)

        # Inline merge for two returned nodes
        p = (lp * rp) % self.k
        c = lc[:]
        for v in range(self.k):
            if rc[v]:
                c[(lp * v) % self.k] += rc[v]
        return p, c


class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        seg = SegmentTree(nums, k)
        ans = []
        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            _, cnt = seg.query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])
        return ans