class Solution:
    def firstUniqChar(self, s):
        count = {}
        queue = []

        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                queue.append((s[i], i))

        return queue[0][1] if queue else -1
