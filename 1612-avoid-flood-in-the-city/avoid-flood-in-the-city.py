class Solution(object):
    def avoidFlood(self, rains):
        full = {}
        dry = []
        res = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
            else:
                if lake in full:
                    j = bisect.bisect_right(dry, full[lake])
                    if j == len(dry):
                        return []
                    res[dry.pop(j)] = lake
                full[lake] = i
        
        for i in dry:
            res[i] = 1
        return res