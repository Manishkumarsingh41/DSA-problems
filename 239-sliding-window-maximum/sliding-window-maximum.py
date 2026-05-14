class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()
        i = j = 0

        while j < len(nums):
            while q and nums[j] > q[len(q) - 1]:
                q.pop()
            q.append(nums[j])

            if j >= k - 1:
                res.append(q[0])
                if nums[i] == q[0]:
                    q.popleft()
                i += 1
            j += 1
        return res

            
        