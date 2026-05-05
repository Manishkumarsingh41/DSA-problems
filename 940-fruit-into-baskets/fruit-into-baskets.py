class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        wind = Counter()
        max_fruits = 0
        l = 0

        for r in range(len(fruits)):
            wind[fruits[r]] += 1
            while len(wind)> 2:
                wind[fruits[l]] -= 1
                if wind[fruits[l]]== 0:
                    del wind[fruits[l]]
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits        