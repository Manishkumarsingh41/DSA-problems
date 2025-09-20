from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()
        self.seen = set()
        self.dest = defaultdict(list)
        self.proc = defaultdict(int)

    def addPacket(self, s: int, d: int, t: int) -> bool:
        if (s, d, t) in self.seen: return False
        if len(self.q) == self.memoryLimit: self.forwardPacket()
        self.q.append((s, d, t)); self.seen.add((s, d, t))
        self.dest[d].append(t); return True

    def forwardPacket(self):
        if not self.q: return []
        s, d, t = self.q.popleft(); self.seen.remove((s, d, t))
        self.proc[d] += 1; return [s, d, t]

    def getCount(self, d: int, l: int, r: int) -> int:
        ts = self.dest.get(d, []); lo = self.proc[d]
        return bisect_right(ts, r, lo) - bisect_left(ts, l, lo)
